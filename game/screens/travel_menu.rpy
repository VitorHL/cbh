image travel_static:
    "gui/thumbnails/generic/travel_static_00.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_01.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_02.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_03.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_04.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_05.webp"
    pause 0.06
    "gui/thumbnails/generic/travel_static_06.webp"
    pause 0.06
    repeat

image travel_guy_icon:
    "gui/travel_menu/travel_icons/travel_header_00.webp"
    pause 0.5
    "gui/travel_menu/travel_icons/travel_header_01.webp"
    pause 0.5
    "gui/travel_menu/travel_icons/travel_header_02.webp"
    pause 0.5
    "gui/travel_menu/travel_icons/travel_header_03.webp"
    pause 0.5
    repeat

################################################################################
# Travel Menu Screen
# Displays a list of available rooms to travel to, with thumbnails and details.
################################################################################

screen travel():
    default selected_room = None
    default dot_count = 0
    
    # Timer to animate dots (fires every 0.5 seconds)
    timer 0.5 repeat True action SetScreenVariable("dot_count", (dot_count + 1) % 4)
    
    # Darken background
    frame:
        xfill True
        yfill True
        background Transform("black", alpha=0.5)
    
    # Main container
    fixed:
        xsize 1300
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            #spacing -15
                
            hbox:
                frame:
                    style "black_tile_border"
                    xsize 60
                    ysize 60
                    image "travel_guy_icon" xalign 0.5 yalign 0.5 zoom 0.75
                frame:
                    xfill True
                    ysize 60
                    style "black_tile_underline"
                    $ dots = "." * dot_count
                    text "TRAVEL[dots]" size 35 yalign 0.25
            hbox:
                xalign 0.5
                yalign 0.5
                #spacing 20
                
                # Left panel - Room list
                frame:
                    xsize 650
                    ysize 540
                    style "black_tile_hollow"
                    
                    vbox:
                        spacing 5
                        # Room list
                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            #scrollbars "vertical"
                            
                            vbox:
                                spacing 8
                                xfill True
                                
                                for room in available_travels:
                                    button:
                                        xfill True
                                        ysize 60
                                        #style "hover_button"
                                        action SetScreenVariable("selected_room", room)
                                        hbox:
                                            frame xsize 60 ysize 60 style "select_button":
                                                if room.known == False:
                                                    text "?" xalign 0.5 yalign 0.5 style "select_button_text"
                                                elif room.icon and renpy.loadable(room.icon):
                                                    add room.icon xalign 0.5 yalign 0.5 at select_image
                                                else:
                                                    add "gui/travel_menu/travel_icons/travel_icon_generic.webp" xalign 0.5 yalign 0.5 at select_image
                                            frame xfill True ysize 60 style "select_button":
                                                text f"{room.name.upper()}":
                                                        xpos 20
                                                        yalign 0.5
                                                        style "select_button_text"
                                        
                                        #hovered SetScreenVariable("selected_room", room)
                                        #unhovered SetScreenVariable("selected_room", None)
                                        hover_sound "audio/menu_hover.wav"
                                        activate_sound "audio/menu_select.wav"
                                        
                                        
                
                # Right panel - 
                vbox:
                    xalign 0.5
                    frame:
                        xsize 650
                        ysize 490
                        style "black_tile"
                        
                        if selected_room:
                            
                            # Thumbnail
                            if renpy.loadable(selected_room.thumb) and selected_room.known:
                                add selected_room.thumb xalign 0.5 yalign 0.5
                            else:
                                add "travel_static" xalign 0.5 yalign 0.5
                            
                            # Location label (top)
                            vbox:
                                xalign 0.5
                                yalign 0.05
                                if selected_room.location:
                                    for line in selected_room.location:
                                        frame:
                                            xalign 0.5
                                            style "black_tile"
                                            text line:
                                                xalign 0.5
                                                yalign 0.5
                                                style "vhs_gothic"
                                else:
                                    frame:
                                        xalign 0.5
                                        style "black_tile"
                                        text "???" textalign 0.5 style "vhs_gothic"
                                        
                            # Address label (bottom)
                            vbox:
                                xalign 0.5
                                yalign 0.95
                                
                                if selected_room.address:
                                    for line in selected_room.address:
                                        frame:
                                            xalign 0.5
                                            #yalign 0.5
                                            style "black_tile"
                                            text line:
                                                textalign 0.
                                                style "vhs_gothic"
                                else:
                                    frame:
                                        xalign 0.5
                                        style "black_tile"
                                        text "???" textalign 0.5 style "vhs_gothic"
                        
                        else:
                            # No room selected
                            text "SELECT A DESTINATION" size 35 xalign 0.5 yalign 0.5
                        frame:
                            xsize 640
                            ysize 480
                            xalign 0.5
                            yalign 0.5
                            style "border_white"
                    hbox:
                        xalign 0.5
                        #yalign 0.75
                        button:
                            xsize 325
                            ysize 50
                            #xalign 0.5
                            #yalign 0.5
                            style "hover_button"
                            action Return()
                            fixed:
                                text "<< BACK" xalign 0.5 yalign 0.5 style "select_button_text"
                        button:
                            xsize 325
                            ysize 50
                            #xalign 0.5
                            #yalign 0.5
                            selected False
                            style "hover_button"
                            sensitive selected_room is not None
                            action Function(move_room, selected_room)
                            fixed:
                                xsize 230
                                ysize 60
                                xalign 0.5 
                                yalign 0.5
                                text "CONFIRM >>" xalign 0.5 yalign 0.5 style "select_button_text"
