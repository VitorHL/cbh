
init offset = 0

# Val --------------------------------------------------------------------------------

define Val = Character(
    "VALERIE", 
    color="#21b32d",
    namebox_background=Transform(
        Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20),
        matrixcolor=TintMatrix("#21b32d")
    ),
    #callback=callback_builder("Val")
)