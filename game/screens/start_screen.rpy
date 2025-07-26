screen start_choose_mode():
    frame:
        background Solid ((0,0,0,255))
    vbox:
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            button:
                xsize 230
                ysize 60
                yalign 0.5
                xalign 0.5
                selected clean_mode == True
                style "hover_button"
                #at skill_hover
                action [SetVariable("clean_mode", True)]
                text "Clean Mode" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
            button:
                xsize 230
                ysize 60
                yalign 0.5
                xalign 0.5
                selected clean_mode == False
                style "hover_button"
                #at skill_hover
                action [SetVariable("clean_mode", False)]
                text "Horny mode" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
        frame:
            background None
            xsize 640
            #ysize 200
            vbox:
                frame:
                    xalign 0.5
                    background None
                    xfill True
                    ysize 125
                    if clean_mode == True:
                        text "[loc_clean_mode_desc]" style "desc_text"
                    else:
                        text "[loc_horny_mode_desc]" style "desc_text"
                frame:
                    xalign 0.5
                    background None
                    xfill True
                    text "[loc_game_mode_psa]" style "desc_text"
        button:
            xsize 230
            ysize 60
            yalign 0.5
            xalign 0.5
            style "hover_button"
            action Show( "game_confirm_box", None, Jump("daniel_apartment_label"), "This setting can be changed at any time in the menu", Fade )
            text "Confirm" xalign 0.5 yalign 0.5 style "dialogue_entry_text"