init offset = -1

################################################################################
## Can't Go There Messages
################################################################################

# ATTENTION: Those two are extremely important, as the number of items in those lists are actually relevant for the calendar code, do not change the size of the list!

define weekdays_list = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
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
define skill_sentiment_loc = "sentiment"
define skill_resolve_loc = "resolve"
define skill_acuity_loc = "acuity"

define skill_inquiry_quote = "\"Judge a man by his questions rather than his answers.\""
define skill_inquiry_source = "Voltaire"
define skill_communion_quote = "\"No man is an island, entire of itself.\""
define skill_communion_source = "John Donne"
define skill_insight_quote = "\"The unexamined life is not worth living.\""
define skill_insight_source = "Socrates"
define skill_sentiment_quote = "\"The heart has its reasons which reason knows nothing of.\""
define skill_sentiment_source = "Blaise Pascal"
define skill_resolve_quote = "\"He who has a why to live can bear almost any how.\""
define skill_resolve_source = "Friedrich Nietzsche"
define skill_acuity_quote = "\"The question is not what you look at, but what you see.\""
define skill_acuity_source = "Henry David Thoreau"

define skill_inquiry_desc = "Inquiry governs your capacity to question individuals, concepts, and circumstances with precision and depth. A high level of inquiry enables you to probe beneath surface answers, uncover hidden truths, and extract valuable information through skillful interrogation."
define skill_communion_desc = "Communion governs your capacity to form meaningful connections and empathize with others. A high level of communion allows you to build trust quickly, understand unspoken feelings, and create bonds that transcend surface-level social interaction."
define skill_insight_desc = "Insight governs your ability to quickly form logical conclusions and understand complex situations. A high level of insight helps you grasp the underlying causes of events, recognize patterns others miss, and solve practical problems through clear reasoning and deduction."
define skill_sentiment_desc = "Sentiment governs your capacity for genuine feeling and emotional depth. A high level of sentiment makes you responsive to beauty, moved by suffering, and attuned to atmosphere, experiencing life with emotional authenticity rather than detachment or cynicism."
define skill_resolve_desc = "Resolve governs your capacity to commit to difficult paths and see them through despite opposition, cost, or doubt. High Resolve gives you the ability to stand firm against emotional or psychological distress. It enables you to remain committed to your goals and persevere despite obstacles or difficulties, preventing you from ever giving up."
define skill_acuity_desc = "Acuity governs the sharpness and precision of your observation. A high level of acuity allows you to notice fine details others overlook, catch subtle changes in your environment, and perceive the world with exceptional clarity and focus."

define skill_tag_dict = {
    "inquiry" : "INQ",
    "communion" : "COM",
    "insight" : "INS",
    "sentiment" : "SEN",
    "resolve" : "RES",
    "acuity" : "ACU"
}

define level_up_loc = "You levelled up to level [player_level]!"
define xp_gain_skill_test_loc = "SKILL ROLL:"
define xp_gain_skill_check_loc = "SKILL CHECK:"
define xp_gain_shown_item_loc = "SHOWN ITEM:"
define level_up_loc = "LEVEL UP:"
define level_prefix = "Lvl"

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
define address_room_edgar_diner = ["2847 Industrial Highway North", "Adjacent to Heartland Motors complex, visible from Highway 6"]
define address_room_church = ["200 Sacred Heart Street", "Old Town Neighborhood"]
define address_room_claire_house = ["Claire House"]
define address_room_cphpd = ["100 Municipal Plaza", "Downtown Government Center"]
define address_room_daniel_apartment = ["1156 Eastbrook Commons", "Eastern District"]
define address_room_forest_trail = ["Copperbell Hill State Forest", "Accessed via Forest Service Road 12"]
define address_room_gas_station = ["2845 Industrial Highway North", "Connected to Edgar's Diner", "Mile Marker 127"]
define address_room_gia_ranch = ["750 Horseshoe Ranch Road", "Rural Route 4","Northern Outskirts"]
define address_room_horse_track = ["500 Victory Boulevard", "Riverside Entertainment District"]
define address_room_library = ["75 Carnegie Avenue", "Historic Downtown District"]
define address_room_chao_bookstore = ["322 Huron Avenue", "Chinatown District"]

define location_room_edgar_diner = ["Edgar's Diner"]
define location_room_church = ["St. Peter Episcopal Church"]
define location_room_claire_house = ["Park Residency"]
define location_room_cphpd = ["Copperbell Hill Police Department"]
define location_room_daniel_apartment = ["Maple Grove Apartments", "Unit 3B"]
define location_room_forest_trail = ["Copperbell Hill State Forest"]
define location_room_gas_station = ["Highway Gas Station"]
define location_room_gia_ranch = ["Rossi Ranch"]
define location_room_horse_track = ["CPH Horse Track"]
define location_room_library = ["Copperbell Hill Public Library"]
define location_room_chao_bookstore = ["Jade Garden Books & Imports"]

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