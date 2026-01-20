
init offset = 0

# Gia -------------------------------------------------------------------------------
define Gia = Character("GIANNA", color="#b32137", namebox_background="gia_namebox", callback=callback_builder("Gia"))
image gia_namebox:
    Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20)
    matrixcolor TintMatrix("#b32137")

image Gia front:
    "GFX/characters/gia/standard/front_stare_cigarrette/0_0.webp"

image Gia front talk:
    "GFX/characters/gia/standard/front_stare_cigarrette/0_1.webp"
    pause 0.10
    "GFX/characters/gia/standard/front_stare_cigarrette/0_0.webp"
    pause 0.10
    "GFX/characters/gia/standard/front_stare_cigarrette/0_2.webp"
    pause 0.10
    "GFX/characters/gia/standard/front_stare_cigarrette/0_0.webp"
    pause 0.10
    repeat

#Char system

default char_gia = game_character( "Gianna \"GIA\" Rossi", "char_gia_hello", "char_gia_small_talk", "gia_show_generic" )