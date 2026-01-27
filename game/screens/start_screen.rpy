screen start_choose_mode():
    # frame:
    #     background Transform(Solid ((0,0,0,200)))
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
                #at skill_hover
                action [SetVariable("clean_mode", True)]
                text "CLEAN" xalign 0.5 yalign 0.5 style "select_button_text"
            button:
                xsize 230
                ysize 60
                yalign 0.5
                xalign 0.5
                selected clean_mode == False
                style "select_button"
                #at skill_hover
                action [SetVariable("clean_mode", False)]
                text "EXPLICIT" xalign 0.5 yalign 0.5 style "select_button_text"
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
            action Show( "game_confirm_box", None, Jump("start_skills"), "This setting can be changed at any time in the preferences menu.", )
            text "Confirm" xalign 0.5 yalign 0.5 style "dialogue_entry_text"

screen skill_screen_start():

    default selected_skill = None
    default spent_skill_points = 0
    default selected_skill_level = None
    $ free_skill_points = att_pts_available - spent_skill_points

    # python:
    #     if selected_skill != None:
    #         for skill in game_skills:
    #             if skill == selected_skill:
    #                 renpy.set_screen_variable("selected_skill_level", skill.level )
    #                 skill_name = get_var_name(selected_skill, globals())[0]
    #                 skill_name_loc = "{0}_loc".format(var_name)
    #                 renpy.set_screen_variable( "selected_skill_loc",globals()[skill_name_loc])

    vbox xalign 0.5 yalign 0.5:
        # frame xalign 0.5:
        #     style "black_tile"
        #     ysize 50
        #     text "ATTRIBUTES" xalign 0.5 style "dialogue_entry_text"
        #text "........................................................" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
        hbox:
            spacing 20
            fixed:
                #background None
                ysize 775
                xsize 800
                vbox spacing 5:
                    hbox xalign 0.5:
                        frame:
                            style "black_tile"
                            xsize 50
                            ysize 50
                        frame:
                            style "black_tile"
                            xsize 200
                            ysize 50
                            text "ANALYTICAL" xalign 0.5 yalign 0.5 style "dialogue_entry_text" size 28
                    frame ysize 325:
                        style "border_white"
                        hbox:
                            spacing 20
                            ysize 300
                            #xalign 0.5
                            #yalign 0.5
                            for skill in game_skills[:3]:
                                button:
                                    xsize 250
                                    ysize 300
                                    #yalign 0.5
                                    #xalign 0.5
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    sensitive True
                                    selected selected_skill == skill
                                    action [SetScreenVariable("selected_skill", skill)]
                                    vbox:
                                        frame:
                                            xfill True
                                            ysize 250
                                            style "select_button_border"
                                        frame:
                                            xfill True
                                            ysize 50
                                            style "select_button"
                                            $ current_skill = skill.level + skill.invested
                                            text "[skill.GetName()!u]:[current_skill]" xalign 0.5 yalign 0.5 style "dialogue_entry_text" size 29
                    hbox xalign 0.5:
                        frame:
                            style "black_tile"
                            xsize 50
                            ysize 50
                        frame:
                            style "black_tile"
                            xsize 200
                            ysize 50
                            text "EMOTIONAL" xalign 0.5 yalign 0.5 style "dialogue_entry_text" size 28
                    
                    frame ysize 325:
                        style "border_white"
                        hbox:
                            spacing 20
                            ysize 300
                            #xalign 0.5
                            #yalign 0.5
                            for skill in game_skills[3:]:
                                button:
                                    xsize 250
                                    ysize 300
                                    #yalign 0.5
                                    #xalign 0.5
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    sensitive True
                                    selected selected_skill == skill
                                    action [SetScreenVariable("selected_skill", skill)]
                                    vbox:
                                        frame:
                                            xfill True
                                            ysize 250
                                            style "select_button_border"
                                        frame:
                                            xfill True
                                            ysize 50
                                            style "select_button"
                                            $ current_skill = skill.level + skill.invested
                                            text "[skill.GetName()!u]:[current_skill]" xalign 0.5 yalign 0.5 style "dialogue_entry_text" size 29
            vbox:
                xsize 384
                frame:
                    style "black_tile_75"
                    xfill True
                    #ysize 720
                    xalign 0.5
                    vbox xalign 0.5 yalign 0.5:
                        text "-------------------" style "dialogue_entry_text" xalign 0.5
                        frame:
                            background None
                            xfill True
                            ysize 35
                            text "ATTRIBUTE POINTS: [att_pts_available]" xalign 0.5 yalign 0.5 style "dialogue_entry_text" size 28
                        text "-------------------" style "dialogue_entry_text" xalign 0.5
                frame:
                        style "black_tile_75"
                        xfill True
                        ysize 192
                hbox:
                    button:
                        xsize 50
                        ysize 50
                        style "hover_button"
                        text "-" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
                        sensitive selected_skill != None and selected_skill.invested > 0
                        action [ Function(add_skill_point, selected_skill, -1) ]
                    frame:
                        xsize 284
                        ysize 50
                        style "black_tile"
                        if selected_skill != None:
                            $ selected_skill_current = selected_skill.level + selected_skill.invested
                            text "[selected_skill.GetName()!u]:[selected_skill_current]" style "dialogue_entry_text" size 38 xalign 0.5
                    button:
                        xsize 50
                        ysize 50
                        style "hover_button"
                        text "+" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
                        sensitive selected_skill != None and att_pts_available > 0 and selected_skill.current < att_pts_max_start
                        action [ Function(add_skill_point, selected_skill, 1) ]
                frame:
                    style "black_tile_75"
                    xfill True
                    ysize 375
                    vbox:
                        text "-------------------" style "dialogue_entry_text" xalign 0.5
                        #background None
                        #spacing 5
                        xsize 370
                        xalign 0.5
                        if selected_skill != None:
                            frame:
                                xfill True
                                background None
                                ysize 100
                                text "[selected_skill.GetQuote()]" style "desc_text" textalign 0.5 xalign 0.5 yalign 0.5 size 20
                            frame:
                                xfill True
                                background None
                                text "[selected_skill.GetDesc()]" style "desc_text" xalign 0.5
                hbox:
                    button:
                        xsize 192
                        ysize 50
                        style "hover_button"
                        sensitive att_pts_spent > 0
                        action [ Function(reset_skill_points) ]
                        text "RESET" xalign 0.5 yalign 0.5 style "dialogue_entry_text"
                    button:
                        xsize 192
                        ysize 50
                        style "hover_button"
                        sensitive att_pts_available == 0 and att_pts_spent > 0
                        action Show( "game_confirm_box", None, [Function(apply_skill_points), Jump("start_test_scenario")], "This cannot be changed later", Fade )
                        text "CONFIRM" xalign 0.5 yalign 0.5 style "dialogue_entry_text"