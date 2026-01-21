

# Claire -------------------------------------------------------------------------------

define Claire = Character(
    "CLAIRE", 
    color="#3962af",
    namebox_background=Transform(
        Frame("gui/tiles/black_tile_border_recolor.webp", 20, 20),
        matrixcolor=TintMatrix("#3962af")
    ),
    callback=callback_builder("Claire")
)

image Claire front_shy:
    block:
        "GFX/characters/claire/standard/front_shy/0_0.webp"
        pause renpy.random.uniform(2.0, 3.0)
        "GFX/characters/claire/standard/front_shy/0_0_1.webp"
        pause 0.1
        "GFX/characters/claire/standard/front_shy/0_0_2.webp"
        pause 0.1
        "GFX/characters/claire/standard/front_shy/0_0_1.webp"
        pause 0.1
    repeat

image Claire front_shy talk:
    "GFX/characters/claire/standard/front_shy/0_1.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/0_0.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/0_2.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/0_0.webp"
    pause 0.10
    repeat

image Claire front_shy happy:
    block:
        "GFX/characters/claire/standard/front_shy/1_0.webp"
        pause renpy.random.uniform(2.0, 3.0)
        "GFX/characters/claire/standard/front_shy/1_0_1.webp"
        pause 0.1
        "GFX/characters/claire/standard/front_shy/1_0_2.webp"
        pause 0.1
        "GFX/characters/claire/standard/front_shy/1_0_1.webp"
        pause 0.1
    repeat

image Claire front_shy happy talk:
    "GFX/characters/claire/standard/front_shy/1_1.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/1_0.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/1_2.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/1_0.webp"
    pause 0.10
    repeat

image Claire front_shy mad:
        "GFX/characters/claire/standard/front_shy/2_0.webp"

image Claire front_shy mad talk:
    "GFX/characters/claire/standard/front_shy/2_1.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/2_0.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/2_2.webp"
    pause 0.10
    "GFX/characters/claire/standard/front_shy/2_0.webp"
    pause 0.10
    repeat