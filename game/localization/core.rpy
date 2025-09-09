init offset = -1

################################################################################
## Can't Go There Messages
################################################################################

# ATTENTION: Those two are extremely important, as the number of items in those lists are actually relevant for the calendar code, do not change the size of the list!

define weekdays_list = [ "Sunday", "Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday" ]
define months_list = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

################################################################################
## Can't Go There Messages
################################################################################

define cgt_default = "Better stay in my way, i need to do something else right now."

################################################################################
## Can't do That Messages
################################################################################

define cdt_default = "Can't do that right now, i need to do something else."

################################################################################
## Game Skills
################################################################################

define skill_inquiry_loc = "inquiry"
define skill_communion_loc = "communion"
define skill_insight_loc = "insight"
define skill_catharsis_loc = "catharsis"
define skill_volition_loc = "volition"
define skill_lore_loc = "lore"

define skill_inquiry_quote = "\"Judge a man by his questions rather than his answers.\"\n\n- Voltaire -"
define skill_communion_quote = "\"No man is an island, entire of itself.\"\n\n- John Donne -"
define skill_insight_quote = "\"The unexamined life is not worth living.\"\n\n- Socrates -"
define skill_catharsis_quote = "\"The wound is the place where the Light enters you.\"\n\n- Rumi -"
define skill_volition_quote = "\"He who has a why to live can bear almost any how.\"\n\n- Friedrich Nietzsche -"
define skill_lore_quote = "\"The past is never dead. It's not even past.\"\n\n- William Faulkner -"

define skill_inquiry_desc = "Inquiry governs your capacity to question individuals, concepts, and circumstances with precision and depth. A high level of inquiry enables you to probe beneath surface answers, uncover hidden truths, and extract valuable information through skillful interrogation."
define skill_communion_desc = "Communion governs your capacity to form meaningful connections and empathize with others. A high level of communion allows you to build trust quickly, understand unspoken feelings, and create bonds that transcend surface-level social interaction."
define skill_insight_desc = "Insight governs your ability to quickly form logical conclusions and understand complex situations. A high level of insight helps you grasp the underlying causes of events, recognize patterns others miss, and solve practical problems through clear reasoning and deduction."
define skill_catharsis_desc = "Catharsis governs your ability to understand and process complex emotions, both your own and others'. A high level of catharsis helps you navigate emotional turmoil with wisdom, find healing through acceptance, and offer genuine comfort to those in distress."
define skill_volition_desc = "Volition governs your willpower and mental fortitude in the face of adversity. A high level of volition enables you to maintain composure under extreme pressure, resist psychological manipulation, and push through situations that would break weaker minds."
define skill_lore_desc = "Lore governs your accumulated knowledge of history, culture, and forgotten wisdom. A high level of lore allows you to recall obscure details about past events, understand ancient mysteries, and draw upon deep wells of traditional knowledge."

define skill_tag_dict = {
    "inquiry" : "INQ",
    "communion" : "COM",
    "insight" : "INS",
    "catharsis" : "CAT",
    "volition" : "VOL",
    "lore" : "LOR"
}

define level_up_loc = "You levelled up to level [player_level]!"
define xp_gain_skill_test_loc = "SKILL ROLL:"
define xp_gain_skill_check_loc = "SKILL CHECK:"
define xp_gain_shown_item_loc = "SHOWN ITEM:"

################################################################################
## Game Menus
################################################################################

define showed_burguer_loc = "Showed Burguer"
define showed_coke_loc = "Showed Coke"
define talked_about_val_loc = "Talked about Val"

################################################################################
## Game Menus
################################################################################

define loc_clean_mode = "Clean Mode"
define loc_horny_mode = "Explicit Mode"
define loc_clean_mode_desc = "Clean Mode skips all explicit sex scenes. While the story and text remain unchanged, and adult themes are still mentioned, no depictions of sexual actions, whether visual or textual, are shown."
define loc_horny_mode_desc = "Explicit mode displays all sex scenes. The narrative remains consistent with clean mode; only the depiction of sexual content differs."
define loc_game_mode_psa = "Please note: This selection has no bearing on mature content that is not sexual in nature."

define loc_continue = "Continue >"
define loc_yes = "Yes" 
define loc_no = "No"
define loc_are_you_sure = "Are you Sure?"

################################################################################
## Places
################################################################################

# Planes
# Planes are not classes, they are only strings set in this page.
define plane_real_world = "Mortal World"


# Regions
# Regions are not classes, they are only strings set in this page.
define region_cph_downtown = "Downton"
define region_cph_industrial_zone = "Industrial Zone"
define region_cph_outskirts = "City Outskirts"
define region_forest = "Forest"

# locations
# locations are not classes, they are only strings set in this page.
define address_room_edgar_diner = "2847 Industrial Highway North\nAdjacent to Heartland Motors complex, visible from Highway 6"
define address_room_church = "200 Sacred Heart Street\nOld Town Neighborhood"
define address_room_claire_house = "Claire House"
define address_room_cphpd = "100 Municipal Plaza\nDowntown Government Center"
define address_room_daniel_apartment = "1156 Eastbrook Commons\nEastern District"
define address_room_forest_trail = "Copperbell Hill State Forest\nAccessed via Forest Service Road 12"
define address_room_gas_station = "2845 Industrial Highway North\nConnected to Edgar's Diner, Mile Marker 127"
define address_room_gia_ranch = "750 Horseshoe Ranch Road\nRural Route 4, Northern Outskirts"
define address_room_horse_track = "500 Victory Boulevard\nRiverside Entertainment District"
define address_room_library = "75 Carnegie Avenue\nHistoric Downtown District"
define address_room_chao_bookstore = "322 Huron Avenue\nChinatown District"

define location_room_edgar_diner = "Edgar's Diner"
define location_room_church = "St. Peter Episcopal Church"
define location_room_claire_house = "Park Residency"
define location_room_cphpd = "Copperbell Hill Police Department"
define location_room_daniel_apartment = "Maple Grove Apartments, Unit 3B"
define location_room_forest_trail = "Copperbell Hill State Forest"
define location_room_gas_station = "Highway Gas Station"
define location_room_gia_ranch = "Rossi Ranch"
define location_room_horse_track = "CPH Horse Track"
define location_room_library = "Copperbell Hill Public Library"
define location_room_chao_bookstore = "Jade Garden Books & Imports"

#Rooms
define LOC_room_edgar_counter = "Roadside Diner"
define LOC_room_edgar_kitchen = "Kitchen"
define LOC_room_edgar_storeroom = "Storeroom"
define LOC_room_church = "Old Town Church"
define LOC_room_cphpd_hall = "Police Department"
define LOC_room_daniel_apartment = "Daniel's Apartment"
define LOC_room_forest_trail = "Forest Trail"
define LOC_room_gas_station = "Gas Station"
define LOC_room_gia_mansion = "Gia's Mansion"
define LOC_room_gia_ranch = "Gia's Ranch"
define LOC_room_gia_stable = "Gia's Stable"
define LOC_room_horse_track = "Horse Track"
define LOC_room_library_hall = "Municipal Library"
define LOC_room_val_apartment = "Bookstore"