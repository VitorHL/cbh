## ============================================================================
## VHS & CRT SHADER FOR REN'PY (ADVANCED THEORY EDITION)
## ============================================================================

init python:
    # ------------------------------------------------------------------------
    # 1. UNIFIED SINGLE-PASS SHADER (Full compatibility)
    # ------------------------------------------------------------------------
    renpy.register_shader("custom.vhs",
        variables="""
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        uniform float u_time;
        uniform float u_chroma_amount;
        uniform float u_scanline_strength;
        uniform float u_noise_strength;
        uniform float u_wobble;
        uniform float u_jitter;
        uniform float u_slip;
        uniform float u_bleed_amount;
        uniform float u_vignette_strength;
        uniform float u_desaturation;
        uniform float u_tape_glitch;
        uniform float u_edge_lock;
        uniform float u_warp;
        uniform float u_luma_bandwidth;
        uniform float u_chroma_bandwidth;
        uniform float u_decoder_type;
        uniform float u_glitch_size;
        uniform float u_glitch_stretch;
        uniform float u_glitch_speed;
        uniform float u_glitch_edge;
        uniform float u_glitch_delay_min;
        uniform float u_glitch_delay_max;
        uniform float u_roll_speed;
        uniform float u_noise_band_size;
        uniform float u_noise_band_speed;
        uniform float u_noise_band_edge;
        uniform float u_noise_band_delay_min;
        uniform float u_noise_band_delay_max;
        uniform float u_noise_band_intensity;
        varying vec2 v_tex_coord;
        """,
        fragment_functions="""
        float vhs_hash(vec2 p) {
            vec3 p3 = fract(vec3(p.xyx) * 0.1031);
            p3 += dot(p3, p3.yzx + 33.33);
            return fract((p3.x + p3.y) * p3.z);
        }

        float filterChannel(sampler2D tex, vec2 uv, vec3 coeffs, float filter_width, vec2 res) {
            if (filter_width <= 0.05) {
                return dot(texture2D(tex, uv).rgb, coeffs);
            }
            float accumulated_val = 0.0;
            float total_weight = 0.0;
            const int radius = 4;
            for (int i = -radius; i <= radius; i++) {
                float offset = float(i) * filter_width / res.x;
                vec3 neighbor_rgb = texture2D(tex, uv + vec2(offset, 0.0)).rgb;
                float val = dot(neighbor_rgb, coeffs);
                float weight = exp(-0.5 * float(i * i) / 4.0);
                accumulated_val += val * weight;
                total_weight += weight;
            }
            return accumulated_val / total_weight;
        }
        """,
        fragment_300="""
        vec2 uv = v_tex_coord;
        vec2 px_size = 1.0 / u_model_size;
        float time = u_time;

        // === EDGE LOCK MASK ===
        float edge_mask = 1.0;
        if (u_edge_lock > 0.5) {
            float margin = 0.05;
            edge_mask = smoothstep(0.0, margin, v_tex_coord.x)
                      * smoothstep(0.0, margin, 1.0 - v_tex_coord.x)
                      * smoothstep(0.0, margin, v_tex_coord.y)
                      * smoothstep(0.0, margin, 1.0 - v_tex_coord.y);
        }

        // === 1. CRT SCREEN CURVATURE ===
        if (u_warp > 0.0) {
            vec2 ndc = uv * 2.0 - 1.0;
            ndc.x *= 1.0 + u_warp * 0.03 * (ndc.y * ndc.y);
            ndc.y *= 1.0 + u_warp * 0.04 * (ndc.x * ndc.x);
            uv = ndc * 0.5 + 0.5;
        }

        // Bezel clipping
        if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
            gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
            return;
        }

        // === 1.5 V-SYNC ROLL (Vertical Hold Loss) ===
        if (u_roll_speed > 0.001) {
            float roll_offset = time * u_roll_speed;
            uv.y = fract(uv.y - roll_offset);
        }

        // === 2. TAPE TRANSPORT INSTABILITY ===
        if (u_slip > 0.001) {
            float bounce_trigger = step(0.92, sin((time * 2.5) + 1.2 + cos(((time * 2.5) + 1.2) * 0.7)));
            float vertical_offset = bounce_trigger * 0.015 * sin(time * 8.0) * u_slip;
            uv.y = mod(uv.y - vertical_offset, 1.0);
        }

        float wave_slow = sin(uv.y * 30.0 + time * 12.0);
        float line_noise = vhs_hash(vec2(uv.y * 250.0, time));
        uv.x += wave_slow * 0.0025 * u_wobble * (0.3 + 0.7 * line_noise) * edge_mask;

        float jitter_noise = vhs_hash(vec2(uv.y * 500.0, time * 2.0));
        uv.x += (jitter_noise - 0.5) * 0.0015 * u_jitter * edge_mask;

        float switch_zone = 0.06;
        if (uv.y > 1.0 - switch_zone) {
            float normalized_dist = (uv.y - (1.0 - switch_zone)) / switch_zone;
            float horizontal_skew = pow(normalized_dist, 4.0) * 0.035 * u_wobble;
            uv.x += horizontal_skew * sin(time * 15.0) * edge_mask;
        }

        // === TAPE TRACKING BAND ===
        float min_s = u_glitch_delay_min / 1000.0;
        float max_s = u_glitch_delay_max / 1000.0;
        float travel_dist = 1.6;
        float scroll_duration = travel_dist / max(u_glitch_speed, 0.001);
        
        float max_cycle = max_s + scroll_duration;
        float cycle_index = floor(time / max_cycle);
        float local_time = mod(time, max_cycle);
        
        float random_delay = mix(min_s, max_s, vhs_hash(vec2(cycle_index, 123.45)));
        
        float glitch_pos = -10.0;
        if (local_time >= random_delay) {
            glitch_pos = -0.3 + ((local_time - random_delay) / scroll_duration) * travel_dist;
        }
        
        float core_size = u_glitch_size;
        float inner_soft = core_size * clamp(u_glitch_edge, 0.0, 1.0);
        
        float glitch_band = smoothstep(glitch_pos - core_size, glitch_pos - core_size + inner_soft, v_tex_coord.y)
                          - smoothstep(glitch_pos + core_size - inner_soft, glitch_pos + core_size, v_tex_coord.y);
                          
        float dist_to_center = v_tex_coord.y - glitch_pos;
        float stretch_factor = clamp(u_glitch_stretch, 0.0, 1.0);
        
        uv.y -= dist_to_center * glitch_band * stretch_factor;
        uv.y = fract(uv.y);

        // === SECONDARY NOISE BAND ===
        float n_min_s = u_noise_band_delay_min / 1000.0;
        float n_max_s = u_noise_band_delay_max / 1000.0;
        float n_travel_dist = 1.6;
        float n_scroll_duration = n_travel_dist / max(u_noise_band_speed, 0.001);
        
        float n_max_cycle = n_max_s + n_scroll_duration;
        float n_cycle_index = floor(time / n_max_cycle);
        float n_local_time = mod(time, n_max_cycle);
        
        float n_random_delay = mix(n_min_s, n_max_s, vhs_hash(vec2(n_cycle_index, 777.77)));
        
        float noise_band_pos = -10.0;
        if (n_local_time >= n_random_delay) {
            noise_band_pos = -0.3 + ((n_local_time - n_random_delay) / n_scroll_duration) * n_travel_dist;
        }
        
        float n_core_size = u_noise_band_size;
        float n_inner_soft = n_core_size * clamp(u_noise_band_edge, 0.0, 1.0);
        
        float noise_band_mask = smoothstep(noise_band_pos - n_core_size, noise_band_pos - n_core_size + n_inner_soft, v_tex_coord.y)
                              - smoothstep(noise_band_pos + n_core_size - n_inner_soft, noise_band_pos + n_core_size, v_tex_coord.y);

        // === 3. NTSC COMPOSITE & BLEED ===
        vec3 Y_COEFFS = vec3(0.299, 0.587, 0.114);
        vec3 I_COEFFS = vec3(0.5959, -0.2744, -0.3216);
        vec3 Q_COEFFS = vec3(0.2115, -0.5229, 0.3114);

        mat3 YIQ_TO_RGB_MATRIX = mat3(
            1.0,       1.0,       1.0,
            0.9563,   -0.2720,   -1.1063,
            0.6210,   -0.6474,    1.7046
        );

        float bleed_strength = u_bleed_amount * px_size.x * 12.0;
        vec2 uv_I = uv - vec2(0.5 * bleed_strength, 0.0);
        vec2 uv_Q = uv - vec2(1.2 * bleed_strength, 0.0);

        float chroma_bw = max(u_chroma_bandwidth, 0.1);
        float luma_bw = max(u_luma_bandwidth, 0.1);
        
        float Y_raw = filterChannel(tex0, uv, Y_COEFFS, 0.0, u_model_size);
        float Y_decoded = Y_raw;
        
        if (u_decoder_type < 0.5) {
            Y_decoded = filterChannel(tex0, uv, Y_COEFFS, 3.0 / luma_bw, u_model_size);
        } else {
            vec2 prev_line_uv = uv - vec2(0.0, px_size.y);
            float Y_prev = filterChannel(tex0, prev_line_uv, Y_COEFFS, 0.0, u_model_size);
            Y_decoded = mix(Y_raw, (Y_raw + Y_prev) * 0.5, 0.8);
        }

        float I_val = filterChannel(tex0, uv_I, I_COEFFS, 2.5 / chroma_bw, u_model_size);
        float Q_val = filterChannel(tex0, uv_Q, Q_COEFFS, 7.5 / chroma_bw, u_model_size);

        vec2 px_coord = uv * u_model_size;
        float subcarrier_freq = 0.45;
        float phase_step = (px_coord.x * subcarrier_freq) + (px_coord.y * 3.141592) + (time * 29.97);

        Y_decoded += (I_val * cos(phase_step) + Q_val * sin(phase_step)) * u_chroma_amount * 0.15;

        float high_freq_luma = Y_raw - Y_decoded;
        I_val += high_freq_luma * u_chroma_amount * cos(phase_step) * 0.12;
        Q_val += high_freq_luma * u_chroma_amount * sin(phase_step) * 0.12;

        vec3 yiq = vec3(Y_decoded, I_val, Q_val);
        vec3 color_rgb = YIQ_TO_RGB_MATRIX * yiq;

        // === 4. CHROMATIC ABERRATION ===
        vec2 chroma_offset = vec2(u_chroma_amount * 0.5, 0.2) * px_size;
        
        float r_val = texture2D(tex0, uv - chroma_offset).r;
        float b_val = texture2D(tex0, uv + chroma_offset).b;
        color_rgb.r = mix(color_rgb.r, r_val, 0.35);
        color_rgb.b = mix(color_rgb.b, b_val, 0.35);

        // === 5. STATIC NOISE & BLOOMING ===
        float static_noise = vhs_hash(vec2(v_tex_coord.x * u_model_size.x, v_tex_coord.y * u_model_size.y + time * 1000.0));
        float burst = step(0.985, vhs_hash(vec2(floor(time * 8.0), 0.0)));
        float noise_amount = u_noise_strength * (0.08 + burst * 0.35);
        color_rgb += (static_noise - 0.5) * noise_amount;

        float bloom = glitch_band * 0.3 * u_tape_glitch;
        color_rgb += bloom;
        color_rgb += glitch_band * (static_noise - 0.5) * 0.2 * u_tape_glitch;
        
        float intense_noise = (static_noise - 0.5) * u_noise_band_intensity * noise_band_mask;
        color_rgb += intense_noise;
        color_rgb += noise_band_mask * 0.15 * u_noise_band_intensity;

        // === 6. DESATURATION & TINT ===
        float luma_gray = dot(color_rgb, vec3(0.299, 0.587, 0.114));
        color_rgb = mix(color_rgb, vec3(luma_gray), u_desaturation);

        color_rgb.r += 0.012 * u_desaturation;
        color_rgb.b -= 0.008 * u_desaturation;

        // === 7. CRT SCANLINES ===
        float scanline_coord = v_tex_coord.y * u_model_size.y;
        float dist_to_scanline = fract(scanline_coord) - 0.5;
        
        float luma_clamp = clamp(luma_gray, 0.0, 1.0);
        float beam_focus = mix(3.5, 1.0, luma_clamp); 
        float scanline_weight = exp(-4.0 * dist_to_scanline * dist_to_scanline * beam_focus);
        float scanline_factor = mix(1.0, scanline_weight, u_scanline_strength);
        color_rgb *= scanline_factor;

        // === 8. LOTTES SUBPIXEL SHADOW MASK ===
        if (u_scanline_strength > 0.05) {
            vec3 linear_color = pow(color_rgb, vec3(2.2));
            float dark_w = mix(1.0, 0.6, u_scanline_strength);
            float light_w = mix(1.0, 1.25, u_scanline_strength);
            
            vec2 mask_pos = gl_FragCoord.xy;
            mask_pos.x += mask_pos.y * 3.0;
            float frac_x = fract(mask_pos.x * 0.166666666);
            vec3 mask = vec3(dark_w);
            if (frac_x < 0.333) {
                mask.r = light_w;
            } else if (frac_x < 0.666) {
                mask.g = light_w;
            } else {
                mask.b = light_w;
            }
            linear_color *= mask;
            color_rgb = pow(linear_color, vec3(1.0 / 2.2));
        }

        // === 9. VIGNETTE & FLICKER ===
        vec2 vig_uv = v_tex_coord * (1.0 - v_tex_coord);
        float vig = vig_uv.x * vig_uv.y * 15.0;
        vig = pow(vig, u_vignette_strength);
        color_rgb *= vig;

        float flicker = 1.0 + 0.015 * sin(time * 15.0) + 0.008 * sin(time * 41.0);
        color_rgb *= flicker;

        if (v_tex_coord.y > 0.988) {
            color_rgb *= 0.0;
        }

        gl_FragColor = vec4(clamp(color_rgb, 0.0, 1.0), 1.0);
        """)

    # ------------------------------------------------------------------------
    # 2. GLOBAL CRT OVERLAY SHADER (Scanlines + Bleed + Jitter for ALL Layers)
    # ------------------------------------------------------------------------
    renpy.register_shader("custom.vhs_crt",
        variables="""
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        uniform float u_time;
        uniform float u_chroma_amount;
        uniform float u_scanline_strength;
        uniform float u_jitter;
        uniform float u_bleed_amount;
        uniform float u_luma_bandwidth;
        uniform float u_chroma_bandwidth;
        uniform float u_decoder_type;
        varying vec2 v_tex_coord;
        """,
        fragment_functions="""
        float vhs_hash_crt(vec2 p) {
            vec3 p3 = fract(vec3(p.xyx) * 0.1031);
            p3 += dot(p3, p3.yzx + 33.33);
            return fract((p3.x + p3.y) * p3.z);
        }

        float filterChannelCRT(sampler2D tex, vec2 uv, vec3 coeffs, float filter_width, vec2 res) {
            if (filter_width <= 0.05) {
                return dot(texture2D(tex, uv).rgb, coeffs);
            }
            float accumulated_val = 0.0;
            float total_weight = 0.0;
            const int radius = 4;
            for (int i = -radius; i <= radius; i++) {
                float offset = float(i) * filter_width / res.x;
                vec3 neighbor_rgb = texture2D(tex, uv + vec2(offset, 0.0)).rgb;
                float val = dot(neighbor_rgb, coeffs);
                float weight = exp(-0.5 * float(i * i) / 4.0);
                accumulated_val += val * weight;
                total_weight += weight;
            }
            return accumulated_val / total_weight;
        }
        """,
        fragment_300="""
        vec2 uv = v_tex_coord;
        vec2 px_size = 1.0 / u_model_size;
        float time = u_time;

        // === LINE JITTER ===
        if (u_jitter > 0.001) {
            float jitter_noise = vhs_hash_crt(vec2(uv.y * 500.0, time * 2.0));
            uv.x += (jitter_noise - 0.5) * 0.0015 * u_jitter;
        }

        vec4 tex_base = texture2D(tex0, uv);

        // Alpha preservation for top/screen layers
        if (tex_base.a < 0.001) {
            gl_FragColor = vec4(0.0);
            return;
        }

        // === NTSC COMPOSITE & BLEED ===
        vec3 Y_COEFFS = vec3(0.299, 0.587, 0.114);
        vec3 I_COEFFS = vec3(0.5959, -0.2744, -0.3216);
        vec3 Q_COEFFS = vec3(0.2115, -0.5229, 0.3114);

        mat3 YIQ_TO_RGB_MATRIX = mat3(
            1.0,       1.0,       1.0,
            0.9563,   -0.2720,   -1.1063,
            0.6210,   -0.6474,    1.7046
        );

        float bleed_strength = u_bleed_amount * px_size.x * 12.0;
        vec2 uv_I = uv - vec2(0.5 * bleed_strength, 0.0);
        vec2 uv_Q = uv - vec2(1.2 * bleed_strength, 0.0);

        float chroma_bw = max(u_chroma_bandwidth, 0.1);
        float luma_bw = max(u_luma_bandwidth, 0.1);
        
        float Y_raw = filterChannelCRT(tex0, uv, Y_COEFFS, 0.0, u_model_size);
        float Y_decoded = Y_raw;
        
        if (u_decoder_type < 0.5) {
            Y_decoded = filterChannelCRT(tex0, uv, Y_COEFFS, 3.0 / luma_bw, u_model_size);
        } else {
            vec2 prev_line_uv = uv - vec2(0.0, px_size.y);
            float Y_prev = filterChannelCRT(tex0, prev_line_uv, Y_COEFFS, 0.0, u_model_size);
            Y_decoded = mix(Y_raw, (Y_raw + Y_prev) * 0.5, 0.8);
        }

        float I_val = filterChannelCRT(tex0, uv_I, I_COEFFS, 2.5 / chroma_bw, u_model_size);
        float Q_val = filterChannelCRT(tex0, uv_Q, Q_COEFFS, 7.5 / chroma_bw, u_model_size);

        vec2 px_coord = uv * u_model_size;
        float subcarrier_freq = 0.45;
        float phase_step = (px_coord.x * subcarrier_freq) + (px_coord.y * 3.141592) + (time * 29.97);

        Y_decoded += (I_val * cos(phase_step) + Q_val * sin(phase_step)) * u_chroma_amount * 0.15;

        float high_freq_luma = Y_raw - Y_decoded;
        I_val += high_freq_luma * u_chroma_amount * cos(phase_step) * 0.12;
        Q_val += high_freq_luma * u_chroma_amount * sin(phase_step) * 0.12;

        vec3 yiq = vec3(Y_decoded, I_val, Q_val);
        vec3 color_rgb = YIQ_TO_RGB_MATRIX * yiq;

        // === CHROMATIC ABERRATION ===
        vec2 chroma_offset = vec2(u_chroma_amount * 0.5, 0.2) * px_size;
        float r_val = texture2D(tex0, uv - chroma_offset).r;
        float b_val = texture2D(tex0, uv + chroma_offset).b;
        color_rgb.r = mix(color_rgb.r, r_val, 0.35);
        color_rgb.b = mix(color_rgb.b, b_val, 0.35);

        // === CRT SCANLINES ===
        float scanline_coord = v_tex_coord.y * u_model_size.y;
        float dist_to_scanline = fract(scanline_coord) - 0.5;
        float luma_gray = dot(color_rgb, vec3(0.299, 0.587, 0.114));
        float luma_clamp = clamp(luma_gray, 0.0, 1.0);
        float beam_focus = mix(3.5, 1.0, luma_clamp); 
        float scanline_weight = exp(-4.0 * dist_to_scanline * dist_to_scanline * beam_focus);
        float scanline_factor = mix(1.0, scanline_weight, u_scanline_strength);
        color_rgb *= scanline_factor;

        // === LOTTES SUBPIXEL SHADOW MASK ===
        if (u_scanline_strength > 0.05) {
            vec3 linear_color = pow(color_rgb, vec3(2.2));
            float dark_w = mix(1.0, 0.6, u_scanline_strength);
            float light_w = mix(1.0, 1.25, u_scanline_strength);
            
            vec2 mask_pos = gl_FragCoord.xy;
            mask_pos.x += mask_pos.y * 3.0;
            float frac_x = fract(mask_pos.x * 0.166666666);
            vec3 mask = vec3(dark_w);
            if (frac_x < 0.333) {
                mask.r = light_w;
            } else if (frac_x < 0.666) {
                mask.g = light_w;
            } else {
                mask.b = light_w;
            }
            linear_color *= mask;
            color_rgb = pow(linear_color, vec3(1.0 / 2.2));
        }

        gl_FragColor = vec4(clamp(color_rgb, 0.0, 1.0), tex_base.a);
        """)


## ============================================================================
## TRANSFORMS
## ============================================================================

# 1. Full Single-Pass Transform
transform vhs(
    chroma=4.0,
    scanlines=0.25,
    noise=1.0,
    wobble=1.0,
    jitter=1.0,
    slip=1.0,
    bleed=3.0,
    vignette=0.35,
    desat=0.2,
    glitch=0.05,
    mode="bg",
    warp=0.03,
    luma_bw=4.2,
    chroma_bw=1.5,
    decoder=1.0,
    glitch_size=0.05,
    glitch_stretch=0.75,
    glitch_speed=0.2,
    glitch_edge=0.5,
    glitch_delay_min=1000.0,
    glitch_delay_max=3000.0,
    roll_speed=0.0,
    noise_band_size=0.03,
    noise_band_speed=1.0,
    noise_band_edge=0.2,
    noise_band_delay_min=2000.0,
    noise_band_delay_max=5000.0,
    noise_band_intensity=0.0,
    xadj=-4,
    yadj=0
    ):
    xoffset xadj
    yoffset yadj
    mesh True
    mesh_pad (int(chroma + bleed + 2), 0, int(chroma + bleed + 2), 0)
    shader "custom.vhs"
    u_chroma_amount float(chroma)
    u_scanline_strength float(scanlines)
    u_noise_strength float(noise)
    u_wobble float(wobble)
    u_jitter float(jitter)
    u_slip float(slip)
    u_bleed_amount float(bleed)
    u_vignette_strength float(vignette)
    u_desaturation float(desat)
    u_tape_glitch float(glitch)
    u_edge_lock float(1.0 if mode == "bg" else 0.0)
    u_warp float(warp)
    u_luma_bandwidth float(luma_bw)
    u_chroma_bandwidth float(chroma_bw)
    u_decoder_type float(decoder)
    u_glitch_size float(glitch_size)
    u_glitch_stretch float(glitch_stretch)
    u_glitch_speed float(glitch_speed)
    u_glitch_edge float(glitch_edge)
    u_glitch_delay_min float(glitch_delay_min)
    u_glitch_delay_max float(glitch_delay_max)
    u_roll_speed float(roll_speed)
    u_noise_band_size float(noise_band_size)
    u_noise_band_speed float(noise_band_speed)
    u_noise_band_edge float(noise_band_edge)
    u_noise_band_delay_min float(noise_band_delay_min)
    u_noise_band_delay_max float(noise_band_delay_max)
    u_noise_band_intensity float(noise_band_intensity)
    pause 1.0 / 30.0
    repeat

# 2. Global CRT Overlay Transform (Scanlines + Bleed + Jitter for all layers)
transform vhs_crt(
    chroma=2.0,
    scanlines=1.0,
    jitter=0.3,
    bleed=0.5,
    luma_bw=4.2,
    chroma_bw=1.5,
    decoder=1.0,
    xadj=-4,
    yadj=0
    ):
    xoffset xadj
    yoffset yadj
    mesh True
    mesh_pad (int(chroma + bleed + 2), 0, int(chroma + bleed + 2), 0)
    shader "custom.vhs_crt"
    u_chroma_amount float(chroma)
    u_scanline_strength float(scanlines)
    u_jitter float(jitter)
    u_bleed_amount float(bleed)
    u_luma_bandwidth float(luma_bw)
    u_chroma_bandwidth float(chroma_bw)
    u_decoder_type float(decoder)
    pause 1.0 / 30.0
    repeat


## ============================================================================
## PRESETS
## ============================================================================

# --- Unified Single-Pass Presets ---
transform vhs_subtle:
    vhs(
        chroma=2.0,
        scanlines=1.0,
        noise=0.4,
        wobble=0.0,
        jitter=0.3,
        slip=0.0,
        bleed=0.5,
        vignette=0.25,
        desat=0.00,
        warp=0.0,
        glitch=0.0,
        glitch_size=0.0125,
        glitch_stretch=0.75,
        glitch_speed=0.40,
        glitch_edge=0.0,
        glitch_delay_min=5000.0,
        glitch_delay_max=10000.0,
        roll_speed=0.0,
        noise_band_intensity=0.0
    )

transform vhs_normal:
    vhs(
        chroma=4.0,
        scanlines=0.25,
        noise=1.0,
        wobble=0.0,
        jitter=1.0,
        slip=1.0,
        bleed=3.0,
        vignette=0.35,
        desat=0.2,
        glitch=0.05,
        warp=0.03,
        glitch_size=0.05,
        glitch_stretch=0.75,
        glitch_speed=0.2,
        glitch_edge=0.5,
        glitch_delay_min=1000.0,
        glitch_delay_max=3000.0,
        roll_speed=0.0,
        noise_band_intensity=1.0,
        noise_band_size=0.03,
        noise_band_speed=1.0,
        noise_band_edge=0.2,
        noise_band_delay_min=1000.0,
        noise_band_delay_max=4000.0
    )

# --- CRT Overlay Presets (Scanlines + Bleed + Jitter) ---
transform vhs_crt_subtle:
    vhs_crt(
        chroma=2.0,
        scanlines=1.0,
        jitter=0.3,
        bleed=0.5
    )

transform vhs_crt_normal:
    vhs_crt(
        chroma=4.0,
        scanlines=0.25,
        jitter=1.0,
        bleed=3.0
    )


## ============================================================================
## LAYER APPLICATION HELPERS & MULTI-LAYER CONTROLLERS
## ============================================================================

init python:

    def apply_vhs_global(preset="subtle"):
        """
        Apply VHS master tape distortions to 'master' layer,
        and CRT scanlines + bleed + jitter overlay to ALL layers
        (master, screens, vhs_screens, overlay, top_layers, menu_clear_layers, etc.).
        """
        master_presets = {
            "subtle": vhs_subtle,
            "normal": vhs_normal,
        }
        crt_presets = {
            "subtle": vhs_crt_subtle,
            "normal": vhs_crt_normal,
        }
        
        tr_master = master_presets.get(preset, vhs_subtle)
        tr_crt = crt_presets.get(preset, vhs_crt_subtle)
        
        # Apply full VHS to master layer
        renpy.layer_at_list([tr_master], layer="master")
        
        # Gather all configured Ren'Py layers
        all_layers = list(getattr(renpy.config, "layers", ["master", "transient", "screens", "overlay"]))
        top_layers = list(getattr(renpy.config, "top_layers", ["vhs_screens", "effect_overlay"]))
        
        combined_layers = list(dict.fromkeys(all_layers + top_layers))
        
        # Apply CRT Scanlines + Bleed + Jitter to top/screen layers
        for lyr in combined_layers:
            if lyr != "master":
                renpy.layer_at_list([tr_crt], layer=lyr)


    def remove_vhs_global():
        """
        Remove VHS shaders from all layers.
        """
        all_layers = list(getattr(renpy.config, "layers", ["master", "transient", "screens", "overlay"]))
        top_layers = list(getattr(renpy.config, "top_layers", ["vhs_screens", "effect_overlay"]))
        combined_layers = list(dict.fromkeys(all_layers + top_layers))
        
        for lyr in combined_layers:
            renpy.layer_at_list([], layer=lyr)


    def apply_vhs_to_layer(layer="master", preset="subtle", mode="full"):
        """
        Apply a VHS preset to a specific layer.
        """
        if mode == "global":
            apply_vhs_global(preset)
            return

        preset_map_full = {
            "subtle": vhs_subtle,
            "normal": vhs_normal,
        }
        preset_map_crt = {
            "subtle": vhs_crt_subtle,
            "normal": vhs_crt_normal,
        }

        if mode == "crt":
            transform_fn = preset_map_crt.get(preset, vhs_crt_subtle)
        else:
            transform_fn = preset_map_full.get(preset, vhs_subtle)

        renpy.layer_at_list([transform_fn], layer=layer)


    def remove_vhs_from_layer(layer="master"):
        """
        Remove VHS transform from a specific layer.
        """
        renpy.layer_at_list([], layer=layer)


# --- Ren'Py Script Helper Labels ---

label vhs_global_on(preset="subtle"):
    $ apply_vhs_global(preset)
    return

label vhs_global_off:
    $ remove_vhs_global()
    return

label vhs_layer_on(preset="subtle"):
    $ apply_vhs_to_layer("master", preset, mode="full")
    return

label vhs_layer_off:
    $ remove_vhs_from_layer("master")
    return