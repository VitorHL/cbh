################################################################################
## CPHPD Hall
################################################################################

label cphpd_hall_label:
    scene cphpd_bg with fade
    call cphpd_hall_label_menu
label cphpd_hall_label_menu:
    $ travel_menu( )
    call cphpd_hall_label_menu