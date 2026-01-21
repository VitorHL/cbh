

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

##########################

    def chunk(lst, size):
        rt = []
        for i in range(0, len(lst), size):
            rt.append(lst[i:i+size])

        return rt