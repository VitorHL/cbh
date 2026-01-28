
init offset = 0

default att_pts_available = 7 # Attribute points at start
default att_pts_spent = 0 # Attribute points at start
define att_pts_max_start = 4 # Maximum a skill can have at start
define att_pts_max = 8 # Skill cap for the whole game

define game_level_max = 16 # Maximum level the player can get
define xp_per_skill_roll = 15 # Amount of xp the player gets per dice roll
define xp_per_skill_check = 10 # Amount of xp the player gets per choice/dialogue unlocked
define xp_per_item_shown = 5 # Amount of xp the player gets per (correct) items shown to characters

default player_level = 1
default player_xp = 0

define xp_progression = {
    2 : 125,
    3 : 175,
    4 : 225,
    5 : 300,
    6 : 375,
    7 : 475,
    8 : 575,
    9 : 675,
    10 : 800,
    11 : 925,
    12 : 1050,
    13 : 1175,
    14 : 1325,
    15 : 1475,
    16 : 1625
}

default skill_inquiry = game_skill()
default skill_insight = game_skill()
default skill_acuity = game_skill()
default skill_sentiment = game_skill()
default skill_resolve = game_skill()
default skill_communion = game_skill()

default game_skills = [ skill_inquiry, skill_insight, skill_acuity, skill_sentiment, skill_resolve, skill_communion ]