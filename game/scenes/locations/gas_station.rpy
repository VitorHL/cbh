

################################################################################
## Gas Station
################################################################################

label gas_station_label:
    scene gas_station_bg with fade
    call gas_station_label_menu
label gas_station_label_menu:
    $ travel_menu( room_edgar_counter )
    call gas_station_label_menu