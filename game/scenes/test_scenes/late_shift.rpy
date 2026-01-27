# game/scenes/test_scenario/late_shift.rpy

################################################################################
## TEST SCENARIO: The Late Shift
## A comprehensive feature test disguised as narrative gameplay
################################################################################

#=============================================================================
# ITEMS FOR THIS SCENARIO
#=============================================================================

default polaroid_photo = game_item(
    "gui/items/polaroid.webp",
    "Strange Polaroid",
    "A polaroid Val gave you. The image shows the old Heartland Motors building at night, but there's something wrong with the shadows. They seem to bend toward the camera.",
    "inspect_polaroid"
)

default coffee_thermos = game_item(
    "gui/items/thermos.webp", 
    "Claire's Thermos",
    "A dented police-issue thermos. Claire left it here last week. You keep meaning to return it, but she keeps forgetting to pick it up. The coffee inside has long since gone cold.",
    "inspect_thermos"
)

default cassette_tape = game_item(
    "gui/items/cassette.webp",
    "Unlabeled Cassette",
    "Val's recording of the strange broadcast. She insists you need to hear it, but warns you not to listen alone. The tape is slightly warped, as if exposed to heat.",
    "inspect_cassette"
)

#=============================================================================
# SKILL BUFFS FOR THIS SCENARIO  
#=============================================================================

default buff_coffee_offered = skill_check_buff(1)
define buff_coffee_offered_loc = "Offered Claire's Thermos"

default buff_listened_to_val = skill_check_buff(2)
define buff_listened_to_val_loc = "Listened to Val's Theory"

default buff_shared_concern = skill_check_buff(1)
define buff_shared_concern_loc = "Shared Concern for Claire"

default buff_noticed_matt = skill_check_buff(-1)
define buff_noticed_matt_loc = "Matt is Watching"

#=============================================================================
# EVENTS FOR THIS SCENARIO
#=============================================================================

default event_late_shift_start = game_event(
    1, 
    "late_shift_intro",
    room_edgar_counter,
    instances=1
)

default event_kitchen_discovery = game_event(
    1,
    "kitchen_strange_noise", 
    room_edgar_kitchen,
    instances=1
)

default event_boss_call = game_event(
    2,
    "boss_evening_call",
    room_edgar_counter,
    instances=1
)

#=============================================================================
# CHARACTER SETUP FOR CLAIRE (expanded for testing)
#=============================================================================

default char_claire = game_character(
    "Claire J. Park",
    "char_claire_hello",
    "char_claire_small_talk", 
    "claire_show_generic"
)

#=============================================================================
# MAIN SCENARIO LABEL
#=============================================================================

label test_scenario_setup:
    # Setup game state for testing
    $ calendar = game_calendar(5, 9, 10, 1997)  # Saturday, September 10, 1997
    $ set_room(room_edgar_counter)
    
    # Add items to inventory
    $ game_iventory.append(polaroid_photo)
    $ game_iventory.append(coffee_thermos)
    
    # Setup Claire's interaction data
    $ char_claire.interested_items[coffee_thermos] = "claire_shown_thermos"
    $ char_claire.interested_items[polaroid_photo] = "claire_shown_polaroid"
    $ char_claire.relevant_itens.append(coffee_thermos)
    
    $ char_claire.interested_talks["The Patrol"] = "claire_talk_patrol"
    $ char_claire.interested_talks["Matt"] = "claire_talk_matt"
    $ char_claire.interested_talks["Us"] = "claire_talk_relationship"
    
    # Add events to available pool
    $ available_events.append(event_late_shift_start)
    $ available_events.append(event_kitchen_discovery)
    $ available_events.append(event_boss_call)
    
    # Show overlays
    show screen vhs_overlay
    show image "gui/overlay/vignette.webp" onlayer vignette
    show grain_effect onlayer effect_overlay
    
    jump edgar_counter_test

#=============================================================================
# DINER COUNTER - MAIN HUB
#=============================================================================

label edgar_counter_test:
    scene edgar_diner_bg with fade
    $ set_room(room_edgar_counter)
    
    # Check for events (should trigger late_shift_intro first time)
    $ check_for_event()
    
    call edgar_counter_menu

label edgar_counter_menu:
    menu:
        "Look around the diner":
            "The fluorescent lights buzz overhead, casting everything in that particular shade of institutional yellow."
            "A few truckers nurse their coffees in the corner booth. The radio crackles with static between songs."
            "Through the window, you can see the gas pumps and beyond them, the dark silhouette of the old Heartland Motors building."
            call edgar_counter_menu
            
        "Check the clock":
            $ hours = "10" if calendar.weekday < 5 else "11"
            "The clock above the pie case reads [hours]:47 PM."
            "Still a few hours until close. Unless the Boss calls with one of his 'special requests.'"
            call edgar_counter_menu
            
        "Head to the kitchen":
            $ move_room(room_edgar_kitchen)
            
        "Go outside to the gas station":
            $ move_room(room_gas_station)
            
        "Wait for something to happen" if not event_late_shift_start in finished_events:
            "You lean against the counter, watching the door."
            "The bell above it jingles."
            jump late_shift_intro
            
        "Travel somewhere else" (important=True):
            call screen travel()
            
    call edgar_counter_menu

#=============================================================================
# OPENING EVENT: The Late Shift Begins
#=============================================================================

label late_shift_intro:
    scene edgar_diner_bg
    
    "The bell above the door jingles as two figures in blue step inside."
    
    "Claire and Matt. Their patrol route brings them by here most evenings."
    
    show Claire front_shy at center with dissolve
    
    Claire "Hey, Daniel."
    
    "She gives you that small wave she does—fingers barely lifting from her side, like she's not sure she's allowed to acknowledge you in front of her partner."
    
    "Matt's already sliding into a booth, that practiced smile of his already in place."
    
    # First skill check - ACUITY to notice something off about Matt
    menu:
        "Notice how Matt positions himself" (skill_check=[skill_acuity, 2]):
            "He's chosen the booth with the best view of both entrances. Old habit, maybe. Or something else."
            "His eyes sweep the diner once, twice. Cataloging. You've seen him do it before, but tonight it feels more... deliberate."
            $ add_skill_buff(buff_noticed_matt)
            
        "Focus on Claire":
            "She looks tired. More tired than usual."
            "The shadows under her eyes have shadows of their own."
    
    Claire "Two coffees? The usual?"
    
    menu:
        "\"Coming right up.\"":
            "You grab the pot that's been warming on the burner for the past hour. The coffee's probably strong enough to strip paint by now."
            
        "\"Long shift?\"" (skill_roll=[skill_communion, 8]):
            if skill_success:
                show Claire front_shy happy
                Claire "Is it that obvious?"
                "Something in her shoulders loosens, just a fraction."
                Claire "We've been running calls since four. Domestic on Maple, car break-ins near the track, some kids causing trouble at the old factory..."
                "She trails off, glancing toward Matt."
                $ add_skill_buff(buff_shared_concern)
            else:
                show Claire front_shy
                Claire "Just the regular amount of long."
                "She turns away slightly. The moment passes."
    
    "You pour two cups and carry them over."
    
    # Matt speaks up
    "Matt looks up from his notepad with that grin that never quite reaches his eyes."
    
    "MATT" "Danny-boy! How's the glamorous life of food service treating you?"
    
    menu:
        "\"Living the dream, Matt.\"":
            "MATT" "Ha! That's what I like about you. Keeping that positive attitude."
            "He sips his coffee without breaking eye contact. Testing something. You're not sure what."
            
        "\"Better than answering domestics on Maple.\"" (skill_check=[skill_insight, 3]):
            "Matt's smile flickers—just for a second."
            "MATT" "Claire's been talking, huh?"
            show Claire front_shy mad
            "Claire stiffens beside him."
            
        "Say nothing, just pour the coffee":
            "Sometimes silence is its own answer."
            "Matt shrugs and goes back to his notepad."
    
    "The bell jingles again."
    
    "You'd recognize that silhouette anywhere—oversized jacket, messenger bag, the slight forward lean of someone who's always rushing toward something."
    
    "Val."
    
    hide Claire with dissolve
    
    Val "Daniel! Oh thank god you're working tonight."
    
    "She's out of breath. Her glasses are slightly askew, and she's clutching something to her chest."
    
    Val "I need to show you something. It's—"
    
    "She notices Claire and Matt in the booth. Her enthusiasm dims like someone turned down a dial."
    
    Val "Oh. Hi, Officer Park. Officer Hayes."
    
    show Claire front_shy at right with dissolve
    
    Claire "Val."
    
    "Matt doesn't look up from his notepad."
    
    Val "Daniel, can we talk? In the back maybe?"
    
    menu:
        "\"What's going on, Val?\"":
            Val "Not here. Please."
            "Her eyes flick toward Matt again."
            
        "\"Let me finish up here first.\"":
            Val "This is important. Like, 'Strange Frequencies' important."
            "She lowers her voice to an urgent whisper."
            Val "I recorded something. Last night. You need to hear it."
            
        "\"Is this about the broadcast?\"" (skill_check=[skill_inquiry, 2]):
            "Val's eyes go wide."
            Val "How did you—have you heard it too?"
            "Her hands are shaking slightly as she pulls a cassette tape from her bag."
            $ game_iventory.append(cassette_tape)
            $ add_skill_buff(buff_listened_to_val)
    
    # Setup for character interaction testing
    "Before you can respond, Claire stands."
    
    show Claire front_shy at center
    
    Claire "I should... check in. With dispatch."
    
    "She heads toward the payphone in the corner, leaving you, Val, and Matt in an uncomfortable triangle."
    
    "Val slides onto a counter stool, as far from Matt's booth as possible."
    
    Val "Can we talk now? Please?"
    
    $ events_played_today.append(event_late_shift_start)
    $ finished_events.append(event_late_shift_start)
    
    menu:
        "Talk to Val about the broadcast":
            jump val_broadcast_conversation
            
        "Go check on Claire":
            jump claire_interaction_start
            
        "Deal with customers first":
            "You gesture toward the truckers' booth. Refills needed."
            Val "Fine. But don't take too long."
            call edgar_counter_menu

#=============================================================================
# VAL CONVERSATION BRANCH
#=============================================================================

label val_broadcast_conversation:
    scene edgar_diner_bg
    
    Val "Okay, so you know how I've been trying to pick up EVP frequencies on the old equipment?"
    
    menu:
        "\"The stuff from your dad's storage unit?\"":
            Val "Yeah! The 70s broadcast gear. Anyway, I was scanning frequencies last night around 2 AM..."
            
        "\"Val, we've talked about this...\"":
            Val "I know, I know, you think it's just radio interference. But this is different, Daniel. This is really different."
            
        "Listen carefully" (skill_roll=[skill_acuity, 8]):
            if skill_success:
                "You focus on Val's words, but also on her body language. The way she keeps touching her bag. The slight tremor in her hands."
                "This isn't her usual enthusiasm. She's scared."
                Val "...and then I heard it. Clear as day. A voice."
            else:
                "You try to focus, but the diner's ambient noise keeps pulling your attention. The coffee maker. The truckers. Matt turning a page in his notepad."
                Val "Are you even listening? A voice, Daniel!"
    
    Val "It was reading names. Like... like a radio obituary. But these weren't dead people."
    
    Val "I checked. I spent all night checking. The names—they're people here. In Copperbell Hill. Alive."
    
    menu:
        "\"That's... unsettling.\"":
            Val "Unsettling? Daniel, it announced a death. With a time and place."
            Val "And I don't know if it already happened or if it's going to."
            
        "\"Play me the recording.\"" (skill_check=[skill_resolve, 3]):
            Val "Not here. Not with—"
            "She glances at Matt's booth."
            Val "I made you a copy. It's in the tape I gave you."
            
        "\"Have you told anyone else?\"" (skill_roll=[skill_inquiry, 10]):
            if skill_success:
                Val "I... tried calling my contact at the university. The one who studies radio phenomena."
                Val "He didn't pick up."
                "She swallows hard."
                Val "His name was on the list, Daniel. Second from the end."
            else:
                Val "Who would believe me? You barely believe me, and you're my best friend."
    
    # Give player the polaroid if they don't have it
    if polaroid_photo not in game_iventory:
        Val "Here. I took this last night too."
        "She presses a polaroid into your hand. The image shows the old Heartland Motors building, but something about the shadows..."
        $ game_iventory.append(polaroid_photo)
    
    Val "I need to get back to my apartment. Review the recordings. Cross-reference the names."
    
    Val "Can you come by later? After your shift?"
    
    menu:
        "\"I'll try.\"":
            Val "Try hard. This is big, Daniel. This could be the thing that finally proves..."
            "She doesn't finish the sentence. She doesn't need to."
            
        "\"I'll be there.\"" (important=True):
            Val "Good. Good."
            "She squeezes your arm once, then grabs her bag."
            Val "Be careful tonight. Something feels wrong. More wrong than usual."
    
    "Val heads for the door, nearly colliding with Claire coming back from the payphone."
    
    "They exchange awkward nods."
    
    "And then it's just you, Claire lingering by the counter, and Matt still watching from his booth."
    
    jump claire_interaction_start

#=============================================================================
# CLAIRE INTERACTION (Full Character System Test)
#=============================================================================

label claire_interaction_start:
    scene edgar_diner_bg
    show Claire front_shy at center with dissolve
    
    Claire "Was that about... you know. The zine stuff?"
    
    "There's something in her voice. Not judgment exactly. Concern, maybe. Or curiosity she's trying to hide."
    
    call screen character_interaction(char_claire)

label char_claire_hello:
    Claire "Hey."
    "That small smile again. The one that doesn't quite know if it's allowed to exist."
    return

label char_claire_small_talk(character):
    show Claire front_shy
    
    Claire "It's been quiet tonight. Relatively."
    
    Claire "Matt's been... I don't know. More Matt than usual."
    
    menu:
        "\"What do you mean?\"":
            show Claire front_shy happy
            Claire "Just... watchful. Writing things down. He does that sometimes when he's working on something."
            "She shrugs, but the gesture seems forced."
            
        "\"You seem tired.\"" (skill_roll=[skill_communion, 8, [buff_shared_concern]]):
            if skill_success:
                show Claire front_shy happy
                Claire "Is it that obvious?"
                "She lets out a breath she seems to have been holding."
                Claire "I haven't been sleeping well. Dreams about... old stuff."
                "She doesn't elaborate. You don't push."
            else:
                show Claire front_shy
                Claire "I'm fine."
                "The wall goes up. Familiar. Frustrating."
    
    call screen character_interaction(character)
    return

label claire_talk_patrol(character):
    show Claire front_shy
    
    Claire "The patrol's been normal. As normal as anything gets in this town."
    
    Claire "Though we did get a weird call earlier. Someone reported seeing lights at the old factory."
    
    menu:
        "\"Lights? What kind?\"" (skill_roll=[skill_inquiry, 8]):
            if skill_success:
                Claire "That's the thing. The caller couldn't describe them. Said they were 'wrong' somehow."
                Claire "Matt wanted to check it out, but dispatch pulled us for the domestic instead."
                "She frowns."
                Claire "He seemed... disappointed. More than usual."
            else:
                Claire "Just lights. Probably kids. Or reflections. You know how it is."
                
        "\"The Heartland Motors building?\"":
            show Claire front_shy happy
            Claire "You've been talking to Val too much."
            "But there's no real criticism in it. Maybe even a hint of fondness."
            
        "Say nothing, just listen":
            Claire "Anyway. Probably nothing."
            "The word 'probably' hangs in the air longer than it should."
    
    call screen character_interaction(character)
    return

label claire_talk_matt(character):
    show Claire front_shy
    
    # This tests the skill buff system with negative modifier
    Claire "Matt's... Matt."
    
    "She glances toward his booth. He's still writing."
    
    menu:
        "\"You two seem close.\"":
            Claire "He's my partner. We have to be."
            "Something in her tone suggests that's not quite the whole truth."
            
        "\"Does he always take so many notes?\"" (skill_roll=[skill_insight, 10, [buff_noticed_matt]]):
            # Note: buff_noticed_matt is NEGATIVE, making this harder if Matt caught you watching
            if skill_success:
                show Claire front_shy happy
                Claire "You noticed that too?"
                "She lowers her voice."
                Claire "He's been doing it more lately. And he never lets me see what he's writing."
                Claire "Probably nothing. Case notes. But..."
                "She doesn't finish."
            else:
                Claire "He's thorough. It's a good quality in a cop."
                "The answer sounds rehearsed."
                
        "\"Never mind.\"":
            Claire "Okay."
            "She seems almost relieved."
    
    call screen character_interaction(character)
    return

label claire_talk_relationship(character):
    show Claire front_shy
    
    # High-stakes emotional conversation testing multiple skills
    Claire "Us?"
    
    "The word hangs between you like something fragile."
    
    menu:
        "\"I've been thinking about... where we stand.\"" (skill_roll=[skill_sentiment, 10, [buff_shared_concern, buff_coffee_offered]]):
            if skill_success:
                show Claire front_shy happy
                Claire "Me too."
                "She looks down at her hands."
                Claire "I know I've been distant. It's not... it's not you."
                Claire "There's stuff I haven't told you. About before. About why I became a cop."
                "She takes a breath."
                Claire "I'm not ready to talk about it yet. But I want to be. Someday."
                "It's more than she's ever given you. It feels like a gift."
            else:
                show Claire front_shy
                Claire "Daniel..."
                "She shakes her head."
                Claire "This isn't the place. Not with Matt right there."
                "The moment passes. You feel it go."
                
        "\"I miss how things were.\"":
            show Claire front_shy happy
            Claire "Things were never really 'how they were.' We just... existed in the same space."
            Claire "But I miss it too. Whatever it was."
            
        "\"Forget I said anything.\"" (important=True):
            show Claire front_shy
            Claire "Already forgotten."
            "But the look she gives you suggests otherwise."
    
    call screen character_interaction(character)
    return

#=============================================================================
# ITEM SHOWING LABELS (Character Reaction Tests)
#=============================================================================

label claire_shown_thermos(character):
    show Claire front_shy happy
    
    Claire "Oh! My thermos. I've been looking for that."
    
    "She takes it, fingers brushing yours for just a moment."
    
    Claire "Thanks for holding onto it. I keep meaning to come by and pick it up, but..."
    
    "She trails off. You both know the 'but' has nothing to do with forgetting."
    
    $ add_skill_buff(buff_coffee_offered)
    
    # Remove from inventory
    $ game_iventory.remove(coffee_thermos)
    
    call screen character_interaction(character)
    return

label claire_shown_polaroid(character):
    show Claire front_shy
    
    "Claire takes the polaroid, studying it with a cop's eye."
    
    Claire "The old factory. Val's work?"
    
    menu:
        "\"She took it last night. Says something's wrong with the shadows.\"":
            show Claire front_shy mad
            Claire "Wrong how?"
            "She tilts the image, catching the light."
            Claire "...huh."
            "She doesn't elaborate, but you see her jaw tighten."
            
        "\"Just something she wanted me to see.\"":
            Claire "Val always wants you to see something."
            "It's not quite an accusation. Not quite not one either."
    
    "She hands it back."
    
    Claire "Be careful with that stuff, Daniel. Some things are better left alone."
    
    call screen character_interaction(character)
    return

label claire_show_generic(character):
    show Claire front_shy
    
    Claire "What's that?"
    
    "She glances at it without much interest."
    
    Claire "I should probably get back to Matt. He's giving me that look."
    
    call screen character_interaction(character)
    return

#=============================================================================
# KITCHEN EVENT (Tests Event Priority System)
#=============================================================================

label kitchen_strange_noise:
    scene edgar_kitchen_bg
    
    "The kitchen is empty. Blackwood must be on his break."
    
    "The fluorescent light above the prep station flickers twice."
    
    "And then you hear it."
    
    "A sound from the walk-in freezer. Not mechanical. Not the compressor cycling."
    
    "Something else."
    
    menu:
        "Investigate the freezer" (skill_roll=[skill_resolve, 8]):
            if skill_success:
                "You approach the freezer door. The handle is cold—colder than it should be."
                "You pull it open."
                "..."
                "Nothing. Just frozen patties and bags of ice."
                "But for a moment, just before the light inside flickered on, you could have sworn you saw—"
                "No. Nothing. Just shadows and cold air."
            else:
                "Your hand reaches for the freezer door."
                "Stops."
                "Some instinct—something deep and old—tells you not to open it. Not tonight."
                "You back away slowly."
                
        "Ignore it—probably just the compressor":
            "That's what you tell yourself."
            "The sound doesn't repeat."
            "Probably just the compressor."
            
        "Call out to see if someone's there" (skill_roll=[skill_acuity, 8]):
            if skill_success:
                "\"Hello?\""
                "Your voice echoes off the steel surfaces."
                "No response. But you notice something else—the radio on the prep counter."
                "It's on. Playing static. You don't remember turning it on."
                "Through the static, just for a second, you hear something that might be a voice."
                "Listing names."
            else:
                "\"Hello?\""
                "Nothing. The sound stops."
                "Probably just pipes."
    
    $ end_event()
    
    jump kitchen_label_menu

label kitchen_label_menu:
    menu:
        "Check the fridge":
            $ run_interaction(kitchen_interaction)
            
        "Use the phone":
            "The kitchen phone is for employees only. The Boss would have your head if you used it for personal calls."
            call kitchen_label_menu
            
        "Return to the counter":
            $ move_room(room_edgar_counter)
            
    call kitchen_label_menu

#=============================================================================
# BOSS CALL EVENT (Tests Event System + Character Dialogue)
#=============================================================================

label boss_evening_call:
    scene edgar_diner_bg
    
    "The phone behind the counter rings."
    
    "You already know who it is. It's always him at this hour."
    
    Boss "Listen up, you catastrophically incompetent waste of restaurant-grade cooking oil."
    
    "Ah. He's in a good mood tonight."
    
    Boss "I need you to do something important. Something that might actually challenge that single functioning brain cell you've been hoarding."
    
    menu:
        "\"Yes, sir?\"":
            Boss "Don't sound so eager. It makes me suspicious."
            
        "\"What do you need?\"" (skill_check=[skill_resolve, 2]):
            Boss "Oh, asking questions now? Getting above your station? I like that. Shows initiative. Misguided, doomed initiative, but initiative nonetheless."
            
        "Just wait in silence":
            Boss "Not talking? Fine. I can hear you breathing. Stop that."
    
    Boss "There's a delivery coming tonight. After close. You're going to receive it."
    
    Boss "Don't ask what's in it. Don't open it. Don't look at it with those cow eyes of yours."
    
    Boss "Just put it in the storeroom and forget you ever saw it."
    
    menu:
        "\"What kind of delivery?\"" (skill_roll=[skill_inquiry, 12]):
            if skill_success:
                Boss "..."
                "A long pause. Unusual for him."
                Boss "It's from the high-ups. That's all you need to know."
                Boss "They're... testing something. New product line. Very hush-hush."
                "His voice sounds different. Almost nervous."
            else:
                Boss "What did I just say about asking questions? Do you have some kind of auditory processing disorder? Should I be speaking slower? Using smaller words?"
                
        "\"Understood.\"":
            Boss "Good. Maybe you're not completely beyond redemption."
            Boss "I'll be watching the cameras. Don't do anything stupid."
            Boss "Well. Stupider than usual."
            
        "\"Why me?\"":
            Boss "Because everyone else has even worse judgment than you do, which is genuinely impressive."
            Boss "Also because you're working tonight, genius."
    
    "The line goes dead."
    
    "Claire is watching you from the booth. Matt has stopped writing."
    
    $ end_event()
    
    call edgar_counter_menu

#=============================================================================
# SCENARIO END SEQUENCE
#=============================================================================

label end_late_shift:
    scene edgar_diner_bg
    
    "The clock reads 11:58 PM."
    
    "Claire and Matt have left. The truckers paid their tab an hour ago."
    
    "You're alone in the diner, waiting for a delivery you're not supposed to ask about."
    
    "Val's cassette tape is in your pocket. The polaroid sits on the counter where Claire left it."
    
    "Through the window, the Heartland Motors building is just a shape in the darkness."
    
    "But tonight, for just a moment, you could swear you see a light in one of the upper windows."
    
    "Then it's gone."
    
    menu:
        "Wait for the delivery":
            "You wait."
            "Nothing happens."
            "At least, nothing you can see."
            
        "Close up early and go to Val's" (important=True):
            "The Boss will be furious. But some things are more important than deliveries you're not supposed to ask about."
            
        "Check the storeroom one more time" (skill_roll=[skill_acuity, 10]):
            if skill_success:
                "You push open the storeroom door."
                "Everything is where it should be. Except..."
                "There's a box in the corner. You don't remember seeing it before."
                "It's unmarked. Sealed with tape that looks older than it should be."
                "The delivery arrived. Somehow. You never heard anyone come in."
            else:
                "The storeroom is exactly as you left it."
                "Empty. Waiting."
    
    "The late shift is over."
    
    $ calendar.next_day()
    
    "Tomorrow is [weekdays_list[calendar.weekday]], [months_list[calendar.month]] [calendar.day]."
    
    "Whatever comes next, it can wait until then."
    
    # Return to main menu or continue to next scene
    call screen travel()

#=============================================================================
# ITEM INSPECTION LABELS
#=============================================================================

label inspect_polaroid:
    "You study the polaroid more closely."
    "The Heartland Motors building, shot at night. Val's timestamp says 2:17 AM."
    "The shadows don't match the light sources. They bend in ways shadows shouldn't."
    "And in one of the windows—third floor, northeast corner—there's something."
    "A shape. Too indistinct to identify. Too present to ignore."
    call screen inventory_screen
    return

label inspect_thermos:
    "Claire's thermos. CBHPD issue."
    "There's a small dent near the bottom where she dropped it once. She told you the story—slipped on ice during a pursuit, nearly tackled a suspect with hot coffee."
    "She laughed when she told it. One of the few times you've seen her laugh."
    call screen inventory_screen
    return

label inspect_cassette:
    "The tape is heavier than it should be. Or maybe that's just your imagination."
    "Val wrote on the label in her cramped handwriting: 'BROADCAST - 9/9/97 - DO NOT PLAY ALONE'"
    "You don't have a tape player here. You'll need to find one."
    "Part of you hopes you don't."
    call screen inventory_screen
    return