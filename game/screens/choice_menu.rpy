screen travel(items):
    #style_prefix "choice"
    default thumb = "generic"
    default address = "???"
    vbox:
        xalign 0.25
        yalign 0.5
        for i in items:
            $ room_thumb = i.kwargs.get("room_thumb", None)
            $ room_address = i.kwargs.get("room_address", "???")
            #textbutton i.caption action i.action hovered [SetScreenVariable("thumb", room_thumb), SetScreenVariable( "address", room_address,  )]
            button:
                
                action i.action
                hovered [SetScreenVariable("thumb", room_thumb), SetScreenVariable( "address", room_address,  )]
                text "[i.caption]" yalign 0.5
    frame:
        xsize 640
        ysize 480
        xalign 0.75 
        yalign 0.5
        image "thumbnail_{0}_bg".format(thumb) 
        text "[address]" textalign 0.5 xalign 0.5 yalign 1.0 