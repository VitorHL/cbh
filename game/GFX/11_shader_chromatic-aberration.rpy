# ==============================================================================
# PROFESSIONAL OPTIMIZED CHROMATIC ABERRATION SHADER FOR REN'PY
# Developed by: GRIMUMU (2025)
# VRAM & QoL Optimized by: Qwen3.7 (2026)
#
# LICENSE:
# Free for use in both commercial and non-commercial projects.
# Attribution is required. Please credit "GRIMUMU" and "Qwen3.7" in your project.
#
# SUPPORT & SOCIALS:
# - Itch.io:    https://grimumu.itch.io/
# - Instagram:  https://www.instagram.com/grimumu__/
# - X/Twitter:  https://x.com/Grimumu_
# - Patreon:    https://www.patreon.com/c/Grimumu
#
# ==============================================================================
#
# VRAM OPTIMIZATION NOTES:
# - `mesh_pad` has been removed from default transforms. It forces Ren'Py to 
#   allocate larger off-screen Framebuffers (FBOs), causing VRAM spikes.
# - OpenGL's default GL_CLAMP_TO_EDGE handles edge sampling gracefully, saving 
#   massive amounts of VRAM without noticeable visual clipping.
#
# ==============================================================================

init python:
    # 1. HORIZONTAL CHROMATIC ABERRATION (Optimized Default)
    renpy.register_shader("custom.chromatic_h",
        variables="""
        uniform sampler2D tex0;
        uniform float u_amount;
        uniform vec2 u_model_size;
        varying vec2 v_tex_coord;
        """,
        fragment_300="""
        vec2 px_size = 1.0 / u_model_size;
        vec2 offset = vec2(u_amount, 0.0) * px_size;

        vec4 col_r = texture2D(tex0, v_tex_coord - offset);
        vec4 col_g = texture2D(tex0, v_tex_coord);
        vec4 col_b = texture2D(tex0, v_tex_coord + offset);

        gl_FragColor = vec4(col_r.r, col_g.g, col_b.b, col_g.a);
        """)

    # 2. VERTICAL CHROMATIC ABERRATION (QoL Addition)
    renpy.register_shader("custom.chromatic_v",
        variables="""
        uniform sampler2D tex0;
        uniform float u_amount;
        uniform vec2 u_model_size;
        varying vec2 v_tex_coord;
        """,
        fragment_300="""
        vec2 px_size = 1.0 / u_model_size;
        vec2 offset = vec2(0.0, u_amount) * px_size;

        vec4 col_r = texture2D(tex0, v_tex_coord - offset);
        vec4 col_g = texture2D(tex0, v_tex_coord);
        vec4 col_b = texture2D(tex0, v_tex_coord + offset);

        gl_FragColor = vec4(col_r.r, col_g.g, col_b.b, col_g.a);
        """)

    # 3. RADIAL CHROMATIC ABERRATION (Premium QoL Addition)
    # Creates a cinematic lens distortion effect that scales naturally from the center.
    renpy.register_shader("custom.chromatic_radial",
        variables="""
        uniform sampler2D tex0;
        uniform float u_amount;
        uniform vec2 u_model_size;
        varying vec2 v_tex_coord;
        """,
        fragment_300="""
        // Normalize coordinates to -1.0 to 1.0 range, centered at (0,0)
        vec2 center = (v_tex_coord - 0.5) * 2.0;
        
        // Calculate distance from center (0.0 at center, ~1.414 at corners)
        float dist = length(center);
        
        // Offset scales with distance for a natural lens falloff
        vec2 offset = (center * dist) * (u_amount / u_model_size);
        
        vec4 col_r = texture2D(tex0, v_tex_coord - offset);
        vec4 col_g = texture2D(tex0, v_tex_coord);
        vec4 col_b = texture2D(tex0, v_tex_coord + offset);
        
        gl_FragColor = vec4(col_r.r, col_g.g, col_b.b, col_g.a);
        """)


# ==============================================================================
# BASE TRANSFORMS (VRAM SAFE)
# ==============================================================================

transform chromatic(amount=5.0):
    mesh True
    shader "custom.chromatic_h"
    u_amount float(amount)

transform chromatic_v(amount=5.0):
    mesh True
    shader "custom.chromatic_v"
    u_amount float(amount)

transform chromatic_radial(amount=15.0):
    mesh True
    shader "custom.chromatic_radial"
    u_amount float(amount)


# ==============================================================================
# PRESETS: Horizontal Split
# ==============================================================================
transform chromatic_1:
    chromatic(amount=1.0)

transform chromatic_2:
    chromatic(amount=2.0)

transform chromatic_3:
    chromatic(amount=3.0)

transform chromatic_4:
    chromatic(amount=4.0)

transform chromatic_5:
    chromatic(amount=5.0)

transform chromatic_6:
    chromatic(amount=6.0)

transform chromatic_7:
    chromatic(amount=7.0)

transform chromatic_8:
    chromatic(amount=8.0)

transform chromatic_9:
    chromatic(amount=9.0)

transform chromatic_10:
    chromatic(amount=10.0)


# ==============================================================================
# PRESETS: Radial / Cinematic Split
# Note: Radial requires higher 'amount' values to be visible due to center falloff.
# ==============================================================================
transform chromatic_radial_1:
    chromatic_radial(amount=5.0)

transform chromatic_radial_2:
    chromatic_radial(amount=10.0)

transform chromatic_radial_3:
    chromatic_radial(amount=15.0)

transform chromatic_radial_4:
    chromatic_radial(amount=20.0)

transform chromatic_radial_5:
    chromatic_radial(amount=25.0)


# ==============================================================================
# LEGACY SUPPORT (Use only if absolutely necessary)
# WARNING: Re-enabling mesh_pad WILL increase VRAM usage for high-res sprites.
# ==============================================================================
transform chromatic_legacy_padded(amount=5.0):
    mesh True
    mesh_pad (int(amount + 2), 0, int(amount + 2), 0)
    shader "custom.chromatic_h"
    u_amount float(amount)