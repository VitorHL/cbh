# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters


define config.speaking_attribute = "talk"

# Game Lists -------------------------------------------------

default calendar = game_calendar(5,9,10,1997)
default cgt_message = cgt_default
default cdt_message = cdt_default

default available_skill_buffs = []
default used_skill_buffs = []

# Game Variables -------------------------------------------------

default clean_mode = True

default skill_success = False

image grain_effect:
    "gui/overlay/grain/grain_00.webp"
    pause 0.06
    "gui/overlay/grain/grain_01.webp"
    pause 0.06
    "gui/overlay/grain/grain_02.webp"
    pause 0.06
    "gui/overlay/grain/grain_03.webp"
    pause 0.06
    "gui/overlay/grain/grain_04.webp"
    pause 0.06
    "gui/overlay/grain/grain_05.webp"
    pause 0.06
    "gui/overlay/grain/grain_06.webp"   
    pause 0.06
    "gui/overlay/grain/grain_07.webp"
    pause 0.06
    "gui/overlay/grain/grain_08.webp"
    pause 0.06
    "gui/overlay/grain/grain_09.webp"
    pause 0.06
    repeat

label  before_main_menu:
    show grain_effect onlayer effect_overlay
    show image "gui/overlay/scanlines.webp" onlayer effect_overlay
return

label  after_load:
    # show image "gui/overlay/vignette.webp" onlayer vignette
    # show image "gui/overlay/scanlines.webp" onlayer effect_overlay
return

label start:
    $set_room( room_daniel_apartment )
    show screen vhs_overlay
    show image "gui/overlay/vignette.webp" onlayer vignette
    show image "gui/overlay/scanlines.webp" onlayer effect_overlay
    show grain_effect onlayer effect_overlay
    #show screen top_bar
    jump choose_mode_label

label choose_mode_label:
    scene edgar_diner_bg #with fade
    call screen start_choose_mode
    jump choose_mode_label

label start_skills:
    #scene edgar_diner_bg with fade
    call screen skill_screen_start   
    jump start_skills

label start_test_scenario:
    jump daniel_apartment_label

###################################################################################################################################################
# System Labels

label char_interaction(character):
    call screen character_interaction(character)
    return

label show_char_item(mode, character, selected_slot=None):
    # Calls the iventory screen to show item to character either in the interaction menu or mid conversation
    call screen inventory_screen(mode, character, selected_slot)
    # if mode == 1:
    #     call screen character_interaction(character)
    return



label char_item_reaction(item, mode, character, selected_slot):
    # Trigger the character reaction to the player showing a item
    if item in character.interested_items:
        if item in character.relevant_itens and character not in item.characters_shown:
            $ add_xp(xp_per_item_shown, xp_gain_shown_item_loc)
            $ item.characters_shown.append(character)
        $ renpy.call( character.interested_items[item], character )# call character.interested_items(item)
    else:
        #call character.generic _show_label
        $ renpy.call (character.generic_show_label, character)
    return
    



label char_conversation_list(character):
    # Generates a list of entries to the conversation tab
    $ generate_character_talks(character)
    return



label skill_test_label(total, difficulty, dice1, dice2, dice3, skill, skill_buffs=[]):
    show screen dice_roll_anim(total, difficulty, dice1, dice2, dice3, skill,skill_buffs)
    pause 1.5
    hide screen dice_roll_anim
    $ add_xp(xp_per_skill_roll,xp_gain_skill_test_loc)
    show screen dice_roll(total, difficulty, dice1, dice2, dice3, skill,skill_buffs)
    pause
    hide screen dice_roll
    return

###################################################################################################################################################
# Gia Interaction Labels

label char_gia_hello(character):
    "Hello, need something?"
    return

label char_gia_small_talk(character):
    show Claire front_shy happy
    Claire "Yes, that’s right shithead, you are being promoted, Congratulations!"
    Claire "Maybe with the immense responsibility I'm humbly entitling to you, you may start doing something useful with your miserable life."
    Daniel "R-really? B-but there are many people who have been working here for longer than me."
    show Claire front_shy
    Claire "Yes, and they are all even more useless than you, can you believe it?"
    Claire "It leaves me with no choice but to let you manage those rascals."
    Claire "It was either you or the crackhead marine."
    Daniel "Blackwood?"
    show Claire front_shy mad
    Claire "No you idiot, I meant Colin Powell.– Of course it is Blackwood moron!"
    show Claire front_shy
    Daniel "He wasn’t a marine, I believe he served in the army sir."
    Daniel "And I’m pretty sure General Powell’s Branch is the Army too..."
    show Claire front_shy mad
    Claire "Does it make any difference?"
    Claire "The nut job gives me some McVeigh vibes, I have the feeling that this nazi-ass will eventually bomb the diner just to kill the boredom."
    Claire "Now it is your job to guarantee that he will not do that by the way."
    Claire "If he ever serves the ‘Hiroshima special’ and blow-up the place the repairs were going to go out of your pocket, I’m clear?"
    show Claire front_shy
    Daniel "Gulp... Yes sir."
    call screen character_interaction(character)
    return

label char_gia_talk_val(character):
    $ add_skill_buff(talked_about_val)
    "Val? What about her?"
    "Can't really say i care much about her at all"
    "You two are a nice couple though..."
    call char_conversation_list(character)
    return

label char_gia_talk_building(character):
    "Yes, it was me who bought the building besides the highway"
    "No i will not ellaborate"
    "Only thing i will say is that it will be nice to be neighbours"
    call char_conversation_list(character)
    return

label char_gia_talk_relationship(character):
    "It is over Daniel... There is nothing you can do to reapair the things now."
    "Maybe we can talk about it later, but not really now."
    menu:
        "I want to still discuss it though." (skill_roll=[skill_sentiment,18,[showed_burguer,showed_coke,talked_about_val]]):
            if skill_success == True:
                "The test was a success"
                "Victory!"
                "She is not coming back though"
            else:
                "This is what should be shown"
                "The text continues"
                "Etc"
    call char_conversation_list(character)
    return



label gia_show_generic(character):
    "..."
    "Why are you showing me this?"
    "Can't really say much about it."
    call show_char_item(mode,character,selected_slot)
    return

label gia_show_coke(character):
    $ add_skill_buff(showed_coke)
    "Coke?"
    "No thanks, this thing have way too much sugar."
    call show_char_item(mode,character,selected_slot)
    return

label gia_show_burger(character):
    $ add_skill_buff(showed_burguer)
    "Oh sorry, no i'm not hungry"
    "Besides, i would prefer to be hit by a car than eating something from your Diner."
    call show_char_item(mode,character,selected_slot)
    return
