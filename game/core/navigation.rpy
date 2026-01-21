
init python:

######################################################################################################################################

    class game_room(store.object):
        def __init__(self, **kwargs):
            self.name = kwargs.get("name", None)
            self.game_label = kwargs.get("game_label", None)
            self.room_hub = kwargs.get("room_hub", False)
            self.address = kwargs.get("address", None)
            self.location = kwargs.get("location", None)
            self.room_travels = kwargs.get("room_travels", [])
            self.base_travel_sound = kwargs.get("travel_sound", "sfx/travel/default_travel.wav")
            self.travel_sound_table = kwargs.get("travel_sound_table", {})

    # Function to set the current room directly
    def set_room(new_room):
        global current_room
        global available_travels
        available_travels = new_room.room_travels
        # If the new room is a hub, add other hubs to available travels
        if new_room.room_hub:
            for i in available_rooms:
                if i.room_hub and i != new_room and i not in available_travels:
                    available_travels.append(i)
        current_room = new_room

    # Function to move to a different room
    def move_room(to_where):
        global cgt_message
        if not available_rooms or to_where in available_rooms:
            set_room(to_where)
            renpy.jump(to_where.game_label)
        else:
            renpy.say("", cgt_message )

    

######################################################################################################################################
