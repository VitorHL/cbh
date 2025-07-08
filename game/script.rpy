# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default calendar = game_calendar(5,9,10,1997)
default cgt_message = cgt_default
default cdt_message = cdt_default
default avaliable_travels = [ room_gas_station, room_church, room_gia_ranch, room_daniel_apartment, room_val_apartment]

default event1 = game_event( 1, "special_day", room_church )
default event2 = game_event( 1, "its_monday", room_church, weekday=1 )
default event3 = game_event( 1, "new_year", room_church, day = 30, month=11 )
default event4 = game_event( 2, "the_church_again", room_church )
default event_repeat = game_event( 1, "recurring_event", room_daniel_apartment, instances = 0)


default kitchen_interaction = game_interaction( "fridge_interaction" )







default avaliable_events = [ event1, event2, event3, event4, event_repeat ]
default finished_events = []
default events_played_today = []
default room_where_events_played_already = []
default avaliable_rooms = []
default avaliable_interactions = []
default interactions_played_today = []
default failed_missions = []
default failed_objectives = []
default completed_missions = []
default avaliable_missions = []


label start:
    #default calendar = game_calendar(1,1,1)

    $ current_room = room_edgar_counter

    show screen top_bar
    jump daniel_apartment_label

################################################################################
## Counter
################################################################################

label counter_label:
    scene edgar_diner_bg with fade
    call counter_label_menu

label counter_label_menu:
    menu:
        "Go to the Gas Station":
            $ move_room(room_gas_station)
    call counter_label_menu

################################################################################
## Church Hall
################################################################################

label church_label:
    scene church_bg with fade

    $ check_for_event()

    call church_label_menu

label church_label_menu:
    $ travel_menu( )
    call church_label_menu

################################################################################
## Storeroom
################################################################################

label storeroom_label:
    scene edgar_storeroom_bg with fade
    call storeroom_label_menu
label storeroom_label_menu:
    $ travel_menu( )
    call storeroom_label_menu

################################################################################
## CPHPD Hall
################################################################################

label cphpd_hall_label:
    scene cphpd_bg with fade
    call cphpd_hall_label_menu
label cphpd_hall_label_menu:
    $ travel_menu( )
    call cphpd_hall_label_menu

################################################################################
## Daniel's Apartment
################################################################################

label daniel_apartment_label:
    scene daniel_apartment_bg with fade
    $ check_for_event()
    call daniel_apartment_label_menu
label daniel_apartment_label_menu:
    menu:
        "Next Day":
            $ calendar.next_day()
        "Fridge":
            $ run_interaction(kitchen_interaction)
        "Travel":
            $ travel_menu( )
    call daniel_apartment_label_menu

################################################################################
## Forest Trail
################################################################################

label forest_trail_label:
    scene forest_bg with fade
    call forest_trail_label_menu
label forest_trail_label_menu:
    $ travel_menu( )
    call forest_trail_label_menu

################################################################################
## Gas Station
################################################################################

label gas_station_label:
    scene gas_station_bg with fade
    call gas_station_label_menu
label gas_station_label_menu:
    $ travel_menu( room_edgar_counter )
    call gas_station_label_menu

################################################################################
## Gia's Mansion
################################################################################

label gia_mansion_label:
    scene gia_mansion_bg with fade
    call gia_mansion_label_menu
label gia_mansion_label_menu:
    $ travel_menu( )
    call gia_mansion_label_menu

################################################################################
## Gia's Ranch
################################################################################

label gia_ranch_label:
    scene gia_ranch_bg with fade
    call gia_ranch_label_menu
label gia_ranch_label_menu:
    $ travel_menu( )
    call gia_ranch_label_menu

################################################################################
## Gia's Stable
################################################################################

label gia_stable_label:
    scene gia_stable_bg with fade
    call gia_stable_label_menu
label gia_stable_label_menu:
    $ travel_menu( )
    call gia_stable_label_menu

################################################################################
## Horse Track
################################################################################

label horse_track_label:
    scene horse_track_bg with fade
    call horse_track_label_menu
label horse_track_label_menu:
    $ travel_menu( )
    call horse_track_label_menu

################################################################################
## Library Hall
################################################################################

label library_hall_label:
    scene library_bg with fade
    call library_hall_label_menu
label library_hall_label_menu:
    $ travel_menu( )
    call library_hall_label_menu

################################################################################
## Val's Apartment
################################################################################

label val_apartment_label:
    scene val_apartment_bg with fade
    call val_apartment_label_menu
label val_apartment_label_menu:
    $ travel_menu( )
    call val_apartment_label_menu
    

label special_day():
    "This is a special day!"
    "Now continue coding!!!"
    $ end_event()

label its_monday():
    "It is Monday!"
    "Incredible"
    $ end_event()

label new_year():
    "Happy new year!"
    "2 years for y2k!"
    $ end_event()

label the_church_again():
    "The church again? why would i need to come here?"
    $ end_event()

label recurring_event():
    "This event ran [ongoing_event.runs] time(s)"
    if ongoing_event.runs > 10:
        "Over 10 times? Incredible"
    elif ongoing_event.runs > 20:
        "Over 20!?"
    $ end_event()

label fridge_interaction():
    if ongoing_interaction.runs_today > 0:
        "I ate today already"
        $ end_interaction()
    "Time for lunch..."
    "Hmm, burgar!"
    $ end_interaction()
         