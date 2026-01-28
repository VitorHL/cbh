transform dice_roll_trans:
    zoom 0.75
    linear 0.075 rotate 1
    linear 0.075 rotate -1
    repeat

transform dice_roll_trans_final:
    zoom 1
    linear 0.05 zoom 0.75

transform dice_number_anim:
    zoom 1
    linear 0.1 zoom 0.9
    repeat

transform dice_result_final:
    zoom 1.5
    linear 0.05 zoom 1

screen dice_roll_anim(total, difficulty, dice1, dice2, skill, skill_buffs):
    default buffs_for_this_check = []
    default changing_number_1 = 1
    default changing_number_2 = 1
    timer 0.1 repeat True action SetScreenVariable("changing_number_1", ([x for x in range(1, 7) if x != changing_number_1][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action SetScreenVariable("changing_number_2", ([x for x in range(1, 7) if x != changing_number_2][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action Play("sound", "audio/dice_tick.wav")
    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing -20
            xalign 0.5
            # Only 2 dice now
            frame:
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(changing_number_1) at dice_roll_trans xalign 0.5 yalign 0.5
            frame:
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(changing_number_2) at dice_roll_trans xalign 0.5 yalign 0.5
        frame:
            style "black_tile_75"
            ypadding 0
            xalign 0.5
            xsize 385
            vbox xalign 0.5:
                text "-------------" style "title_text" xalign 0.5 yalign 0.5
                hbox:
                    spacing 7
                    xalign 0.5
                    # Only 2 dice in the formula display
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "[changing_number_1]" style "title_text" at dice_number_anim xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "+" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "[changing_number_2]" style "title_text" at dice_number_anim xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "+" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        ysize 30
                        background None
                        text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" color game_yellow_color xalign 0.5 yalign 0.5

                if len(skill_buffs) > 0 and any(buff in available_skill_buffs for buff in skill_buffs):    
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 10
                        for buff in skill_buffs:
                            if buff in available_skill_buffs:
                                if buff.value >= 0:
                                    text "[buff.GetName()]:+[buff.value]" ypos 15 xalign 0.5 style "vhs_gothic" color game_green_strong_color size 16
                                else:
                                    text "[buff.GetName()]:[buff.value]" ypos 15 xalign 0.5 style "vhs_gothic" color game_red_strong_color size 16

                text "-------------" style "title_text" xalign 0.5 yalign 0.5
        frame:
            style "black_tile_border_75"
            ypos 10
            xpadding 40
            ypadding 20
            xalign 0.5
            hbox:
                spacing 15
                xalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    # Updated formula: only 2 dice + skill
                    text "{:02d}".format(sum([changing_number_1,changing_number_2,skill.level])) style "title_text" at dice_number_anim size 60 xalign 0.5 yalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    text "/" style "title_text" size 60 xalign 0.5 yalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    text "{:02d}".format(difficulty) style "title_text" size 60 xalign 0.5 yalign 0.5

# Results screen - also updated for 2 dice            
screen dice_roll(total, difficulty, dice1, dice2, skill, skill_buffs=[]):
    on "show" action Play("sound", "audio/dice_result.wav")
    
    # Calculate if this was a natural 2 or 12
    $ natural_roll = dice1 + dice2
    $ is_snake_eyes = (natural_roll == 2)
    $ is_boxcars = (natural_roll == 12)
    
    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing -20
            xalign 0.5
            # Only 2 dice
            frame:
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(dice1) at dice_roll_trans_final xalign 0.5 yalign 0.5
            frame:
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(dice2) at dice_roll_trans_final xalign 0.5 yalign 0.5
        frame:
            style "black_tile_75"
            ypadding 0
            xalign 0.5
            xsize 385
            vbox xalign 0.5 :
                text "-------------" style "title_text" xalign 0.5 yalign 0.5
                hbox:
                    spacing 7
                    xalign 0.5
                    # Only 2 dice in formula
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "[dice1]" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "+" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "[dice2]" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        xsize 40
                        ysize 30
                        background None
                        text "+" style "title_text" xalign 0.5 yalign 0.5
                    frame:
                        ysize 30
                        background None
                        text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" color game_yellow_color xalign 0.5 yalign 0.5
                
                # Show special roll indicator
                if is_snake_eyes:
                    text "SNAKE EYES - AUTO FAIL!" style "title_text" color game_red_strong_color size 20 xalign 0.5
                elif is_boxcars:
                    text "BOXCARS - AUTO SUCCESS!" style "title_text" color game_green_strong_color size 20 xalign 0.5
                
                if len(skill_buffs) > 0 and any(buff in available_skill_buffs for buff in skill_buffs):    
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        spacing 10
                        for buff in skill_buffs:
                            if buff in available_skill_buffs:
                                if buff.value >= 0:
                                    text "[buff.GetName()]:+[buff.value]" ypos 15 xalign 0.5 style "vhs_gothic" color game_green_strong_color size 16
                                else:
                                    text "[buff.GetName()]:[buff.value]" ypos 15 xalign 0.5 style "vhs_gothic" color game_red_strong_color size 16
                                        
                text "-------------" style "title_text" xalign 0.5 yalign 0.5
        frame:
            style "black_tile_border_75"
            ypos 10
            xpadding 40
            ypadding 20
            xalign 0.5
            hbox:
                spacing 15
                xalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    if total >= difficulty and not is_snake_eyes:
                        text "{:02d}".format(total) style "title_text" color game_green_strong_color size 60 at dice_result_final xalign 0.5 yalign 0.5
                    else:
                        text "{:02d}".format(total) style "title_text" color game_red_strong_color size 60 at dice_result_final xalign 0.5 yalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    text "/" style "title_text" size 60 xalign 0.5 yalign 0.5
                frame:
                    xsize 60
                    ysize 60
                    background None
                    text "{:02d}".format(difficulty) style "title_text" size 60 xalign 0.5 yalign 0.5