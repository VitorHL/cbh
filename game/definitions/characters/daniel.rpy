
init offset = 0

# Daniel ----------------------------------------------------------------------------

define Daniel = Character(
    "DANIEL", 
    color="#21b393",
    namebox_background=Transform(
        Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20),
        matrixcolor=TintMatrix("#21b393")
    ),
    #callback=callback_builder("Daniel")
)