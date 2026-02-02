transform pause_anim:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.25
    repeat

screen vhs_overlay():
    # Use Ren'Py's built-in _menu variable instead of game_paused
    # _menu is True when any game menu screen is showing
    
    # Only run the timer when not in a menu
    if not _menu:
        timer 1.0 action Function(update_clock) repeat True
    
    zorder 100
    layer "vhs_screens"
    
    # Scanlines effect
    image "gui/vhs_lines.webp"
    
    frame:
        xsize 1853
        ysize 1012
        background None
        yalign 0.5
        xalign 0.5
        xpadding 41
        ypadding 41
        
        # Top-left: PLAY/STOP indicator
        hbox:
            spacing 15
            if _menu:
                text "PAUSE" style "vhs_overlay_text" at pause_anim
                image "gui/vhs_pause.webp" ypos 11 at pause_anim
            else:
                text "PLAY" style "vhs_overlay_text"
                image "gui/vhs_arrow.webp" ypos 11 
        
        # Bottom-left: SLP indicator
        text "SLP" style "vhs_overlay_text" yalign 1.0
        
        # Top-right: Date/placeholder
        text "--:--" style "vhs_overlay_text" xalign 1.0
        
        # Bottom-right: Clock
        text "{:02d}:{:02d}:{:02d}".format(clock_hours, clock_minutes, clock_seconds):
            style "vhs_overlay_text"
            xalign 1.0
            yalign 1.0


style vhs_overlay_text:
    size 65
    color "#c8c8c8"
    outlines [(2, "#000000", 1, 1)]


init python:
    def update_clock():
        store.clock_seconds += 1
        
        if store.clock_seconds >= 60:
            store.clock_seconds = 0
            store.clock_minutes += 1
            
            if store.clock_minutes >= 60:
                store.clock_minutes = 0
                store.clock_hours += 1
                
                if store.clock_hours >= 100:
                    store.clock_hours = 0