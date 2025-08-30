# Screen Transforms -------------------------------------------------------

transform travel_entry_dot:
    on idle:   
        xsize 42
        ysize 42
    on hover:
        xsize 52
        ysize 52
        
transform dialogue_entry:
    on idle:
        zoom 0.75
    on hover:
        zoom 1.0
    on selected_idle:
        zoom 1.0
transform selected_hover:
    on idle:
        zoom 0.75
    on selected_idle:
        zoom 1.0
    on selected_hover:
        zoom 1.0
    on insensitive: 
        zoom 0.75

# Text Styles -------------------------------------------------------

style entrytext:
    color "#ffffff"
    outlines [(1, "#191919", 0, 0)]
    hover_color "#191919"
    hover_outlines [(0, "#191919", 0, 0)]
    selected_color "#191919"
    selected_outlines [(0, "#191919", 0, 0)]
    hover_size 45

style dialogue_entry_text:
    color "#ffffff"
    outlines [(1, "#191919", 0, 0)]
    hover_color "#ffffff"
    #hover_outlines [(0, "#191919", 0, 0)]
    selected_color "#191919"
    selected_outlines [(0, "#191919", 0, 0)]

style select_button_text:
    color "#ffffff"
    outlines [(1, "#191919", 0, 0)]
    hover_color "#ffffff"
    #hover_outlines [(0, "#191919", 0, 0)]
    selected_color "#191919"
    selected_outlines [(0, "#191919", 0, 0)]

style hover_button_text:
    color "#ffffff"
    outlines [(1, "#191919", 0, 0)]
    hover_color "#ffffff"

style desc_text:
    font "GFX/fonts/video_cond_light.otf"
    size 24
    justify True 
    kerning 1 
    line_spacing 2

style title_text:
    size 50
    color "#ffffff"
    outlines [(2, "#191919", 0, 0)]

# Button Styles -------------------------------------------------------

style hover_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background Frame("gui/tiles/black_tile_bracket.webp", 20, 20,)
    hover_background Frame("gui/tiles/black_tile_bracket_dark.webp", 20, 20)
    # xpadding 15
    # ypadding 15

style select_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background Frame("gui/tiles/black_tile_bracket.webp", 20, 20,)
    hover_background Frame("gui/tiles/black_tile_bracket_dark.webp", 20, 20)
    selected_background Frame("gui/tiles/white_tile_bracket.webp", 20, 20)
    # xpadding 15
    # ypadding 15
style select_button_border:
    background Frame("gui/tiles/black_tile_border.webp", 20, 20,)
    hover_background Frame("gui/tiles/black_tile_border_dark.webp", 20, 20)
    selected_background Frame("gui/tiles/white_tile_border.webp", 20, 20)
    # xpadding 15
    # ypadding 15

# Screen Styles -------------------------------------------------------

style black_tile:
    background Frame("gui/tiles/black_tile.webp", 20, 20,)
    xpadding 10
    ypadding 10
style black_tile_75:
    background Frame("gui/tiles/black_tile_75.webp", 20, 20,)
    xpadding 10
    ypadding 10

style black_tile_border_75:
    background Frame("gui/tiles/black_tile_border_75.webp", 20, 20,)
    xpadding 10
    ypadding 10

style border_white:
    background Frame("gui/tiles/border_white.webp", 7, 7)
    xpadding 10
    ypadding 10

