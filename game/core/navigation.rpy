
init python:

################################################################################
# Classes 
################################################################################

    # Game Room Class Definition
    class game_room(store.object):
        def __init__(self, **kwargs):
            self.name = kwargs.get("name", None) # Name of the room
            self.game_label = kwargs.get("game_label", None) # Label to jump to when entering the room
            self.room_hub = kwargs.get("room_hub", False) # If true, this room acts as a hub and adds other hubs to available travels
            self.address = kwargs.get("address", None) # Address of the room
            self.location = kwargs.get("location", None) # Location of the room
            self.room_travels = kwargs.get("room_travels", []) # List of rooms the player can travel to from this room
            self.base_travel_sound = kwargs.get("travel_sound", "sfx/travel/default_travel.wav") # Default sound played when traveling from this room
            self.travel_sound_table = kwargs.get("travel_sound_table", {}) # Dictionary with specific travel sounds for specific rooms
            self.thumb = kwargs.get("thumb", None) # Thumbnail image path for the room
            self.icon = kwargs.get("icon", None) # Icon image path for the room
            self.known = kwargs.get("known", False) # If false, the room is unknown and will display "???" in travel menu

        def GetThumb(self):
            return get_var_suffix(self, "thumbnail")

        @property
        def room_travels(self):
            # Lazily resolve string references to actual room objects
            resolved = []
            for item in self._room_travels:
                if isinstance(item, str):
                    # Look up the room by name in the store
                    resolved.append(getattr(store, item))
                else:
                    # Already a room object
                    resolved.append(item)
            return resolved
        
        @room_travels.setter
        def room_travels(self, value):
            self._room_travels = value

################################################################################
# Functions
################################################################################

    # Helper to resolve a room reference (string or object)
    def resolve_room(room_ref):
        if isinstance(room_ref, str):
            return getattr(store, room_ref)
        return room_ref
    
    # Function to set the current room directly
    def set_room(new_room):
        global current_room
        global available_travels

        # Resolve string references to actual room objects
        available_travels = [resolve_room(r) for r in new_room.room_travels]

        # Mark the room as known when visited
        if new_room.known == False:
            new_room.known = True

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

