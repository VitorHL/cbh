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
style entrytext:
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_color "#000000"
    hover_outlines [(0, "#000000", 0, 0)]
    hover_size 45

style dialogue_entry_text:
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_color "#000000"
    hover_outlines [(0, "#000000", 0, 0)]

style desc_text:
    font "GFX/fonts/video_cond_light.otf"
    size 24
    justify True 
    kerning 1 
    line_spacing 2

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    #style_prefix "choice"
    frame:
        xfill True
        yfill True
        background Transform("black", alpha = 0.5)
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        for i in items:
            button:
                at dialogue_entry
                xalign 0.5
                xsize 800
                #ymaximum 40
                action i.action
                selected False
                sensitive True
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                text "[i.caption]": 
                    yalign 0.5
                    xalign 0.5 
                    style "dialogue_entry_text"
                    

################################################################################

screen travel(items):
    #style_prefix "choice"
    default thumb = "generic"
    default address = "???"
    default location = "???"
    frame:
        xfill True
        yfill True
        background Transform("black", alpha = 0.5)
    fixed:
        xsize 1280
        ysize 480
        xalign 0.5
        yalign 0.5
        fixed:
            xsize 640
            ysize 480
            hbox:
                spacing 10
                frame:
                    xsize 52
                    ysize 52
                    background Frame("gui/tiles/black_tile.webp", 3, 3)
                frame:
                    xfill True
                    background Frame("gui/tiles/black_tile.webp", 3, 3)
                    text "Travel" size 45
            vbox:
                #xalign 0.0
                yalign 0.5
                spacing 4
                for i in items:
                    $ room_thumb = i.kwargs.get("room_thumb", None)
                    $ room_address = i.kwargs.get("room_address", "???")
                    $ room_location = i.kwargs.get("room_location", "???")
                    
                    button:
                        #ymaximum 40
                        action i.action
                        hovered [SetScreenVariable("thumb", room_thumb), SetScreenVariable( "address", room_address), SetScreenVariable( "location", room_location)]
                        selected False
                        sensitive True
                        hover_sound "audio/menu_hover.wav"
                        activate_sound "audio/menu_select.wav"
                        hbox:
                            spacing 10
                            frame:
                                xpos 0
                                ypos 0
                                at travel_entry_dot
                                background Frame("gui/tiles/black_tile.webp", 3, 3)
                                hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                            frame:
                                background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                                hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                text "[i.caption]": 
                                    yalign 0.5
                                    style "entrytext"

        fixed:
            xsize 640
            ysize 480
            xalign 1.0 
            yalign 0.5
            image "thumbnail_{0}_bg".format(thumb)
            frame: 
                xalign 0.5 
                yalign 0.05 
                background Frame("gui/tiles/black_tile.webp", 3, 3)
                text "[location]": 
                    textalign 0.5 
            frame: 
                xalign 0.50 
                yalign 0.95 
                background Frame("gui/tiles/black_tile.webp", 3, 3)
                text "[address]": 
                    textalign 0.5 
                
##############################################################################################################################

screen character_interaction(character):
    vbox spacing 20:
        xalign 0.1
        yalign 0.5
        frame:
            background Transform(Frame("gui/tiles/white_tile.webp", 3, 3))
            text "[character.name!u]" size 45 xalign 0.5 yalign 0.5 color "#000000"
        vbox spacing 10:
            button:
                #xalign 0.5
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call(character.small_talk_game_label, character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                    frame xsize 320 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                        text "SMALL TALK" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                sensitive False
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                    frame xsize 320 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                        text "CONVERSATION" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                action Call("show_char_item",1, character)
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                    frame xsize 320 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                        text "SHOW ITEM" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                action Return()
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                    frame xsize 320 ysize 64:
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                        text "< GO BACK" yalign 0.5 size 45 style "dialogue_entry_text"

##############################################################################################################################

screen inventory_screen(mode=0, character=None, selected_slot = None): 
    #global game_iventory
    default slot_value = selected_slot
    frame:
        xfill True
        yfill True
        background Transform("black", alpha = 0.5)
        hbox spacing 20:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5 
            ypos 0.5    
            frame:
                xanchor 0.5
                yanchor 0.0
                #ypos 0.5
                xpos 0.5
                background None
                vbox spacing 5:
                    frame: 
                        xalign 0.5
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                        text "IVENTORY" size 45:
                            xalign 0.5
                            yalign 0.5
                    frame:
                        ysize 5
                        xsize 592
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    grid 5 4 spacing 15 xalign 0.5:
                        for slot in range(0,20):
                            fixed:
                                ysize 128
                                xsize 128
                                button:
                                    at selected_hover
                                    ysize 128
                                    xsize 128
                                    xalign 0.5
                                    yalign 0.5
                                    action SetScreenVariable( "slot_value", slot )
                                    sensitive len(game_iventory) > slot
                                    selected (slot_value == slot)
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.75)
                                    hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                    selected_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                    if len(game_iventory) > slot:
                                        image "[game_iventory[slot].icon]" xalign 0.5 yalign 0.5
                    frame:
                        ysize 5
                        xsize 592
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
            frame:
                xsize 384
                #ysize 480
                xanchor 0.5
                yanchor 0.0
                #ypos 0.5
                xpos 0.5
                background None
                vbox spacing 5:
                    frame:
                        xalign 0.5
                        #xfill True
                        if not slot_value == None:
                            text "[game_iventory[slot_value].name!u]" size 45 xalign 0.5
                        else:
                            text "SELECT ITEM" size 45 xalign 0.5
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    
                    frame:
                        xalign 0.5
                        xfill True
                        ysize 128
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3), alpha = 0.5)
                        if not slot_value == None:
                            image "[game_iventory[slot_value].icon]" xalign 0.5 yalign 0.5
                    
                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                        
                    frame:
                        xalign 0.5
                        xfill True
                        ysize 384
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                        if not slot_value == None:
                            text "[game_iventory[slot_value].desc]" style "desc_text"

                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                
                    frame:
                        xfill True
                        ysize 48
                        background None
                        hbox spacing 3:
                            align(0.5, 0.5)
                            button:
                                    xalign 0.5
                                    yalign 0.5
                                    action [ If(mode == 1, true=[Call("char_interaction",character)]), If(mode != 1, true=[Return()]) ]
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    frame:
                                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                        #at dialogue_entry
                                        
                                        text "< GO BACK" yalign 0.5 style "dialogue_entry_text"
                            button:
                                    xalign 0.5
                                    yalign 0.5
                                    if slot_value != None:
                                        action [If( mode==0 ,true=[Call(game_iventory[slot_value].game_label)]),If( mode>=1 ,true=[Call("char_item_reaction", game_iventory[slot_value], mode, character, slot_value)])]
                                    sensitive slot_value != None
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    frame:
                                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                                        hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                        #at dialogue_entry
                                        if mode == 0:
                                            text "INSPECT" yalign 0.5 style "dialogue_entry_text"
                                        if mode >= 1:
                                            text "SHOW" yalign 0.5 style "dialogue_entry_text"