
init offset = 0

# Karol --------------------------------------------------------------------------------

define Karol = Character(
    "KAROLINA", 
    color="#8521b3",
    namebox_background=Transform(
        Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20),
        matrixcolor=TintMatrix("#8521b3")
    ),
    #callback=callback_builder("Karol")
)