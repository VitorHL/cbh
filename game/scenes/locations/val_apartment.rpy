
################################################################################
## Val's Apartment
################################################################################

label val_apartment_label:
    scene val_apartment_bg with fade
    call val_apartment_label_menu
label val_apartment_label_menu:
    call screen travel()
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
