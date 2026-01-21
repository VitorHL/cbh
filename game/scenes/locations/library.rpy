

################################################################################
## Library Hall
################################################################################

label library_hall_label:
    scene library_bg with fade
    call library_hall_label_menu
label library_hall_label_menu:
    call screen travel()
    call library_hall_label_menu