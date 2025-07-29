define sounds = ['audio/default_talk_blip.ogg']

init python:
    # Importing Important Stuff
    import renpy.store as store
    import renpy.exports as renpy

    class game_calendar(store.object):
        def __init__(self, weekday, month, day, year):
            self.weekday = weekday
            self.month = month
            self.day = day
            self.year = year

            # Days per month dictionary
            self.days_per_month = {
                0: 31,   # January
                1: 28,   # February
                2: 31,   # March
                3: 30,   # April
                4: 31,   # May
                5: 30,   # June
                6: 31,   # July
                7: 31,   # August
                8: 30,   # September
                9: 31,   # October
                10: 30,  # November
                11: 31   # December
            }
        
        def is_leap_year(self, year):
            """Check if a year is a leap year"""
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
        def get_days_in_month(self, month, year):
            """Get the number of days in a given month, accounting for leap years"""
            days = self.days_per_month[month]
            # Adjust February for leap years
            if month == 1 and self.is_leap_year(year):
                days = 29
            return days
        
        def next_day(self): #Go to the next day
            global events_played_today, room_where_events_played_already, interactions_played_today
            self.day += 1
            events_played_today.clear()
            room_where_events_played_already.clear()
            for interaction in interactions_played_today:
                interaction.runs_today = 0
            interactions_played_today.clear()
            
            # Handle weekday progression
            if self.weekday >= 6:  # Sunday (assuming 0=Monday, 6=Sunday)
                self.weekday = 0
            else:
                self.weekday += 1
            
            # Handle month/year progression
            days_in_current_month = self.get_days_in_month(self.month, self.year)
            
            if self.day > days_in_current_month:
                self.day = 1  # Reset to first day of new month
                
                if self.month >= 11:  # December (month 11)
                    self.month = 0  # Reset to January
                    self.year += 1  # Advance to next year
                else:
                    self.month += 1  # Advance to next month


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
        if not avaliable_rooms or to_where in avaliable_rooms:
            current_room = to_where
            renpy.jump(to_where.game_label)
        else:
            renpy.say("", cgt_message )

######################################################################################################################################

    

    def travel_menu(new_entries=None):
        global avaliable_travels, current_room
        
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
        
        # Add items from avaliable_travels, excluding current_room
        for room in avaliable_travels:
            if room != current_room:
                var_name = get_var_name(room, globals())[0]
                menu_list.append( (room.name, renpy.Choice(room, room_thumb=var_name, room_address=room.address, room_location=room.location) ) )
        
        # Display the menu with the processed list
        room = renpy.display_menu(menu_list, "" , True, screen='travel'  )
        move_room(room)


    ############################################################################################################################################

    class game_event(store.object): 
        def __init__(self,priority,game_label,game_room = None,**kwargs):
            self.priority = priority
            self.game_label = game_label
            self.game_room = game_room  
            self.day = kwargs.get('day', None)
            self.month = kwargs.get('month', None)
            self.year = kwargs.get('year', None)
            self.weekday = kwargs.get('weekday', None)
            self.instances = kwargs.get ('instances', 1) # if set to zero or less, the event is infinite
            self.runs = 0

    def run_event(event_to_run):
        global avaliable_events, ongoing_event
        event_to_run.runs += 1
        # Checks if the event is single use or can run multiple times, if instance <= the event is infinite.
        if event_to_run.instances == 1:
            avaliable_events.remove(event_to_run)
        elif event_to_run.instances > 1:
            event_to_run.instances - 1
        room_where_events_played_already.clear()
        ongoing_event = event_to_run
        renpy.call(event_to_run.game_label)

    def end_event():
        global ongoing_event, finished_events, events_played_today, room_where_events_played_already
        finished_events.append(ongoing_event)
        events_played_today.append(ongoing_event)
        room_where_events_played_already.append(current_room)
        del ongoing_event
        renpy.return_statement()


    def check_for_event():
        global current_room, avaliable_events, finished_events, events_played_today, room_where_events_played_already, calendar

        # Filter events that meet all criteria
        suitable_events = []
        
        for event in avaliable_events:
            # Check if event matches current room
            if event.game_room == current_room or event.game_room is None:
            # Check if event hasn't been played today
                if event not in events_played_today:
                    # Check if current room is not in rooms where events were played already
                    if current_room not in room_where_events_played_already:
                        
                        # Check calendar-based conditions
                        calendar_suitable = True
                        
                        # Check day if specified
                        if hasattr(event, 'day') and event.day is not None:
                            if event.day != calendar.day:
                                calendar_suitable = False
                        
                        # Check month if specified
                        if hasattr(event, 'month') and event.month is not None:
                            if event.month != calendar.month:
                                calendar_suitable = False
                        
                        # Check year if specified
                        if hasattr(event, 'year') and event.year is not None:
                            if event.year != calendar.year:
                                calendar_suitable = False
                        
                        # Check weekday if specified
                        if hasattr(event, 'weekday') and event.weekday is not None:
                            if event.weekday != calendar.weekday:
                                calendar_suitable = False
                        
                        # Only add to suitable events if all calendar conditions are met
                        if calendar_suitable:
                            suitable_events.append(event)
        
        # If we found suitable events, get the one with lowest priority
        if suitable_events:
            # Sort by priority (lowest first) and get the first one
            best_event = min(suitable_events, key=lambda event: event.priority)
            run_event(best_event)

#####################################################################################################################################################

    class game_interaction(store.object): 
        def __init__(self,game_label,**kwargs):
            self.game_label = game_label
            self.state = 0 # used mainly to set this interaction in diferent "modes"
            self.runs = 0
            self.runs_today = 0

    def run_interaction(interaction_to_run):
        global avaliable_interactions, ongoing_interaction
        if not avaliable_interactions or interaction_to_run in avaliable_interactions:
            ongoing_interaction = interaction_to_run
            renpy.call(interaction_to_run.game_label)
        else:
            renpy.say("", cdt_message )

    def end_interaction():
        global avaliable_interactions, ongoing_interaction, interactions_played_today
        ongoing_interaction.runs += 1
        ongoing_interaction.runs_today += 1
        interactions_played_today.append(ongoing_interaction)
        del ongoing_interaction
        renpy.return_statement()


#####################################################################################################################################################


    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds), loop=True)
        


        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1.0)

#####################################################################################################################################################

    class game_item(store.object):
        def __init__(self, icon, name, desc, game_label, interaction_mode=0):
            self.icon = icon
            self.name = name
            self.desc = desc
            self.game_label = game_label
            self.interaction_mode = interaction_mode

    def inspect_item(item):
        renpy.hide_screen("inventory_screen")
        #renpy.show_screen("inventory_screen")
        #renpy.say("", "Annoying shit")
        #renpy.call(item.game_label)
        #renpy.jump(item.game_label)

########################################################################################################################################################

    class game_character(store.object):
        def __init__(self, name,game_label, small_talk_game_label, generic_show_label):
            self.name = name
            self.game_label = game_label # The intro dialogue played when you click in the character
            self.small_talk_game_label = small_talk_game_label
            self.generic_show_label = generic_show_label
            self.interested_talks = {}
            self.interested_items = {}
            self.flags = {}

            def add_talk(self, topic, dialogue):
                self.interested_talks[topic] = dialogue
            
            def add_item_reaction(self, item, reaction):
                self.interested_items[item] = reaction
            
            def set_flag(self, flag_name, value):
                self.flags[flag_name] = value

            def remove_talk(self, topic):
                if topic in self.interested_talks:
                    del self.interested_talks[topic]
            
            def remove_item_reaction(self, item):
                if item in self.interested_items:
                    del self.interested_items[item]
            
            def remove_flag(self, flag_name):
                if flag_name in self.flags:
                    del self.flags[flag_name]

#####################################################################################################################################################

    def generate_character_talks(character):
        """
        Creates a Ren'Py menu from a class object's interested_talks dictionary.
        
        Args:
            class_object: Object with interested_talks dictionary attribute
            
        Returns:
            The result of renpy.display_menu()
        """
        # Create tuples from the interested_talks dictionary
        menu_items = []
        label = "gia_show_coke"
        
        for key, value in character.interested_talks.items():
            # Create a lambda that captures the current value and class_object
            # This ensures the correct values are used when the menu item is selected
            menu_action = lambda v=value, obj=character: renpy.call(v, obj)
            
            # Create tuple: (display_text, action_function)
            menu_items.append((key, renpy.Choice(None, game_label=value, character=character) ))
        
        # Feed the tuple list to renpy.display_menu
        return renpy.display_menu(menu_items,"",interact=True,screen="choice_talks", args=[("character",character)])

#####################################################################################################################################################

    class game_skill(store.object):
        def __init__(self):
            self.level = 1
            self.invested = 0
            self.current = 1
            
        def GetName(self):
            return get_var_suffix(self, "loc")

        def GetDesc(self):
            return get_var_suffix(self, "desc")

        def GetQuote(self):
            return get_var_suffix(self, "quote")