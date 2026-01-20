
init python:

######################################################################################################################################

    class game_room(store.object):
        def __init__(self, game_label, name = None, address = None, location = None):
            self.name = name
            self.game_label = game_label
            self.address = address
            self.location = location
    
    def move_room(to_where):
        global current_room
        global cgt_message
        if not available_rooms or to_where in available_rooms:
            current_room = to_where
            renpy.jump(to_where.game_label)
        else:
            renpy.say("", cgt_message )

######################################################################################################################################

    def travel_menu(new_entries=None):
        global available_travels, current_room
        
        # Start with empty list
        menu_list = []
        
        # Add new_entries if provided
        if new_entries is not None:
            # If it's a single room object, wrap it in a tuple
            if hasattr(new_entries, 'name'):
                new_entries = (new_entries,)
            
            # Add each room from new_entries
            for room in new_entries:
                var_name = get_var_name(room, globals())[0]
                menu_list.append((room.name, renpy.Choice(room, room_thumb=var_name, room_address=room.address, room_location=room.location) ))
        
        # Add items from available_travels, excluding current_room
        for room in available_travels:
            if room != current_room:
                var_name = get_var_name(room, globals())[0]
                menu_list.append( (room.name, renpy.Choice(room, room_thumb=var_name, room_address=room.address, room_location=room.location) ) )
        
        # Display the menu with the processed list
        room = renpy.display_menu(menu_list, "" , True, screen='travel'  )
        move_room(room)