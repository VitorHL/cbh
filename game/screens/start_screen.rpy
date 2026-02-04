################################################################################
## Start Screens - Mode Selection and Initial Skill Allocation
################################################################################

screen start_choose_mode():
    # Prevent ESC menu during mode selection
    modal True
    key "game_menu" action NullAction()
    
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
                style "select_button"
                action [SetVariable("clean_mode", True)]
                text "CLEAN" xalign 0.5 yalign 0.5 style "select_button_text"
            button:
                xsize 230
                ysize 60
                yalign 0.5
                xalign 0.5
                selected clean_mode == False
                style "select_button"
                action [SetVariable("clean_mode", False)]
                text "EXPLICIT" xalign 0.5 yalign 0.5 style "select_button_text"
        frame:
            background None
            xsize 640
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
            action Show( "game_confirm_box", None, Jump("start_skills"), "This setting can be changed at any time in the preferences menu.", )
            text "Confirm" xalign 0.5 yalign 0.5 style "select_button_text"