
init offset = 0

# The Game inventlry list itself

default game_inventory = [ ]

#################################################################
# Game Itens
#################################################################

default burgar = game_item(
    icon = "gui/items/burgar.webp",
    name = "Cold Hamburguer",
    desc = "A cold hamburguer left on the fridge overnight, looks eadible.",
    interaction_game_label = "burgar_interaction",
    huge_icon = "rotating_burgar"
)

default fries = game_item(
    icon = "gui/items/fries.webp",
    name = "French Fries",
    desc = "A pack of fast-food french fries, salty and crunchy.",
    interaction_game_label = "fries_interaction",
    huge_icon = "rotating_fries"
)

default coke = game_item(
    icon = "gui/items/coke.webp",
    name = "POP-Cola can",
    desc = "A can of fresh and cold POP-Cola.",
    interaction_game_label = "coke_interaction",
    huge_icon = "rotating_coke"
)

# Test scenario items

default polaroid_photo = game_item(
    icon = "gui/items/polaroid.webp",
    name = "Strange Polaroid",
    desc = "A polaroid Val gave you. The image shows the old Heartland Motors building at night, but there's something wrong with the shadows. They seem to bend toward the camera.",
    interaction_game_label = "inspect_polaroid",
    huge_icon = "rotating_polaroid"
)

default coffee_thermos = game_item(
    icon = "gui/items/thermos.webp", 
    name = "Claire's Thermos",
    desc = "A dented police-issue thermos. Claire left it here last week. You keep meaning to return it, but she keeps forgetting to pick it up. The coffee inside has long since gone cold.",
    interaction_game_label = "inspect_thermos",
    huge_icon = "rotating_thermos"
)

default cassette_tape = game_item(
    icon = "gui/items/cassette.webp",
    name = "Unlabeled Cassette",
    desc = "Val's recording of the strange broadcast. She insists you need to hear it, but warns you not to listen alone. The tape is slightly warped, as if exposed to heat.",
    interaction_game_label = "inspect_cassette",
    huge_icon = "rotating_cassette"
)