#############################
# Level Header
#############################
screen level_header():
    fixed xalign 0.5 ypos 35:
        xsize 760
        ysize 110
        hbox:
            spacing 10
            frame xsize 110 ysize 110:
                style "black_tile_border"
                vbox xalign 0.5 yalign 0.5:
                    text "LEVEL" xalign 0.5 style "title_text" size 20 color game_yellow_color
                    text "{:02d}".format(player_level) xalign 0.5  style "title_text" size 50 color game_cyan_color
            frame:
                yalign 0.5
                xfill True
                background None
                vbox:
                    xalign 0.5
                    frame:
                        xalign 0.5
                        style "black_tile_75"
                        ypadding 0
                        vbox:
                            xalign 0.5
                            spacing -5
                            text "--------------" style "title_text" xalign 0.5 size 24
                            hbox:
                                xalign 0.5
                                text "XP:"style "title_text" xalign 0.5 size 18 font "GFX/fonts/vhs-gothic.ttf"
                                text "[player_xp]" style "title_text" xalign 0.5 font "GFX/fonts/vhs-gothic.ttf" size 18:
                                    if player_xp >= 10:
                                        color game_green_light_color
                                text "/[xp_progression[player_level + 1]]"  style "title_text" xalign 0.5 font "GFX/fonts/vhs-gothic.ttf" size 18
                            text "--------------" style "title_text" xalign 0.5 size 24
                    frame:
                        style "black_tile"
                        xalign 0.5
                        xfill True
                        hbox:
                            xalign 0.5
                            spacing 10
                            text "{:02d}%".format(int((player_xp / xp_progression[player_level + 1]) * 100)) size 20 style "title_text"
                            bar value player_xp range xp_progression[player_level + 1] xsize 550 ysize 10 yalign 0.5:
                                left_bar Solid(game_yellow_color)    # Filled portion (green)
                                right_bar Solid(game_black_color)   # Empty portion (dark)

################################################################################
## Skills Screen for Pause Menu (uses game_menu wrapper)
################################################################################

screen skills(starting_game=False):
    tag menu
    

    if starting_game == False:
        use game_menu(_("skills"), scroll=None, content_yalign=0.0)
        use level_header()
    else:
        key "game_menu" action NullAction()

    default selected_skill = None
    default spent_skill_points = 0
    default selected_skill_level = None
    $ free_skill_points = att_pts_available - spent_skill_points

    vbox yalign 0.5:
        if starting_game == True:
            xalign 0.5 
        else:
            xalign 0.6
        hbox:
            spacing 10
            fixed:
                ysize 775
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
                            text "ANALYTICAL" style "title_text" yalign 0.25
                    frame ysize 332:
                        style "black_tile_hollow_transparent"
                        hbox:
                            spacing -5
                            for skill in game_skills[:3]:
                                button:
                                    xsize 250
                                    ysize 300
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    sensitive True
                                    selected selected_skill == skill
                                    action [SetScreenVariable("selected_skill", skill)]
                                    vbox:
                                        frame:
                                            xsize 238
                                            ysize 250
                                            style "select_button_border"
                                            if renpy.loadable("gui/attributes/{}_icon.webp".format(get_var_name(skill,globals())[0])) and selected_skill != skill:
                                                image "gui/attributes/{}_icon.webp".format(get_var_name(skill,globals())[0]) xalign 0.5 yalign 0.5 at select_image
                                            if renpy.loadable("gui/attributes/{}_icon_selected.webp".format(get_var_name(skill,globals())[0])) and selected_skill == skill:
                                                image "gui/attributes/{}_icon_selected.webp".format(get_var_name(skill,globals())[0]) xalign 0.5 yalign 0.5
                                        frame:
                                            xfill True
                                            ysize 50
                                            style "select_button"
                                            $ current_skill = skill.level + skill.invested
                                            text "[skill.GetName()!u]:[current_skill]" xalign 0.5 style "select_button_text" size 29 ypos 17
                    hbox:
                        frame:
                            style "black_tile_border"
                            xsize 60
                            ysize 60
                        frame:
                            style "black_tile_underline"
                            xfill True
                            ysize 60
                            text "EMOTIONAL" style "title_text" yalign 0.25
                    frame ysize 332:
                        style "black_tile_hollow_transparent"
                        hbox:
                            spacing -5
                            for skill in game_skills[3:]:
                                button:
                                    xsize 250
                                    ysize 300
                                    hover_sound "audio/menu_hover.wav"
                                    activate_sound "audio/menu_select.wav"
                                    sensitive True
                                    selected selected_skill == skill
                                    action [SetScreenVariable("selected_skill", skill)]
                                    vbox:
                                        frame:
                                            xsize 238
                                            ysize 250
                                            style "select_button_border"
                                            if renpy.loadable("gui/attributes/{}_icon.webp".format(get_var_name(skill,globals())[0])) and selected_skill != skill:
                                                image "gui/attributes/{}_icon.webp".format(get_var_name(skill,globals())[0]) xalign 0.5 yalign 0.5 at select_image
                                            if renpy.loadable("gui/attributes/{}_icon_selected.webp".format(get_var_name(skill,globals())[0])) and selected_skill == skill:
                                                image "gui/attributes/{}_icon_selected.webp".format(get_var_name(skill,globals())[0]) xalign 0.5 yalign 0.5
                                        frame:
                                            xfill True
                                            ysize 50
                                            style "select_button"
                                            $ current_skill = skill.level + skill.invested
                                            text "[skill.GetName()!u]:[current_skill]" xalign 0.5 style "select_button_text" size 29 ypos 17
        
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
                        text "ATTRIBUTES" xalign 0.5 style "title_text" yalign 0.25
                    frame:
                        style "black_tile"
                        xsize 60
                        ysize 60
                        text "*" xalign 0.5
                frame:
                    style "black_tile_75"
                    xfill True
                    vbox xalign 0.5 yalign 0.5:
                        text "-----------------" style "title_text" xalign 0.5
                        frame:
                            background None
                            xfill True
                            ysize 35
                            hbox:
                                xalign 0.5
                                text "ATTRIBUTE POINTS:" xalign 0.5 yalign 0.5 style "title_text" size 30
                                text "{:02d}".format(att_pts_available) xalign 0.5 yalign 0.5 style "title_text" size 30:
                                    if free_skill_points > 0:
                                        color game_yellow_color
                                    else:
                                        color game_white_inactive
                                
                        text "-----------------" style "title_text" xalign 0.5
                hbox:
                    button:
                        xsize 50
                        ysize 50
                        style "hover_button"
                        text "-" xalign 0.5 yalign 0.5 style "select_button_text"
                        sensitive selected_skill != None and selected_skill.invested > 0
                        action [ Function(add_skill_point, selected_skill, -1) ]
                    frame:
                        xsize 284
                        ysize 50
                        style "black_tile"
                        if selected_skill != None:
                            $ selected_skill_current = selected_skill.level + selected_skill.invested
                            text "[selected_skill.GetName()!u]:[selected_skill_current]" style "title_text" size 38 xalign 0.5 yalign 0.5
                    button:
                        xsize 50
                        ysize 50
                        style "hover_button"
                        text "+" xalign 0.5 yalign 0.5 style "select_button_text"
                        if starting_game == True:
                            sensitive selected_skill != None and att_pts_available > 0 and selected_skill.current < att_pts_max_start
                        else:
                            sensitive selected_skill != None and att_pts_available > 0 and selected_skill.current < att_pts_max
                        action [ Function(add_skill_point, selected_skill, 1) ]
                frame:
                    style "black_tile_75"
                    xfill True
                    ysize 503
                    vbox:
                        text "-----------------" style "title_text" xalign 0.5
                        xalign 0.5
                        fixed:
                            xfill True
                            yfill True
                            vbox:
                                if selected_skill != None:
                                    frame:
                                        xfill True
                                        background None
                                        ysize 75
                                        vbox:
                                            xalign 0.5
                                            spacing 10
                                            text "[selected_skill.GetQuote()]" style "desc_text" textalign 0.5 xalign 0.5 yalign 0.5 size 12 color game_yellow_color
                                            text "- [selected_skill.GetQuoteSource()] -" style "desc_text" textalign 0.5 xalign 0.5 yalign 0.5 size 12 color game_cyan_color
                                    frame:
                                        xfill True
                                        background None
                                        text "[selected_skill.GetDesc()]" style "desc_text"
                            text "-----------------" style "title_text" xalign 0.5 yalign 1.0
                hbox:
                    button:
                        xsize 192
                        ysize 50
                        style "hover_button"
                        sensitive att_pts_spent > 0
                        action [ Function(reset_skill_points) ]
                        text "RESET" xalign 0.5 yalign 0.5 style "select_button_text"
                    button:
                        xsize 192
                        ysize 50
                        style "hover_button"
                        sensitive att_pts_available == 0 and att_pts_spent > 0
                        if starting_game == True:
                            action Show( "game_confirm_box", None, [Function(apply_skill_points), Jump("start_test_scenario")], "This cannot be changed later", Fade )
                        else:
                            action Show( "game_confirm_box", None, [Function(apply_skill_points)], "This cannot be changed later" )
                        text "CONFIRM" xalign 0.5 yalign 0.5 style "select_button_text"
