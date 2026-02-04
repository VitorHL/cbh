################################################################################
## Inventory Screen
################################################################################

screen inventory_screen(character=None, **kwargs):
    tag menu
    #default character = kwargs.get("character", None)
    default screen_mode = kwargs.get("screen_mode","default")
    default slot_value = kwargs.get( "selected_item", None)

    if screen_mode == "default":
        
        use game_menu(_("inventory"), scroll=None, content_yalign=0.0)
    
    if screen_mode != "default":
        #Dark background
        frame xfill True yfill True background Transform("black", alpha=0.7)
    fixed yalign 0.5:
        if screen_mode != "default":
            xalign 0.5 
        else:
            xalign 0.6
        ysize 784
        xsize 1154
        vbox:
            hbox:
                spacing 10
                frame background None xpadding 0 ypadding 0:
                    xsize 760
                    vbox:
                        hbox:
                            frame:
                                style "black_tile_border"
                                xsize 60
                                ysize 60
                            frame:
                                style "black_tile_underline"
                                xfill True
                                ysize 60
                                text "ITEM" style "title_text" yalign 0.25
                        frame style "black_tile_hollow" ysize 330 xfill True:
                            frame background None ypadding 0 xpadding 0 ypos 10 xalign 0.5:
                                vbox:
                                    if slot_value is not None:
                                        text "[game_iventory[slot_value].name!u]" style "title_text"
                                    else:
                                        text "SELECT ITEM" style "title_text"
                                    text "----------------------------------" style "title_text"
                                    hbox:
                                        spacing 20
                                        frame style "border_white" xsize 220 ysize 220
                                        fixed xsize 470:
                                            vbox:
                                                spacing 10
                                                text "DESCRIPTION:" style "desc_text" color game_cyan_color size 16
                                                if slot_value is not None:
                                                    text "[game_iventory[slot_value].desc]" style "desc_text"
                                                else:
                                                    text "???" style "desc_text"
                            
                                
                    
                vbox:
                    xsize 384
                    hbox:
                        frame:
                            style "black_tile"
                            xsize 60
                            ysize 60
                            text "*" xalign 0.5
                        frame:
                            style "black_tile"
                            xsize 264
                            ysize 60
                            text "ACTIONS" xalign 0.5 style "title_text" yalign 0.25
                        frame:
                            style "black_tile"
                            xsize 60
                            ysize 60
                            text "*" xalign 0.5
                    frame style "black_tile_hollow_transparent":
                        ysize 330
                        # Action buttons
                        vbox:
                            button xfill True ysize 50 style "hover_button":
                                    sensitive slot_value is not None and screen_mode == "default"
                                    #if slot_value is not None:
                                    #    action Call("char_item_reaction", game_iventory[slot_value], mode, character, slot_value)
                                    text "INSPECT ITEM" xalign 0.5 yalign 0.5 style "select_button_text"

                            button xfill True ysize 50 style "hover_button":
                                    sensitive slot_value is not None and screen_mode != "default"
                                    if slot_value is not None and screen_mode != "default":
                                        action Call("char_item_reaction", game_iventory[slot_value], character, slot_value)
                                    text "SHOW ITEM" xalign 0.5 yalign 0.5 style "select_button_text"

                            button xfill True ysize 50 style "hover_button":
                                    sensitive screen_mode == "show_item"
                                    action Call("char_interaction", character)
                                    text "< GO BACK" xalign 0.5 yalign 0.5 style "select_button_text"
                    
            vbox:
                hbox:
                    frame:
                        style "black_tile_border"
                        xsize 60
                        ysize 60
                    frame:
                        style "black_tile_underline"
                        xfill True
                        ysize 60
                        text "IVENTORY" style "title_text" yalign 0.25
                frame style "black_tile_hollow_transparent" xfill True yfill True:
                    grid 8 2 spacing 10 xalign 0.5 yalign 0.5:
                        for slot in range(16):
                            fixed:
                                ysize 128
                                xsize 128
                                
                                button:
                                    at selected_hover
                                    ysize 128
                                    xsize 128
                                    xalign 0.5
                                    yalign 0.5
                                    action SetScreenVariable("slot_value", slot)
                                    sensitive len(game_iventory) > slot
                                    selected (slot_value == slot)
                                    style "hover_button"
                                    
                                    if len(game_iventory) > slot:
                                        image "[game_iventory[slot].icon]" xalign 0.5 yalign 0.5
                    