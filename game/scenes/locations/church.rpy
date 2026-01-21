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