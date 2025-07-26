screen game_confirm_box (on_confirm, desc = None, hide_transition = None):
    modal True
    zorder 999
    frame:
        background Solid ((0,0,0,200))
    frame:
        #xsize 500
        #ysize 150
        xalign 0.5
        yalign 0.5
        grid 1 3:
            text "Are you sure?" xalign 0.5 yalign 0.25
            if desc <> None:
                text "[desc]" xalign 0.5
            grid 2 1:
                xalign 0.5
                #yalign 0.75
                button:
                    xsize 230
                    ysize 60
                    xalign 0.5
                    yalign 0.5
                    #xalign 0.5
                    selected False
                    style "hover_button"
                    action [ Hide(None, hide_transition), on_confirm]
                    fixed:
                        xsize 230
                        ysize 60
                        xalign 0.5 
                        yalign 0.5
                        text "Yes" xalign 0.5 yalign 0.5
                button:
                    xsize 230
                    ysize 60
                    xalign 0.5
                    yalign 0.5
                    #xalign 0.5
                    selected False
                    style "hover_button"
                    action Hide()
                    fixed:
                        xsize 230
                        ysize 60
                        xalign 0.5 
                        yalign 0.5
                        text "No" xalign 0.5 yalign 0.5