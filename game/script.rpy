# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
default calendar = game_calendar(1,1,1,1997)
default cgt_message = cgt_default
default cdt_message = cdt_default
default avaliable_travels = [ room_gas_station, room_church, room_gia_ranch, room_daniel_apartment, room_val_apartment]


label start:
    #default calendar = game_calendar(1,1,1)

    $ avaliable_events = []
    $ finished_events = []
    $ events_played_today = []
    $ room_where_events_played_already = []
    $ avaliable_rooms = []
    $ avaliable_game_actions = []
    $ failed_missions = []
    $ failed_objectives = []
    $ completed_missions = []
    $ avaliable_missions = []

    $ cgt_message = cgt_default
    $ cdt_message = cdt_default

    $ current_room = room_edgar_counter

    show screen top_bar
    jump counter_label

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
    call daniel_apartment_label_menu
label daniel_apartment_label_menu:
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
    
