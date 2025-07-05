transform travel_entry_dot:
    on idle:   
        xsize 42
        ysize 42
    on hover:
        xsize 52
        ysize 52

style entrytext:
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_color "#000000"
    hover_outlines [(0, "#000000", 0, 0)]
    hover_size 45

screen travel(items):
    #style_prefix "choice"
    default thumb = "generic"
    default address = "???"
    frame:
        xfill True
        yfill True
        background Transform("black", alpha = 0.5)
    fixed:
        xsize 1280
        ysize 480
        xalign 0.5
        yalign 0.5
        fixed:
            xsize 640
            ysize 480
            hbox:
                spacing 10
                frame:
                    xsize 52
                    ysize 52
                    background Frame("gui/tiles/black_tile.webp", 3, 3)
                frame:
                    xfill True
                    background Frame("gui/tiles/black_tile.webp", 3, 3)
                    text "Travel" size 45
            vbox:
                #xalign 0.0
                yalign 0.5
                spacing 4
                for i in items:
                    $ room_thumb = i.kwargs.get("room_thumb", None)
                    $ room_address = i.kwargs.get("room_address", "???")
                    
                    button:
                        #ymaximum 40
                        action i.action
                        hovered [SetScreenVariable("thumb", room_thumb), SetScreenVariable( "address", room_address,  )]
                        selected False
                        sensitive True
                        hbox:
                            spacing 10
                            frame:
                                xpos 0
                                ypos 0
                                at travel_entry_dot
                                background Frame("gui/tiles/black_tile.webp", 3, 3)
                                hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                            frame:
                                background Transform(Frame("gui/tiles/black_tile.webp", 3, 3),alpha = 0.5)
                                hover_background Frame("gui/tiles/white_tile.webp", 3, 3)
                                text "[i.caption]": 
                                    yalign 0.5
                                    style "entrytext"
#at "entrytext_trans"
        fixed:
            xsize 640
            ysize 480
            xalign 1.0 
            yalign 0.5
            image "thumbnail_{0}_bg".format(thumb)
            frame: 
                xalign 0.5 
                yalign 1.0 
                background Frame("gui/tiles/black_tile.webp", 3, 3)
                text "[address]": 
                    textalign 0.5 
                