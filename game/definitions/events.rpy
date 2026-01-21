
init offset = 1 # Set offset to 1 to ensure this init block runs after room definitions

default available_events = []
default finished_events = []
default events_played_today = []
default room_where_events_played_already = []

# Game Events -------------------------------------------------

default event1 = game_event( 1, "special_day", room_church )
default event2 = game_event( 1, "its_monday", room_church, weekday=1 )
default event3 = game_event( 1, "new_year", room_church, day = 30, month=11 )
default event4 = game_event( 2, "the_church_again", room_church )
default event_repeat = game_event( 1, "recurring_event", room_daniel_apartment, instances = 0)