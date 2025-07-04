init python:
    # Importing Important Stuff
    import renpy.store as store
    import renpy.exports as renpy

    class game_calendar(store.object):
        def __init__(self,weekday,month,day,year):
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
            self.day += 1
            
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
        def __init__(self, game_label, name = None, address = None):
            self.name = name
            self.game_label = game_label
            self.address = address
    
    def move_room(to_where):
        global current_room
        global cgt_message
        if not avaliable_rooms or to_where in avaliable_rooms:
            current_room = to_where
            renpy.jump(to_where.game_label)
        else:
            renpy.say("", cgt_message )

######################################################################################################################################

    def get_var_name(var, scope):
        return [name for name in scope if scope[name] is var]

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
                var_address = room.address
                menu_list.append((room.name, renpy.Choice(room, room_thumb=var_name, room_address=room.address) ))
        
        # Add items from avaliable_travels, excluding current_room
        for room in avaliable_travels:
            if room != current_room:
                var_name = get_var_name(room, globals())[0]
                var_address = room.address
                menu_list.append( (room.name, renpy.Choice(room, room_thumb=var_name, room_address=room.address) ) )
        
        # Display the menu with the processed list
        room = renpy.display_menu(menu_list, "" , True, screen='travel'  )
        move_room(room)


    