################################################################################
## CPHPD Hall
################################################################################

label cphpd_hall_label:
    scene cphpd_bg with fade
    call cphpd_hall_label_menu
label cphpd_hall_label_menu:
    call screen travel()
    call cphpd_hall_label_menu