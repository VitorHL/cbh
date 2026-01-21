################################################################################
## Church Hall
################################################################################

label church_label:
    scene church_bg with fade

    $ check_for_event()

    call church_label_menu

label church_label_menu:
    call screen travel()
    call church_label_menu