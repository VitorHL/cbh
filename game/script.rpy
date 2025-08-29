# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Game Events -------------------------------------------------

default event1 = game_event( 1, "special_day", room_church )
default event2 = game_event( 1, "its_monday", room_church, weekday=1 )
default event3 = game_event( 1, "new_year", room_church, day = 30, month=11 )
default event4 = game_event( 2, "the_church_again", room_church )
default event_repeat = game_event( 1, "recurring_event", room_daniel_apartment, instances = 0)

# Game Itens -------------------------------------------------

default burgar = game_item("burgar", "Hamburgar", "Hamburgar, delicious!", "burgar_interaction" )
default fries = game_item("fries", "Freedom_Fries", "Take that frenchies, those are FREEDOM fries!", "fries_interaction" )
default coke = game_item("coke", "Coca-cola", "Cokey-cola!", "coke_interaction")

# Game Characters -------------------------------------------------

default char_gia = game_character( "Gianna \"GIA\" Rossi", "char_gia_hello", "char_gia_small_talk", "gia_show_generic" )

# Game Interactions -------------------------------------------------

default kitchen_interaction = game_interaction( "fridge_interaction" )

# Game Lists -------------------------------------------------

default game_iventory = [ burgar, fries, coke ]
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

default calendar = game_calendar(5,9,10,1997)
default cgt_message = cgt_default
default cdt_message = cdt_default
default avaliable_travels = [ room_gas_station, room_church, room_gia_ranch, room_daniel_apartment, room_val_apartment]

# Game Variables -------------------------------------------------

default clean_mode = True

default skill_success = False

default att_pts_avaliable = 8 # Attribute points at start
default att_pts_spent = 0 # Attribute points at start
define att_pts_max_start = 4 # Maximum a skill can have at start

define game_level_max = 18 # Maximum level the player can get
define xp_per_check = 10 # Amount of xp the player gets per dice roll
define xp_per_unlock = 5 # Amount of xp the player gets per choice/dialogue unlocked



default skill_inquiry = game_skill()
default skill_insight = game_skill()
default skill_lore = game_skill()
default skill_catharsis = game_skill()
default skill_volition = game_skill()
default skill_communion = game_skill()

default game_skills = [ skill_inquiry, skill_insight, skill_lore, skill_catharsis, skill_volition, skill_communion ]









label skill_test_label(total, difficulty, dice1, dice2, dice3, skill):
    show screen dice_roll_anim(total, difficulty, dice1, dice2, dice3, skill)
    # show screen dice_roll_fake_0()
    # show screen dice_roll_fake_1()
    # show screen dice_roll_fake_2()
    # show screen dice_roll_result_fake(skill)
    pause 1
    #hide screen dice_roll_anim
    hide screen dice_roll_anim
    show screen dice_roll(total, difficulty, dice1, dice2, dice3, skill)
    # hide screen dice_roll_fake_0
    # hide screen dice_roll_fake_1
    # hide screen dice_roll_fake_2
    # hide screen dice_roll_result_fake
    # show screen dice_roll_0(dice1, difficulty)
    # show screen dice_roll_1(dice2, difficulty)
    # show screen dice_roll_2(dice3, difficulty)
    # show screen dice_roll_result(skill, dice1, dice2, dice3)
    
    pause
    hide screen dice_roll
    # hide screen dice_roll_0
    # hide screen dice_roll_1
    # hide screen dice_roll_2
    # hide screen dice_roll_result
    return

































label start:
    #default calendar = game_calendar(1,1,1)

    $ current_room = room_edgar_counter

    show screen top_bar
    jump choose_mode_label

label choose_mode_label:
    scene edgar_diner_bg #with fade
    call screen start_choose_mode
    jump choose_mode_label

label start_skills:
    #scene edgar_diner_bg with fade
    call screen skill_screen_start   
    jump start_skills


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

    # $ char_gia.add_item_reaction( burgar, "gia_show_burger" )
    # $ char_gia.add_item_reaction( coke, "gia_show_coke" )
    # $ char_gia.add_talk( "Relationship", "char_gia_talk_relationship" )
    # $ char_gia.add_talk( "Val", "char_gia_talk_val" )
    # $ char_gia.add_talk( "The Building", "char_gia_talk_building" )

    $ char_gia.interested_items[burgar] = "gia_show_burger"
    $ char_gia.interested_items[coke] = "gia_show_coke"
    $ char_gia.interested_talks["Relationship"] = "char_gia_talk_relationship"
    $ char_gia.interested_talks["The Building"] = "char_gia_talk_building"
    $ char_gia.interested_talks["Val"] = "char_gia_talk_val"


    scene daniel_apartment_bg with fade
    call screen character_interaction(char_gia)
    $ check_for_event()
    call daniel_apartment_label_menu
label daniel_apartment_label_menu:
    menu:
        "Talk with someone":
            menu:
                "About the milkshake sack..." (skill_check=[skill_inquiry,10]):
                    "Ok"
                "I don't know much about the boss either." (skill_roll=[skill_communion,14]):
                    #$ skill_check(skill_communion, 14)
                    #show screen dice_roll(1,1)
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "I don't have time for it, just say where you left it." (skill_roll=[skill_catharsis,14]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "I would prefer to not say my reasons." (skill_roll=[skill_lore,5]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "Hey, don't speak about Val like that!" (skill_roll=[skill_inquiry,18]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
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
         

label burgar_interaction():
    "This is a burger"
    "And it is (probably) delicious!"
    call screen inventory_screen
    return

label fries_interaction():
    "In 6 years those will become the epicenter of a geopolitical mini-crisis"
    "I hope Saddam Hussein may have some ketchup..."
    call screen inventory_screen
    return

label coke_interaction():
    "Did you know those things had cocaine in its original formula?"
    "Impressive, heh?"
    call screen inventory_screen
    return


###################################################################################################################################################
# System Labels

label char_interaction(character):
    call screen character_interaction(character)
    return

label show_char_item(mode, character, selected_slot=None):
    # Calls the iventory screen to show item to character either in the interaction menu or mid conversation
    call screen inventory_screen(mode, character, selected_slot)
    # if mode == 1:
    #     call screen character_interaction(character)
    return

label char_item_reaction(item, mode, character, selected_slot):
    # Trigger the character reaction to the player showing a item
    if item in character.interested_items:
        $ renpy.call( character.interested_items[item], character )# call character.interested_items(item)
    else:
        #call character.generic _show_label
        $ renpy.call (character.generic_show_label, character)
    #"Amongi"
    return


label char_conversation_list(character):
    # Generates a list of entries to the conversation tab
    $ generate_character_talks(character)
    return

###################################################################################################################################################
# Gia Interaction Labels

label char_gia_hello(character):
    "Hello, need something?"
    return

label char_gia_small_talk(character):
    "I think the climate is very nice today"
    "Don't you think?"
    call screen character_interaction(character)
    return

label char_gia_talk_val(character):
    "Val? What about her?"
    "Can't really say i care much about her at all"
    "You two are a nice couple though..."
    call char_conversation_list(character)
    return

label char_gia_talk_building(character):
    "Yes, it was me who bought the building besides the highway"
    "No i will not ellaborate"
    "Only thing i will say is that it will be nice to be neighbours"
    call char_conversation_list(character)
    return

label char_gia_talk_relationship(character):
    "It is over Daniel... There is nothing you can do to reapair the things now."
    "Maybe we can talk about it later, but not really now."
    call char_conversation_list(character)
    return



label gia_show_generic(character):
    "..."
    "Why are you showing me this?"
    "Can't really say much about it."
    call show_char_item(mode,character,selected_slot)
    return

label gia_show_coke(character):
    "Coke?"
    "No thanks, this thing have way too much sugar."
    call show_char_item(mode,character,selected_slot)
    return

label gia_show_burger(character):
    "Oh sorry, no i'm not hungry"
    "Besides, i would prefer to be hit by a car than eating something from your Diner."
    call show_char_item(mode,character,selected_slot)
    return
