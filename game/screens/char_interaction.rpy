################################################################################
## Choice Talks Screen (for character conversations)
################################################################################

screen choice_talks(items, args=[character, None]):
    
    frame:
        xfill True
        yfill True
        background Transform("black", alpha=0.5)
    
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        
        # Conversation options
        for item in items:
            $ game_label = item.kwargs.get("game_label", None)
            
            button:
                #at dialogue_entry
                xalign 0.5
                xsize 800
                action Call(game_label, character)
                selected False
                sensitive True
                style "hover_button"
                
                text "[item.caption]":
                    yalign 0.5
                    xalign 0.5
                    style "dialogue_entry_text"
        
        # Back button
        button:
            #at dialogue_entry
            xalign 0.5
            xsize 800
            action Call("char_interaction", character)
            selected False
            sensitive True
            style "hover_button"
            
            text "< GO BACK":
                yalign 0.5
                xalign 0.5
                style "dialogue_entry_text"

################################################################################
## Character Interaction Screen
################################################################################

screen character_interaction(character):
    tag menu
    vbox spacing 20:
        xalign 0.1
        yalign 0.5
        
        # Character name header
        frame style "white_tile":
            xpadding 40
            text "[character.name!u]" size 45 xalign 0.5 yalign 0.5 color game_black_color font "GFX/fonts/vhs-gothic.ttf"
        
        # Interaction buttons
        vbox spacing 10:
            # Small Talk button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call(character.small_talk_game_label, character)
                hbox spacing 5:
                    frame xsize 80 ysize 80:
                        style "hover_button"
                    frame xsize 340 ysize 80:
                        style "hover_button"
                        text "SMALL TALK" yalign 0.5 size 50 style "select_button_text"
            
            # Conversation button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call("char_conversation_list", character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "CONVERSATION" yalign 0.5 size 45 style "select_button_text"
            
            # Show Item button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call("show_char_item", character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SHOW ITEM" yalign 0.5 size 45 style "select_button_text"
            
            # Go Back button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Return()
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "< GO BACK" yalign 0.5 size 45 style "select_button_text"