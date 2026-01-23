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
            $ skill_roll = i.kwargs.get("skill_roll", [])
            $ skill_check = i.kwargs.get("skill_check", [])
            button:
                #at dialogue_entry
                xalign 0.5
                xsize 800
                #ymaximum 40
                if skill_roll != []:
                    if len(skill_roll) > 2:
                        action [ Function(game_skill_roll, skill_roll[0], skill_roll[1], skill_roll[2]), i.action ]
                    else:
                        action [ Function(game_skill_roll, skill_roll[0], skill_roll[1]), i.action ]
                else:
                    action i.action
                selected False
                sensitive True
                style "hover_button"
                vbox:
                    frame:
                        xfill True
                        background None
                        text "> [i.caption]" yalign 0.5 style "dialogue_entry_text"
                    #if skill_roll != [] or skill_check != []:
                    #    text "-------------------------" yalign 0.5 xalign 0.5 style "dialogue_entry_text" size 14
                    if skill_roll != []:
                        text "-SKILL ROLL-" yalign 0.5 xalign 0.5 style "dialogue_entry_text" size 12
                        if len(skill_roll) > 2:
                            default columns = 2
                            default buffs_for_this_check = []
                            for i in skill_roll[2]:
                                python:
                                    if i in available_skill_buffs:
                                        buffs_for_this_check.append(i)
                            vbox:
                                xalign 0.5
                                spacing 5
                                for i in chunk(buffs_for_this_check, columns):
                                    hbox:
                                        spacing 40
                                        align (0.5, 0.5)
                                        yalign 0.5
                                        for buff in i:
                                            if buff.value >= 0:
                                                text "[buff.GetName()]: +[buff.value]" yalign 0.5 xalign 0.5 style "dialogue_entry_text" color "#0adc28" size 14
                                            else:
                                                text "[buff.GetName()]: -[buff.value]" yalign 0.5 xalign 0.5 style "dialogue_entry_text" color "#dc2020" size 14
                            
                        if len(skill_roll) > 2:
                            text "> [skill_roll[0].GetName()!u]:[rollchance(skill_roll[0], skill_roll[1], skill_roll[2])!u]% <" yalign 0.5 xalign 0.5 style "hover_button_text" size 16
                        else:
                            text "> [skill_roll[0].GetName()!u]:[rollchance(skill_roll[0], skill_roll[1])!u]% <" yalign 0.5 xalign 0.5 style "hover_button_text" size 16
                    if skill_check != []:
                        text "-SKILL CHECK-" yalign 0.5 xalign 0.5 style "dialogue_entry_text" size 12
                        text "> [skill_check[0].GetName()!u]:[skill_check[0].level]/[skill_check[1]] <" yalign 0.5 xalign 0.5 style "hover_button_text" size 16
                    
################################################################################

screen choice_talks(items, args=[character,None]):
    frame:
        xfill True
        yfill True
        background Transform("black", alpha = 0.5)
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        for i in items:
            $ game_label = i.kwargs.get("game_label", None)
            #$ character = i.kwargs.get("character", None)
            button:
                at dialogue_entry
                xalign 0.5
                xsize 800
                #ymaximum 40
                action Call(game_label,character)
                selected False
                sensitive True
                style "hover_button"
                text "[i.caption]": 
                    yalign 0.5
                    xalign 0.5 
                    style "dialogue_entry_text"
        button:
                at dialogue_entry
                xalign 0.5
                xsize 800
                #ymaximum 40
                action Call("char_interaction", character)
                selected False
                sensitive True
                style "hover_button"
                text "< GO BACK": 
                    yalign 0.5
                    xalign 0.5 
                    style "dialogue_entry_text"

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
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SMALL TALK" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                action Call("char_conversation_list", character)
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "CONVERSATION" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                action Call("show_char_item",1, character)
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SHOW ITEM" yalign 0.5 size 45 style "dialogue_entry_text"
            button:
                #xalign 0.5
                yalign 0.5
                action Return()
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
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
                                    style "hover_button"
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
                                        style "hover_button"
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
                                        style "hover_button"
                                        #at dialogue_entry
                                        if mode == 0:
                                            text "INSPECT" yalign 0.5 style "dialogue_entry_text"
                                        if mode >= 1:
                                            text "SHOW" yalign 0.5 style "dialogue_entry_text"