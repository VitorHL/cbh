define sounds = ['audio/default_talk_blip.ogg']

init python:
    # Importing Important Stuff
    import renpy.store as store
    import renpy.exports as renpy
    import random

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
        global available_events, ongoing_event
        event_to_run.runs += 1
        # Checks if the event is single use or can run multiple times, if instance <= the event is infinite.
        if event_to_run.instances == 1:
            available_events.remove(event_to_run)
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
        global current_room, available_events, finished_events, events_played_today, room_where_events_played_already, calendar

        # Filter events that meet all criteria
        suitable_events = []
        
        for event in available_events:
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
        global available_interactions, ongoing_interaction
        if not available_interactions or interaction_to_run in available_interactions:
            ongoing_interaction = interaction_to_run
            renpy.call(interaction_to_run.game_label)
        else:
            renpy.say("", cdt_message )

    def end_interaction():
        global available_interactions, ongoing_interaction, interactions_played_today
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
            self.characters_shown = []

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
            self.relevant_itens = []
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

########################

    def game_skill_roll(skill, difficulty, skill_buffs = []):
        global skill_success, available_skill_buffs , used_skill_buffs
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        roll = dice1 + dice2 + dice3

        total = roll + skill.level

        sum_buffs = 0
        for buff in skill_buffs:
            if buff in available_skill_buffs :
                sum_buffs = sum_buffs + buff.value
                buff.times_used += 1
                if buff.limit <> 0 and buff.times_used >= buff.limit:
                    available_skill_buffs .remove(buff)
                    used_skill_buffs.append(buff)
        total = total + sum_buffs

        skill_success = total >= difficulty

        renpy.call("skill_test_label", total, difficulty, dice1, dice2, dice3, skill,skill_buffs )

##########################

    def add_skill_buff(skill_buff):
        global available_skill_buffs , used_skill_buffs
        if skill_buff not in available_skill_buffs  and skill_buff not in used_skill_buffs:
            available_skill_buffs .append(skill_buff)

##########################

    def rollchance(skill,difficulty,skill_buffs = []):
        global available_skill_buffs
        die_table = {
            "die_3" : 1,
            "die_4" : 0.9954,
            "die_5" : 0.9815,
            "die_6" : 0.9537,
            "die_7" : 0.9074,
            "die_8" : 0.8380,
            "die_9" : 0.7407,
            "die_10" : 0.6250,
            "die_11" : 0.5,
            "die_12" : 0.3750,
            "die_13" : 0.2593,
            "die_14" : 0.1620,
            "die_15" : 0.0926,
            "die_16" : 0.0463,
            "die_17" : 0.0185,
            "die_18" : 0.0046,
            "die_impossible" : 0
        }

        difficulty -= skill.level
        for buff in skill_buffs:
            if buff in available_skill_buffs:
                difficulty -= buff.value

        if difficulty <= 3:
            difficulty = 3
        if difficulty > 18:
            difficulty = "impossible"
        chance = die_table["die_%r" % difficulty]

        return round(chance*100)

##########################

    class skill_check_buff(store.object):
        def __init__(self, value , limit = 0):
            self.times_used = 0
            self.value = value
            self.limit = limit
        def GetName(self):
            return get_var_suffix(self, "loc")

##########################

    def chunk(lst, size):
        rt = []
        for i in range(0, len(lst), size):
            rt.append(lst[i:i+size])

        return rt

#########################

    def add_xp(quantity,reason):
        global player_xp, player_level, xp_progression, xp_progression
        player_xp += quantity
        next_level = player_level + 1
        if quantity >= 0:
            renpy.notify(f"{reason}{{color=#0adc28}}+{quantity}XP{{/color}}")
        else:
            renpy.notify(f"{reason}{{color=#dc2020}}-{quantity}XP{{/color}}")
        if next_level in xp_progression and player_xp >= xp_progression[next_level]:
            player_levelup()
            

########################

    def player_levelup():
        global player_level, player_xp, att_pts_available, level_up_loc, level_prefix
        player_xp -= xp_progression[player_level + 1]
        player_level += 1
        att_pts_available += 1
        renpy.notify(f"{level_up_loc}{{color=#0adc28}}{level_prefix}{player_level}{{/color}}")