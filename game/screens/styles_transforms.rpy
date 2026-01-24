
init offset = -10

# Define common colors used throughout the UI
define game_white_color = "#c8c8c8"
define game_white_selected = "#ffffff"
define game_white_unhovered = "#afafaf"
define game_white_inactive = "#4b4b4b"
define game_dark_red_color = "#c73232"
define game_black_color = "#191919"
define game_orange_color = "#c74e32"
define game_yellow_color = "#c79532"
define game_cyan_color = "#c7b695"
define game_green_color = "#63c763"

# Define recolorable base frames
init python:
    def layered_frame(**kwargs):
        """
        Creates a layered frame with separate base and border colors.
        
        Keyword Args:
            base_color (str): Hex color for the background layer (default: "#000000")
            border_color (str): Hex color for the border layer (default: "#FFFFFF")
            base_alpha (float): Opacity of base layer, 0.0 to 1.0 (default: 1.0)
            border_alpha (float): Opacity of border layer, 0.0 to 1.0 (default: 1.0)
            base_image (str): Path to base tile image (default: "gui/tiles/base_tile.webp")
            border_image (str): Path to border tile image (default: "gui/tiles/border_tile.webp")
            borders (tuple): Frame borders for tiling (default: (20, 20))
        """
        base_color = kwargs.get('base_color', "#FFFFFF")
        border_color = kwargs.get('border_color', game_white_color)
        base_alpha = kwargs.get('base_alpha', 1.0)
        border_alpha = kwargs.get('border_alpha', 1.0)
        base_image = kwargs.get('base_image', "gui/tiles/black_tile.webp")
        border_image = kwargs.get('border_image', "gui/tiles/tile_border.webp")
        borders = kwargs.get('borders', (20, 20))
        
        # Create the base layer
        base_layer = Transform(
            Frame(base_image, *borders),
            matrixcolor=TintMatrix(base_color),
            alpha=base_alpha
        )
        
        # Create the border layer
        border_layer = Transform(
            Frame(border_image, *borders),
            matrixcolor=TintMatrix(border_color),
            alpha=border_alpha
        )
        
        # Use Fixed to layer them properly
        return Fixed(
            base_layer,
            border_layer,
            fit_first=True
        )



# Screen Transforms -------------------------------------------------------

transform travel_entry_dot:
    on idle:   
        xsize 42
        ysize 42
    on hover:
        xsize 52
        ysize 52
        
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

style header_text:
    color "#ffffff"
    size 40

style entrytext:
    color "#ffffff"
    outlines [(1, game_black_color, 0, 0)]
    hover_color game_black_color
    hover_outlines [(0, game_black_color, 0, 0)]
    selected_color game_black_color
    selected_outlines [(0, game_black_color, 0, 0)]
    hover_size 45

style dialogue_entry_text:
    color game_white_color
    outlines [(1, "#000000", 0, 0)]
    hover_color game_white_selected
    insensitive_color game_white_inactive
    adjust_spacing False
    size 20
    font "GFX/fonts/vhs-gothic.ttf"

style dialogue_entry_important_text:
    color game_cyan_color
    outlines [(1, "#000000", 0, 0)]
    hover_color game_cyan_color
    insensitive_color game_cyan_color
    adjust_spacing False
    size 20
    font "GFX/fonts/vhs-gothic.ttf"

style check_skill_text:
    color game_white_color
    outlines [(1, "#000000", 0, 0)]
    hover_color game_white_selected
    insensitive_color game_dark_red_color

style select_button_text:
    color game_white_unhovered
    outlines [(1, game_black_color, 0, 0)]
    hover_color game_white_color
    #hover_outlines [(0, game_black_color, 0, 0)]
    selected_color game_black_color
    selected_outlines [(0, game_black_color, 0, 0)]
    insensitive_color game_white_inactive

style yellow_text:
    color game_yellow_color 
    outlines [(1, game_black_color, 0, 0)]

style orange_text:
    color game_orange_color 
    outlines [(1, game_black_color, 0, 0)]

style green_text:
    color game_green_color 
    outlines [(1, game_black_color, 0, 0)]

style hover_button_text:
    color game_white_color
    outlines [(1, game_black_color, 0, 0)]
    hover_color game_white_selected
    insensitive_color game_white_inactive

style desc_text:
    font "GFX/fonts/video_cond_light.otf"
    size 24
    justify True 
    kerning 1 
    line_spacing 2

style title_text:
    size 50
    color "#ffffff"
    outlines [(2, game_black_color, 0, 0)]

style vhs_gothic:
    adjust_spacing False
    size 24
    color game_white_color
    outlines [(1, game_black_color, 0, 0)]
    font "GFX/fonts/vhs-gothic.ttf"
    bold False

# Button Styles -------------------------------------------------------

style hover_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_unhovered, base_alpha=0.5)
    hover_background layered_frame(border_image = "gui/tiles/tile_bracket.webp",border_color=game_white_color, base_alpha=0.75)
    insensitive_background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_inactive, base_alpha=0.5)
    xpadding 20
    ypadding 10

style choice_menu_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_unhovered, base_alpha=0.5)
    hover_background layered_frame(border_image = "gui/tiles/tile_bracket.webp",border_color=game_white_color, base_alpha=0.75)
    insensitive_background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_inactive, base_alpha=0.5)
    xpadding 20
    ypadding 10

style important_choice_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_unhovered, base_alpha=0.5)
    hover_background layered_frame(border_image = "gui/tiles/tile_bracket.webp",border_color=game_white_color, base_alpha=0.75)
    insensitive_background layered_frame(border_image = "gui/tiles/tile_bracket.webp", border_color=game_white_inactive, base_alpha=0.5)
    xpadding 20
    ypadding 10

style skill_check_border:
    background layered_frame(border_color=game_white_unhovered, base_alpha=0.0)
    hover_background layered_frame(border_color=game_white_color, base_alpha=0.0)
    insensitive_background layered_frame(border_color=game_dark_red_color, base_alpha=0.0)
    xpadding 13
    ypadding 13

transform select_image:
    on idle:
        matrixcolor TintMatrix(game_white_unhovered)
    on hover:
        matrixcolor TintMatrix(game_white_color)    
    on selected_idle, selected_hover:
        matrixcolor TintMatrix(game_black_color)

style select_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background layered_frame(border_color=game_white_unhovered, base_alpha=0.5)
    hover_background layered_frame(border_color=game_white_color, base_alpha=0.75)
    selected_background layered_frame(border_color=game_black_color, border_image ="gui/tiles/tile_border_thin.webp", base_image="gui/tiles/white_tile.webp", base_alpha=0.9)
    # xpadding 15
    # ypadding 15
style select_button_border:
    background Frame("gui/tiles/black_tile_border.webp", 20, 20,)
    hover_background Frame("gui/tiles/black_tile_border_dark.webp", 20, 20)
    selected_background Frame("gui/tiles/white_tile_border.webp", 20, 20)
    # xpadding 15
    # ypadding 15
style select_border:
    background layered_frame(border_color=game_white_unhovered, base_alpha=0.0)
    hover_background layered_frame(border_color=game_white_color, base_alpha=0.0)
    insensitive_background layered_frame(border_color=game_white_inactive, base_alpha=0.0)
    selected_background Frame("gui/tiles/white_tile_border.webp", 20, 20)
    ypadding 10
    xpadding 20

# Screen Styles -------------------------------------------------------

style black_tile:
    background Frame("gui/tiles/black_tile.webp", 20, 20,)
    xpadding 10
    ypadding 10

style black_tile_hollow:
    background Frame("gui/tiles/black_tile_hollow.webp", 20, 20,)
    xpadding 10
    ypadding 10

style black_tile_border:
    background layered_frame()
    xpadding 20
    ypadding 10

style skill_tile:
    background layered_frame(base_alpha = 0, border_color=game_yellow_color)
    xpadding 20
    ypadding 15

style black_tile_underline:
    background layered_frame(border_image = "gui/tiles/tile_underline.webp")
    xpadding 10
    ypadding 10

style black_tile_75:
    background Frame("gui/tiles/black_tile_75.webp", 20, 20,)
    xpadding 10
    ypadding 10

style black_tile_50:
    background Frame("gui/tiles/black_tile_50.webp", 20, 20,)
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

