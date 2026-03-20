## ============================================================================
## VHS SHADER FOR REN'PY
## ============================================================================
## Original full-featured shader with structural performance fixes:
##   - gl_pixel_perfect True (render at texture size, not display size)
##   - 30fps redraw cap (VHS was 30fps — authentic AND saves GPU)
##   - Tighter mesh_pad (no oversized texture allocation)
##   - ALU-only hash function (no sin()-based hashing)
## ============================================================================

init python:
    renpy.register_shader("custom.vhs",
        variables="""
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        uniform float u_time;
        uniform float u_chroma_amount;
        uniform float u_scanline_strength;
        uniform float u_noise_strength;
        uniform float u_distortion_strength;
        uniform float u_bleed_amount;
        uniform float u_vignette_strength;
        uniform float u_desaturation;
        uniform float u_tape_glitch;
        varying vec2 v_tex_coord;
        """,
        fragment_functions="""
        float vhs_hash(vec2 p) {
            vec3 p3 = fract(vec3(p.xyx) * 0.1031);
            p3 += dot(p3, p3.yzx + 33.33);
            return fract((p3.x + p3.y) * p3.z);
        }
        """,
        fragment_300="""
        vec2 uv = v_tex_coord;
        vec2 px_size = 1.0 / u_model_size;
        float time = u_time;

        // === TRACKING DISTORTION (horizontal wobble) ===
        float distort = u_distortion_strength * px_size.x;
        float wave_slow = sin(uv.y * 5.0 + time * 1.5) * 3.0;
        float wave_fast = sin(uv.y * 120.0 + time * 30.0) * 0.3;
        float wave_drift = sin(uv.y * 35.0 - time * 4.0) * 0.8;
        float h_offset = (wave_slow + wave_fast + wave_drift) * distort;

        // Occasional strong horizontal shift (tracking slip)
        float slip_trigger = step(0.993, vhs_hash(vec2(floor(time * 3.0), 1.0)));
        float slip_band = 1.0 - smoothstep(0.0, 0.02, abs(uv.y - fract(time * 0.7)));
        h_offset += slip_trigger * slip_band * distort * 40.0;

        uv.x += h_offset;

        // === TAPE GLITCH BAND (noisy band rolling across screen) ===
        float glitch_pos = fract(time * 0.05);
        float glitch_band = smoothstep(glitch_pos - 0.01, glitch_pos, uv.y)
                          - smoothstep(glitch_pos, glitch_pos + u_tape_glitch, uv.y);
        float glitch_noise = vhs_hash(vec2(uv.x * 100.0, floor(time * 20.0))) * glitch_band;
        uv.x += glitch_noise * 0.03 * u_distortion_strength;

        // === CHROMATIC ABERRATION ===
        vec2 chroma_offset = vec2(u_chroma_amount, 0.5) * px_size;
        vec2 offset_r = vec2(-chroma_offset.x, chroma_offset.y * 0.3);
        vec2 offset_b = vec2( chroma_offset.x, -chroma_offset.y * 0.3);

        vec4 col_r = texture2D(tex0, uv + offset_r);
        vec4 col_g = texture2D(tex0, uv);
        vec4 col_b = texture2D(tex0, uv + offset_b);

        vec4 color = vec4(col_r.r, col_g.g, col_b.b, col_g.a);

        // === COLOR BLEEDING (horizontal smear) ===
        float bleed = u_bleed_amount * px_size.x;
        vec4 bleed_sample = vec4(0.0);
        bleed_sample += texture2D(tex0, uv + vec2(bleed * 1.0, 0.0));
        bleed_sample += texture2D(tex0, uv + vec2(bleed * 2.0, 0.0));
        bleed_sample += texture2D(tex0, uv + vec2(bleed * 3.0, 0.0));
        bleed_sample += texture2D(tex0, uv + vec2(bleed * 4.0, 0.0));
        bleed_sample /= 4.0;

        float bleed_mix = 0.15 * step(0.01, u_bleed_amount);
        color.rgb = mix(color.rgb, bleed_sample.rgb, bleed_mix);

        // === SCANLINES ===
        float scanline = sin(uv.y * u_model_size.y * 3.14159) * 0.5 + 0.5;
        scanline = pow(scanline, 1.5);
        scanline = 1.0 - (u_scanline_strength * (1.0 - scanline));
        color.rgb *= scanline;

        // === STATIC NOISE ===
        float static_noise = vhs_hash(vec2(uv.x * u_model_size.x, uv.y * u_model_size.y + time * 1000.0));
        float burst = step(0.985, vhs_hash(vec2(floor(time * 8.0), 0.0)));
        float noise_amount = u_noise_strength * (0.08 + burst * 0.35);
        color.rgb += (static_noise - 0.5) * noise_amount;

        // Tape glitch band adds extra noise
        color.rgb += glitch_band * (static_noise - 0.5) * 0.5 * u_tape_glitch;

        // === DESATURATION (washed-out VHS look) ===
        float luma = dot(color.rgb, vec3(0.299, 0.587, 0.114));
        color.rgb = mix(color.rgb, vec3(luma), u_desaturation);

        // Slight warm tint (VHS tapes skew warm)
        color.r += 0.01 * u_desaturation;
        color.b -= 0.015 * u_desaturation;

        // === VIGNETTE ===
        vec2 vig_uv = v_tex_coord * (1.0 - v_tex_coord);
        float vig = vig_uv.x * vig_uv.y * 15.0;
        vig = pow(vig, u_vignette_strength);
        color.rgb *= vig;

        // === SLIGHT BRIGHTNESS FLUCTUATION ===
        float flicker = 1.0 + 0.02 * sin(time * 12.0) + 0.01 * sin(time * 37.0);
        color.rgb *= flicker;

        // Clamp and output
        color.rgb = clamp(color.rgb, 0.0, 1.0);
        gl_FragColor = color;
        """)


## ============================================================================
## TRANSFORMS
## ============================================================================

transform vhs(
    chroma=4.0,
    scanlines=0.25,
    noise=1.0,
    distortion=1.0,
    bleed=3.0,
    vignette=0.35,
    desat=0.2,
    glitch=0.05
    ):
    mesh True
    gl_pixel_perfect True
    mesh_pad (int(chroma + 6), 0, int(chroma + 6), 0)
    shader "custom.vhs"
    u_chroma_amount float(chroma)
    u_scanline_strength float(scanlines)
    u_noise_strength float(noise)
    u_distortion_strength float(distortion)
    u_bleed_amount float(bleed)
    u_vignette_strength float(vignette)
    u_desaturation float(desat)
    u_tape_glitch float(glitch)
    pause 1.0 / 30.0
    repeat


## ============================================================================
## PRESETS
## ============================================================================

transform vhs_subtle:
    vhs(
        chroma=2.0,
        scanlines=0.1,
        noise=0.4,
        distortion=0.3,
        bleed=1.0,
        vignette=0.25,
        desat=0.08,
        glitch=0.01
    )

transform vhs_normal:
    vhs(
        chroma=4.0,
        scanlines=0.25,
        noise=1.0,
        distortion=1.0,
        bleed=3.0,
        vignette=0.35,
        desat=0.2,
        glitch=0.05
    )

transform vhs_worn:
    vhs(
        chroma=6.0,
        scanlines=0.35,
        noise=1.8,
        distortion=2.0,
        bleed=5.0,
        vignette=0.45,
        desat=0.35,
        glitch=0.12
    )

transform vhs_damaged:
    vhs(
        chroma=10.0,
        scanlines=0.5,
        noise=3.0,
        distortion=4.0,
        bleed=8.0,
        vignette=0.55,
        desat=0.45,
        glitch=0.25
    )

transform vhs_glitch:
    vhs(
        chroma=15.0,
        scanlines=0.6,
        noise=5.0,
        distortion=8.0,
        bleed=10.0,
        vignette=0.6,
        desat=0.5,
        glitch=0.5
    )

transform vhs_scanlines_only:
    vhs(
        chroma=0.0,
        scanlines=0.4,
        noise=0.0,
        distortion=0.0,
        bleed=0.0,
        vignette=0.3,
        desat=0.0,
        glitch=0.0
    )

transform vhs_static_only:
    vhs(
        chroma=0.0,
        scanlines=0.0,
        noise=5.0,
        distortion=0.0,
        bleed=0.0,
        vignette=0.0,
        desat=0.0,
        glitch=0.0
    )


## ============================================================================
## USAGE
## ============================================================================
##
##     scene bg room at vhs_normal
##     show eileen happy at vhs_subtle
##     scene bg room at vhs(chroma=3.0, noise=2.0, distortion=1.5)
##
## ============================================================================
