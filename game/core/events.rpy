
init python:

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