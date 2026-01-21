
################################################################################
## Forest Trail
################################################################################

label forest_trail_label:
    scene forest_bg with fade
    call forest_trail_label_menu
label forest_trail_label_menu:
    $ travel_menu( )
    call forest_trail_label_menu