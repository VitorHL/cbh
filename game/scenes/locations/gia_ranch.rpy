
################################################################################
## Gia's Mansion
################################################################################

label gia_mansion_label:
    scene gia_mansion_bg with fade
    call gia_mansion_label_menu
label gia_mansion_label_menu:
    call screen travel()
    call gia_mansion_label_menu

################################################################################
## Gia's Ranch
################################################################################

label gia_ranch_label:
    scene gia_ranch_bg with fade
    call gia_ranch_label_menu
label gia_ranch_label_menu:
    call screen travel()
    call gia_ranch_label_menu

################################################################################
## Gia's Stable
################################################################################

label gia_stable_label:
    scene gia_stable_bg with fade
    call gia_stable_label_menu
label gia_stable_label_menu:
    call screen travel()
    call gia_stable_label_menu

################################################################################
## Horse Track
################################################################################

label horse_track_label:
    scene horse_track_bg with fade
    call horse_track_label_menu
label horse_track_label_menu:
    call screen travel()
    call horse_track_label_menu