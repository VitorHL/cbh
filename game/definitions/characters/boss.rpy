
init offset = 0

# Boss --------------------------------------------------------------------------------

define Boss = Character(
    "BOSS", 
    color="#b34f21",
    namebox_background=Transform(
        Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20),
        matrixcolor=TintMatrix("#b34f21")
    ),
    #callback=callback_builder("Boss")
)