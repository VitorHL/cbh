## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
        hbox:
            spacing 5

            xalign 1.0
            ypos 24

            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_history.webp"
                hover "gui/dialogue_history_hover.webp"
            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_auto.webp"
                hover "gui/dialogue_auto_hover.webp"
            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_skip.webp"
                hover "gui/dialogue_skip_hover.webp"
            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_quick_save.webp"
                hover "gui/dialogue_quick_save_hover.webp"
            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_quick_load.webp"
                hover "gui/dialogue_quick_load_hover.webp"
            imagebutton style "qm_button" action ShowMenu('preferences'):
                idle "gui/dialogue_preferences_idle.webp"
                hover "gui/dialogue_preferences_hover.webp"
        frame:
            style "say_frame"
            text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xsize 1000
    #background Frame("gui/tiles/black_tile_50.webp", 20, 20,)
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    #background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    #xpos gui.name_xpos
    background Frame("gui/tiles/black_tile_50.webp", 20, 20,)
    xpadding 25
    ypadding 10

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    ypos -1
    outlines [(2, "#000000", 1, 1)]

style say_frame:
    background Frame("gui/tiles/black_tile_border.webp", 20, 20,)
    xpadding 25
    ypadding 25
    ypos 70
    xfill True
    ysize 185

style say_dialogue:
    properties gui.text_properties("dialogue")
    #xpos gui.dialogue_xpos
    #xsize gui.dialogue_width
    #ypos gui.dialogue_ypos
    adjust_spacing False
    size 30
    color "#c8c8c8"
    outlines [(2, "#000000", 1, 1)]
    font "GFX/fonts/vhs-gothic.ttf"
    bold False

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

# screen quick_menu():

#     ## Ensure this appears on top of other screens.
#     zorder 100

#     if quick_menu:

#         hbox:
#             style_prefix "quick"

#             xalign 0.5
#             yalign 1.0

#             imagebutton style "qm_button" action ShowMenu('preferences'):
#                 idle "gui/dialogue_auto.webp"
#                 hover "gui/dialogue_auto_hover.webp"
#             imagebutton style "qm_button" action ShowMenu('preferences'):
#                 idle "gui/dialogue_skip.webp"
#                 hover "gui/dialogue_skip_hover.webp"
#             imagebutton style "qm_button" action ShowMenu('preferences'):
#                 idle "gui/dialogue_quick_save.webp"
#                 hover "gui/dialogue_quick_save_hover.webp"
#             imagebutton style "qm_button" action ShowMenu('preferences'):
#                 idle "gui/dialogue_quick_load.webp"
#                 hover "gui/dialogue_quick_load_hover.webp"
#             imagebutton style "qm_button" action ShowMenu('preferences'):
#                 idle "gui/dialogue_preferences_idle.webp"
#                 hover "gui/dialogue_preferences_hover.webp"
#                 #image  "gui/dialogue_preferences_idle.webp" xalign 0.5 yalign 0.5#:
#                     #hover "gui/dialogue_preferences_hovered.webp"
#             # textbutton _("Back") action Rollback()
#             # textbutton _("History") action ShowMenu('history')
#             # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#             # textbutton _("Auto") action Preference("auto-forward", "toggle")
#             # textbutton _("Save") action ShowMenu('save')
#             # textbutton _("Q.Save") action QuickSave()
#             # textbutton _("Q.Load") action QuickLoad()
#             # textbutton _("Prefs") action ShowMenu('preferences')

style qm_button:
    hover_sound "audio/menu_hover.wav"
    activate_sound "audio/menu_select.wav"
    background Frame("gui/tiles/black_tile_50.webp", 20, 20,)
    hover_background Frame("gui/tiles/black_tile_selected.webp", 20, 20) # hover_background Frame(Fixed(Frame("gui/tiles/black_tile_50.webp", 20, 20,),Transform("gui/dialogue_preferences_hover.webp", align=(0.5, 0.5))))
    xsize 40
    ysize 40
    xalign 0.5
    yalign 0.5

# ## This code ensures that the quick_menu screen is displayed in-game, whenever
# ## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")

# default quick_menu = True

# style quick_button is default
# style quick_button_text is button_text

# style quick_button:
#     properties gui.button_properties("quick_button")

# style quick_button_text:
#     properties gui.button_text_properties("quick_button")