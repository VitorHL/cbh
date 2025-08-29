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

screen dice_roll_anim(total, difficulty, dice1, dice2, dice3, skill):
    default changing_number_1 = 1
    default changing_number_2 = 1
    default changing_number_3 = 1
    timer 0.1 repeat True action SetScreenVariable("changing_number_1", ([x for x in range(1, 7) if x != changing_number_1][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action SetScreenVariable("changing_number_2", ([x for x in range(1, 7) if x != changing_number_2][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action SetScreenVariable("changing_number_3", ([x for x in range(1, 7) if x != changing_number_3][renpy.random.randint(0, 4)]))
    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing -20
            xalign 0.5
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
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(changing_number_3) at dice_roll_trans xalign 0.5 yalign 0.5
        hbox:
            spacing 7
            xalign 0.5
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
                xsize 40
                ysize 30
                background None
                text "[changing_number_3]" style "title_text" at dice_number_anim xalign 0.5 yalign 0.5
            frame:
                xsize 40
                ysize 30
                background None
                text "+" style "title_text" xalign 0.5 yalign 0.5
            frame:
                #xsize 40
                ysize 30
                background None
                text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" xalign 0.5 yalign 0.5
        hbox:
            ypos 20
            spacing 15
            xalign 0.5
            frame:
                xsize 60
                ysize 60
                background None
                text "{:02d}".format(sum([changing_number_1,changing_number_2,changing_number_3,skill.level])) style "title_text" at dice_number_anim size 60 xalign 0.5 yalign 0.5
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
            
screen dice_roll(total, difficulty, dice1, dice2, dice3, skill):
    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing -20
            xalign 0.5
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
                xsize 200
                ysize 200
                background None
                image "/gui/dice/dice_{0}.webp".format(dice3) at dice_roll_trans_final xalign 0.5 yalign 0.5
        hbox:
            spacing 7
            xalign 0.5
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
                xsize 40
                ysize 30
                background None
                text "[dice3]" style "title_text" xalign 0.5 yalign 0.5
            frame:
                xsize 40
                ysize 30
                background None
                text "+" style "title_text" xalign 0.5 yalign 0.5
            frame:
                #xsize 30
                ysize 30
                background None
                text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" xalign 0.5 yalign 0.5
        hbox:
            ypos 20
            spacing 15
            xalign 0.5
            frame:
                xsize 60
                ysize 60
                background None
                text "{:02d}".format(total) style "title_text" size 60 at dice_result_final xalign 0.5 yalign 0.5
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


screen dice_roll_fake_0():
    default changing_number = 1
    timer 0.1 repeat True action SetScreenVariable("changing_number", ([x for x in range(1, 7) if x != changing_number][renpy.random.randint(0, 4)]))
    image "/gui/dice/dice_{0}.webp".format(changing_number) at dice_roll_trans xalign 0.4 yalign 0.4

screen dice_roll_fake_1():
    default changing_number = 1
    timer 0.1 repeat True action SetScreenVariable("changing_number", ([x for x in range(1, 7) if x != changing_number][renpy.random.randint(0, 4)]))
    image "/gui/dice/dice_{0}.webp".format(changing_number) at dice_roll_trans xalign 0.5 yalign 0.4

screen dice_roll_fake_2():
    default changing_number = 1
    timer 0.1 repeat True action SetScreenVariable("changing_number", ([x for x in range(1, 7) if x != changing_number][renpy.random.randint(0, 4)]))
    image "/gui/dice/dice_{0}.webp".format(changing_number) at dice_roll_trans xalign 0.6 yalign 0.4

screen dice_roll_0(result, difficulty):
    image "/gui/dice/dice_{0}.webp".format(result) at dice_roll_trans_final xalign 0.4 yalign 0.4
screen dice_roll_1(result, difficulty):
    image "/gui/dice/dice_{0}.webp".format(result) at dice_roll_trans_final xalign 0.5 yalign 0.4
screen dice_roll_2(result, difficulty):
    image "/gui/dice/dice_{0}.webp".format(result) at dice_roll_trans_final xalign 0.6 yalign 0.4

screen dice_roll_result_fake(skill):
    default changing_result_1 = 1
    default changing_result_2 = 1
    default changing_result_3 = 1
    #default result_total = changing_result_1 + changing_result_2 + changing_result_3
    timer 0.1 repeat True action SetScreenVariable("changing_result_1", ([x for x in range(1, 7) if x != changing_result_1][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action SetScreenVariable("changing_result_2", ([x for x in range(1, 7) if x != changing_result_2][renpy.random.randint(0, 4)]))
    timer 0.1 repeat True action SetScreenVariable("changing_result_3", ([x for x in range(1, 7) if x != changing_result_3][renpy.random.randint(0, 4)]))
    #text "[changing_result_1] + [changing_result_2] + [changing_result_3] = [sum([changing_result_1,changing_result_2,changing_result_3])]" xalign 0.5 yalign 0.5
    hbox:
        spacing 7
        xalign 0.5
        yalign 0.6
        frame:
            #xsize 30
            ysize 30
            background None
            text "[changing_result_1]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[changing_result_2]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[changing_result_3]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" xalign 0.5 yalign 0.5

screen dice_roll_result(skill, dice1, dice2, dice3):
    hbox:
        spacing 7
        xalign 0.5
        yalign 0.6
        frame:
            #xsize 30
            ysize 30
            background None
            text "[dice1]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[dice2]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[dice3]" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "+" style "title_text" xalign 0.5 yalign 0.5
        frame:
            #xsize 30
            ysize 30
            background None
            text "[skill_tag_dict[skill.GetName()]]:[skill.level]" style "title_text" xalign 0.5 yalign 0.5