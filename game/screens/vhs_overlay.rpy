default clock_hours = 0
default clock_minutes = 0
default clock_seconds = 0
default clock_running = True

screen vhs_overlay():
#timer 1.0 action Function(update_clock) repeat clock_running
    image "gui/vhs_lines.webp"
    zorder 100
    layer "vhs_screens"
    frame:
        xsize 1853
        ysize 1012
        background None
        yalign 0.5
        xalign 0.5
        xpadding 41
        ypadding 41
        hbox:
            spacing 10
            text "PLAY" style "vhs_overlay_text"
            image "gui/vhs_arrow.webp" ypos 11 
        text "SLP" style "vhs_overlay_text" yalign 1.0
        text "--:--" style "vhs_overlay_text" xalign 1.0
        #text "{:02d}:{:02d}:{:02d}".format(clock_hours, clock_minutes, clock_seconds) style "vhs_overlay_text" xalign 1.0 yalign 1.0
        

style vhs_overlay_text:
    size 65
    color "#c8c8c8"
    outlines [(2, "#000000", 1, 1)]

# init python:
#     config.overlay_screens.append("vhs_overlay")

# Ren'Py Real-Time Clock System
# Add this code to your script.rpy file

# Initialize the clock variables


# Clock update function
init python:
    def update_clock():
        global clock_seconds, clock_minutes, clock_hours
        
        if store.clock_running:
            store.clock_seconds += 1
            
            # Handle seconds overflow
            if store.clock_seconds >= 60:
                store.clock_seconds = 0
                store.clock_minutes += 1
                
                # Handle minutes overflow
                if store.clock_minutes >= 60:
                    store.clock_minutes = 0
                    store.clock_hours += 1