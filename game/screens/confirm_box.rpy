screen game_confirm_box (on_confirm, desc = None, hide_transition = None):
    modal True
    zorder 999
    frame:
        background Solid ((0,0,0,200))
    frame:
        background None
        xsize 500
        #xsize 500
        #ysize 150
        xalign 0.5
        yalign 0.5
        vbox:
            hbox:
                frame:
                        style "black_tile"
                        xsize 50
                        ysize 50
                        text "*" xalign 0.5 yalign 0.5
                frame:
                        style "black_tile"
                        xsize 390
                        ysize 50
                        text "ARE YOU SURE?" xalign 0.5 yalign 0.25
                frame:
                        style "black_tile"
                        xsize 50
                        ysize 50
                        text "*" xalign 0.5 yalign 0.5
            frame:
                style "black_tile_75"
                xfill True
                vbox:
                    spacing 15
                    text "-------------------------" xalign 0.5
                    if desc != None:
                        text "[desc]" xalign 0.5 yalign 0.5 style "desc_text"
                    text "-------------------------" xalign 0.5
            hbox:
                xalign 0.5
                #yalign 0.75
                button:
                    xsize 245
                    ysize 50
                    xalign 0.5
                    yalign 0.5
                    style "hover_button"
                    action [ Hide(None, hide_transition), on_confirm]
                    fixed:
                        text "YES" xalign 0.5 yalign 0.5 style "hover_button_text"
                button:
                    xsize 245
                    ysize 50
                    xalign 0.5
                    yalign 0.5
                    selected False
                    style "hover_button"
                    action Hide()
                    fixed:
                        xsize 230
                        ysize 60
                        xalign 0.5 
                        yalign 0.5
                        text "NO" xalign 0.5 yalign 0.5 style "hover_button_text"