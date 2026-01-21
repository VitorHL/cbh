
init offset = 0

default att_pts_available = 8 # Attribute points at start
default att_pts_spent = 0 # Attribute points at start
define att_pts_max_start = 4 # Maximum a skill can have at start

define game_level_max = 18 # Maximum level the player can get
define xp_per_skill_roll = 15 # Amount of xp the player gets per dice roll
define xp_per_skill_check = 10 # Amount of xp the player gets per choice/dialogue unlocked
define xp_per_item_shown = 5 # Amount of xp the player gets per (correct) items shown to characters

default player_level = 1
default player_xp = 0

define xp_progression = {
    2 : 100,
    3 : 125,
    4 : 175,
    5 : 225,
    6 : 275,
    7 : 325,
    8 : 425,
    9 : 475,
    10 : 475,
    11 : 525,
    12 : 575,
    13 : 625,
    14 : 675,
    15 : 725,
    16 : 775,
    17 : 825,
    18 : 875
}

default skill_inquiry = game_skill()
default skill_insight = game_skill()
default skill_lore = game_skill()
default skill_catharsis = game_skill()
default skill_volition = game_skill()
default skill_communion = game_skill()

default game_skills = [ skill_inquiry, skill_insight, skill_lore, skill_catharsis, skill_volition, skill_communion ]