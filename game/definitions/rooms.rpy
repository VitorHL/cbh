
init offset = 0

################################################################################
# Game Room Class Definition
# Navigation / Rooms Definitions
################################################################################
default available_rooms = [room_gas_station, room_church, room_gia_ranch, room_daniel_apartment, room_val_apartment, room_edgar_counter, room_edgar_kitchen, room_edgar_storeroom] # List of rooms the player can access
default available_travels = [] # List of rooms the player can travels to from current room

################################################################################
## Room Definitions
################################################################################

# Edgar's Diner Complex
define room_edgar_counter = game_room(
    game_label = "counter_label", 
    name = LOC_room_edgar_counter, 
    thumb = "gfx/interface/thumbnail_edgar_counter_bg.webp",
    address = address_room_edgar_diner, 
    location = location_room_edgar_diner,
    room_hub = True,
    room_travels = ["room_gas_station", "room_edgar_kitchen", "room_edgar_storeroom"]
)
define room_edgar_kitchen = game_room(
    game_label = "kitchen_label", 
    name = LOC_room_edgar_kitchen,
    thumb = "gfx/interface/thumbnail_edgar_kitchen_bg.webp",
    location = location_room_edgar_diner,
    room_travels = ["room_edgar_counter"]
)
define room_edgar_storeroom = game_room(
    game_label = "storeroom_label", 
    name = LOC_room_edgar_storeroom,
    thumb = "gfx/interface/thumbnail_edgar_storeroom_bg.webp",
    location = location_room_edgar_diner,
    room_travels = ["room_edgar_counter"]
)

# Gas Station
define room_gas_station = game_room(
    game_label = "gas_station_label", 
    name = LOC_room_gas_station,
    thumb = "gfx/interface/thumbnail_gas_station_bg.webp",
    address = address_room_gas_station, 
    location = location_room_gas_station,
)

# Church
define room_church = game_room(
    game_label = "church_label", 
    name = LOC_room_church, 
    thumb = "gfx/interface/thumbnail_church_bg.webp",
    address = address_room_church, 
    location = location_room_church,
    room_hub = True
)

# Police Department
define room_cphpd_hall = game_room(
    game_label = "cphpd_hall_label", 
    name = LOC_room_cphpd_hall, 
    thumb = "gfx/interface/thumbnail_cphpd_hall_bg.webp",
    address = address_room_cphpd, 
    location = location_room_cphpd,
    room_hub = True
)

# Daniel's Apartment
define room_daniel_apartment = game_room(
    game_label = "daniel_apartment_label", 
    name = LOC_room_daniel_apartment, 
    thumb = "gfx/interface/thumbnail_daniel_apartment_bg.webp",
    address = address_room_daniel_apartment, 
    location = location_room_daniel_apartment,
    room_hub = True
)

# Forest/Outskirts
define room_forest_trail = game_room(
    game_label = "forest_trail_label", 
    name = LOC_room_forest_trail,
    thumb = "gfx/interface/thumbnail_forest_trail_bg.webp", 
    address = address_room_forest_trail, 
    location = location_room_forest_trail,
    room_hub = True
)

# Gia's Properties
define room_gia_mansion = game_room(
    game_label = "gia_mansion_label", 
    name = LOC_room_gia_mansion,
    thumb = "gfx/interface/thumbnail_gia_mansion_bg.webp"
)
define room_gia_ranch = game_room(
    game_label = "gia_ranch_label", 
    name = LOC_room_gia_ranch, 
    thumb = "gfx/interface/thumbnail_gia_ranch_bg.webp",
    address = address_room_gia_ranch, 
    location = location_room_gia_ranch,
    room_hub = True,
    room_travels = ["room_gia_stable", "room_horse_track"]
)
define room_gia_stable = game_room(
    game_label = "gia_stable_label", 
    name = LOC_room_gia_stable,
    thumb = "gfx/interface/thumbnail_gia_stable_bg.webp",
)

# Horse Track
define room_horse_track = game_room(
    game_label = "horse_track_label", 
    name = LOC_room_horse_track, 
    thumb = "gfx/interface/thumbnail_horse_track_bg.webp",
    address = address_room_horse_track, 
    location = location_room_horse_track
)

# Library
define room_library_hall = game_room(
    game_label = "library_hall_label", 
    name = LOC_room_library_hall, 
    thumb = "gfx/interface/thumbnail_library_hall_bg.webp",
    address = address_room_library, 
    location = location_room_library
)

# Val's Apartment / Bookstore
define room_val_apartment = game_room(
    game_label = "val_apartment_label", 
    name = LOC_room_val_apartment, 
    thumb = "gfx/interface/thumbnail_val_apartment_bg.webp",
    #address = address_room_val_apartment, 
    location = location_room_library
)