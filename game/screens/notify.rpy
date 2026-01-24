default notify_messages = []

# Duration the full ATL takes
default notify_duration = 5.0

# Max number we store for reviewing in the history screen
default notify_history_length = 20

init python:

    import time

    def add_notify_message(msg=None):

        if not msg:
            return

        global notify_messages

        add_time = time.time()

        # Just in case multiple notifications are added really really 
        # fast, this gives them minorly different time values so they 
        # do not steal displayables meant for other notifications
        if notify_messages and notify_messages[-1][1] >= add_time:

            add_time = notify_messages[-1][1] + 0.01

        notify_messages.append((msg, add_time))

        # just keep notify_history_length number of messages
        notify_messages = notify_messages[-notify_history_length:]

        renpy.show_screen("notify_container")
        renpy.restart_interaction()


    def finish_notify(trans, st, at):

        max_start = time.time() - notify_duration

        if not [k for k in notify_messages if k[1] > max_start]:

            # If the notification list is now empty, hide the screen
            renpy.hide_screen("notify_container")
            renpy.restart_interaction()

        return None


define config.notify = add_notify_message

style notify_item_frame:

    background Frame("images/notify_frame_background.png", 10, 10)

    padding (16, 2, 16, 2)
    minimum (20,20)
    # xanchor 0.5


style notify_item_text:

    xsize None 
    align (0.5,0.5) 

    # just standard font specific stuff
    color "#FFF"
    outlines [(abs(2), "#000", abs(0), abs(0))]
    # font ""
    size 20


transform notify_appear():

    alpha 0.0 xpos -25

    linear 0.10 alpha 1.0 xpos 0

    pause 5.0

    linear 0.10 alpha 0.0 xpos -25

    function finish_notify


screen notify_item(msg, use_atl=True):

    hbox:
        frame:
            if use_atl: # ATL not used for history
                at notify_appear
            style "black_tile_75"
            text "*" style "notify_item_text"
        frame:

            if use_atl: # ATL not used for history
                at notify_appear
            style "black_tile_75"
            text msg style "notify_item_text"


screen notify_container():

    fixed:

        xpos 75
        ypos 150

        vbox:

            xmaximum 300
            spacing 5

            # We index on the time the notification was added as that
            # is unique. Using index helps manage the ATL nicely
            for msg_info index msg_info[1] in notify_messages:

                if msg_info[1] > time.time() - notify_duration:

                    use notify_item(msg_info[0])


screen notify_history():

    viewport:
        area (5, 50, 320, 380)
        # scrollbars "vertical"
        draggable True
        mousewheel True
        yinitial 1.0

        vbox:
            xfill True
            spacing 5

            for msg_info in notify_messages:

                use notify_item(msg_info[0], False)
            