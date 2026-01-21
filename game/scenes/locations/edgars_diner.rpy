
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
## Storeroom
################################################################################

label storeroom_label:
    scene edgar_storeroom_bg with fade
    call storeroom_label_menu
label storeroom_label_menu:
    call screen travel()
    call storeroom_label_menu