## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

################################################################################
## Skill Check XP Tracking System
################################################################################

init python:
    def award_skill_check_xp_once(check_id):
        """
        Awards XP for seeing a skill check option, but only once per unique check.
        Returns True if XP was just awarded, False if already awarded before.
        """
        global awarded_skill_checks
        if check_id not in awarded_skill_checks:
            awarded_skill_checks.add(check_id)
            add_xp(xp_per_skill_check, xp_gain_skill_check_loc)
            return True
        return False

    def register_skill_roll_result(roll_id, roll_result=False):
        """
        Registers that a skill roll has been made.
        """
        global skill_rolls_made
        skill_rolls_made[roll_id] = roll_result
        
        # Debug output
        print("=" * 50)
        print("SKILL ROLL REGISTERED")
        print(f"  Roll ID: {roll_id}")
        print(f"  Result: {roll_result}")
        print(f"  All rolls: {skill_rolls_made}")
        print("=" * 50)

    def generate_choice_id(caption, skill, difficulty):
        """
        Generates a unique identifier for a skill check/roll based on its properties.
        """
        choice_id = (caption, skill.GetName(), difficulty)
        
        # Debug output
        print("-" * 50)
        print("CHOICE ID GENERATED")
        print(f"  Caption: {caption}")
        print(f"  Skill: {skill.GetName()}")
        print(f"  Difficulty: {difficulty}")
        print(f"  Generated ID: {choice_id}")
        print(f"  ID in skill_rolls_made: {choice_id in skill_rolls_made}")
        if choice_id in skill_rolls_made:
            print(f"  Stored result: {skill_rolls_made[choice_id]}")
        print("-" * 50)
        
        return choice_id

# Track which skill checks have already awarded XP (persists across saves)
default awarded_skill_checks = set()
# Track which skill rolls have been made
default skill_rolls_made = {}

################################################################################
## Main Choice Screen
################################################################################

screen choice(items):
    
    # Dark overlay background
    frame:
        xfill True
        yfill True
        background Transform("black", alpha=0.5)
    
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        
        for item in items:
            # Extract skill parameters from menu item
            $ item_skill_roll = item.kwargs.get("skill_roll", [])
            $ item_skill_check = item.kwargs.get("skill_check", [])
            $ item_skill_roll_mode = item.kwargs.get("skill_roll_mode", 0 ) 
            
            # Check if the item is marked as important choice
            $ item_important = item.kwargs.get("important", False)

            # Generate roll_id early if it's a skill roll
            $ roll_id = generate_choice_id(item.caption, item_skill_roll[0], item_skill_roll[1]) if item_skill_roll else None
            # Check if this roll was already made
            $ roll_already_made = roll_id in skill_rolls_made if roll_id else False
            $ roll_was_success = skill_rolls_made.get(roll_id) if roll_already_made else None
            
            # Determine if this choice should be available and handle XP
            python:
                # Default: choice is available
                choice_available = True
                
                # Skill checks block the choice if skill level is too low
                if item_skill_check:
                    choice_available = item_skill_check[0].level >= item_skill_check[1]
                    
                    # Award XP for seeing this skill check (only once per unique check)
                    check_id = generate_choice_id(item.caption, item_skill_check[0], item_skill_check[1])
                    award_skill_check_xp_once(check_id)
                # Skill rolls can be limited based on previous rolls
                #elif item_skill_roll:
                #    roll_id = generate_choice_id(item.caption, item_skill_roll[0], item_skill_roll[1])
                #    choice_available = roll_id not in skill_rolls_made or item_skill_roll_mode >= 1
            
            button:
                xalign 0.5
                xsize 800
                selected False
                sensitive choice_available
                if roll_already_made:
                    if roll_was_success:
                        style "choice_success_menu_button"
                    else:
                        style "choice_failed_menu_button"
                else:
                    style "choice_menu_button"
                
                # Set up the action based on skill type
                if item_skill_roll:
                    if roll_id not in skill_rolls_made or item_skill_roll_mode >= 1:
                        # Skill roll choice
                        if len(item_skill_roll) > 2:
                            # Roll with buffs
                            action [
                                Function(game_skill_roll, item_skill_roll[0], item_skill_roll[1], item_skill_roll[2], roll_id),
                                item.action
                            ]
                        else:
                            # Roll without buffs
                            action [
                                Function(game_skill_roll, item_skill_roll[0], item_skill_roll[1], [], roll_id),
                                item.action
                            ]
                    else:
                        
                        action [
                            SetVariable("skill_success", skill_rolls_made.get(roll_id, False)), # Get previous roll result
                            item.action
                            ]
                else:
                    # Regular choice or skill check (XP already awarded on display)
                    action item.action
                
                # Choice content
                
                    
                vbox:
                    #if item_skill_check or item_skill_roll:
                    #    yalign 0.5
                    # Skill Roll indicator (inlined)
                    if item_skill_roll:
                        vbox:
                            #background None
                            #xsize 200
                            xpos 38
                    
                            # Display roll chance
                            python:
                                # Calculate roll chance
                                if len(item_skill_roll) > 2:
                                    roll_chance = rollchance(item_skill_roll[0], item_skill_roll[1], item_skill_roll[2])
                                else:
                                    roll_chance = rollchance(item_skill_roll[0], item_skill_roll[1])
                                
                                # Build the display text
                                skill_name = item_skill_roll[0].GetName().upper()
                                
                                if not roll_already_made:
                                    roll_status = "{}%".format(roll_chance)
                                elif roll_was_success:
                                    roll_status = "{color=#63c763}SUCCESS!{/color}"
                                else:
                                    roll_status = "{color=#c73232}FAILED!{/color}"
                            hbox:
                                
                                vbox:
                                    text "[skill_name] ROLL" style "dialogue_entry_important_text" size 14 color "#c7b695"
                                    
                                text ":" style "dialogue_entry_important_text" size 14 xalign 1.0 color "#c7b695"
                                text  [roll_status] style "dialogue_entry_important_text" size 14 xalign 1.0
                                text "([get_difficulty_descriptor(item_skill_roll[1])])" style "dialogue_entry_important_text" size 12 yalign 0.5 color Color(get_difficulty_color(item_skill_roll[1]))
                                

                            
                            # Display active buffs for this roll
                            if len(item_skill_roll) > 2 and item_skill_roll[2]:
                                python:
                                    active_buffs = [b for b in item_skill_roll[2] if b in available_skill_buffs]
                                
                                if active_buffs:
                                    vbox:
                                        xsize 724
                                        spacing 2
                                        
                                        python:
                                            # Better character width estimation
                                            # Adjust multiplier based on your font (6-8 pixels per char is typical for size 12)
                                            avg_char_width = 9  # Adjust this value
                                            max_line_chars = int(724 / avg_char_width)
                                            
                                            lines = []
                                            current_line = []
                                            current_chars = 0
                                            
                                            for i, buff in enumerate(active_buffs):
                                                sign = '+' if buff.value >= 0 else ''
                                                buff_text = buff.GetName() + ":" + sign + str(buff.value)
                                                
                                                # Count characters including comma and space
                                                item_chars = len(buff_text)
                                                if current_line:
                                                    item_chars += 2  # ", "
                                                
                                                # Check if this buff fits on current line
                                                # Leave some margin (10 chars) for safety
                                                if current_line and current_chars + item_chars > max_line_chars - 10:
                                                    lines.append(current_line[:])
                                                    current_line = []
                                                    current_chars = 0
                                                
                                                current_line.append((buff, buff.value >= 0))
                                                current_chars += len(buff_text) + (2 if current_line else 0)
                                            
                                            if current_line:
                                                lines.append(current_line)
                                        
                                        for line in lines:
                                            hbox:
                                                spacing 0
                                                for j, (buff, is_positive) in enumerate(line):
                                                    $ sign = '+' if buff.value >= 0 else ''
                                                    $ color = "#63c763" if buff.value > 0 else "#c73232"
                                                    
                                                    if j > 0:
                                                        text ", " style "dialogue_entry_important_text" size 12
                                                    
                                                    text "[buff.GetName()]:[sign][buff.value]":
                                                        style "dialogue_entry_important_text"
                                                        size 12
                                                        color color
            
                    # Skill Check indicator (inlined)
                    if item_skill_check:
                            vbox:
                                xsize 724  # Adjust to fit within your button width minus margins
                                xpos 38
                                hbox:
                                    # Show current level vs required                                    
                                    text "[item_skill_check[0].GetName()!u] CHECK: [item_skill_check[0].level]/[item_skill_check[1]]" size 14 style "check_skill_text"
                                    if choice_available == True:
                                        text "(SUCCESS)" style "dialogue_entry_important_text" size 12 yalign 0.5 color "#63c763"
                                    else:
                                        text "(FAILED)" style "dialogue_entry_important_text" size 12 yalign 0.5 color "#c73232"
                    # Choice text
                    frame:
                        xfill True
                        background None
                    
                        hbox:
                            if roll_already_made:
                                if roll_was_success:
                                    $ entry_text_style = "dialogue_entry_success_text"
                                else:
                                    $ entry_text_style = "dialogue_entry_failed_text"
                            else:
                                $ entry_text_style = "dialogue_entry_text"

                            text "> " style entry_text_style
                            $ choice_caption = "[item.caption]" if choice_available else "???"
                            text [choice_caption] style entry_text_style
                    
                    if item_important == True:
                        text "ADVANCE >>>" style "dialogue_entry_important_text" size 14 xpos 38 color game_yellow_color

################################################################################
## Choice Talks Screen (for character conversations)
################################################################################

screen choice_talks(items, args=[character, None]):
    
    frame:
        xfill True
        yfill True
        background Transform("black", alpha=0.5)
    
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        
        # Conversation options
        for item in items:
            $ game_label = item.kwargs.get("game_label", None)
            
            button:
                #at dialogue_entry
                xalign 0.5
                xsize 800
                action Call(game_label, character)
                selected False
                sensitive True
                style "hover_button"
                
                text "[item.caption]":
                    yalign 0.5
                    xalign 0.5
                    style "dialogue_entry_text"
        
        # Back button
        button:
            #at dialogue_entry
            xalign 0.5
            xsize 800
            action Call("char_interaction", character)
            selected False
            sensitive True
            style "hover_button"
            
            text "< GO BACK":
                yalign 0.5
                xalign 0.5
                style "dialogue_entry_text"

################################################################################
## Character Interaction Screen
################################################################################

screen character_interaction(character):
    tag menu
    vbox spacing 20:
        xalign 0.1
        yalign 0.5
        
        # Character name header
        frame style "white_tile":
            xpadding 40
            text "[character.name!u]" size 45 xalign 0.5 yalign 0.5 color game_black_color font "GFX/fonts/vhs-gothic.ttf"
        
        # Interaction buttons
        vbox spacing 10:
            # Small Talk button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call(character.small_talk_game_label, character)
                hbox spacing 5:
                    frame xsize 80 ysize 80:
                        style "hover_button"
                    frame xsize 340 ysize 80:
                        style "hover_button"
                        text "SMALL TALK" yalign 0.5 size 50 style "select_button_text"
            
            # Conversation button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call("char_conversation_list", character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "CONVERSATION" yalign 0.5 size 45 style "select_button_text"
            
            # Show Item button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Show("inventory_screen", character = character, screen_mode = "show_item")
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SHOW ITEM" yalign 0.5 size 45 style "select_button_text"
            
            # Go Back button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Return()
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "< GO BACK" yalign 0.5 size 45 style "select_button_text"

################################################################################
## Inventory Screen
################################################################################

screen inventory_screen(**kwargs):
    tag menu
    default character = kwargs.get("character", None)
    default screen_mode = kwargs.get("screen_mode","default")
    default slot_value = None

    if screen_mode == "default":
        
        use game_menu(_("inventory"), scroll=None, content_yalign=0.0)
    
    if screen_mode != "default":
        #Dark background
        frame xfill True yfill True background Transform("black", alpha=0.7)

    hbox: 
        if screen_mode != "default":
            xalign 0.5 
        else:
            xalign 0.6
        yalign 0.5
        vbox:
            ysize 775
            xsize 760
            hbox:
                frame:
                    style "black_tile_border"
                    xsize 60
                    ysize 60
                frame:
                    style "black_tile_underline"
                    xfill True
                    ysize 60
                    text "IVENTORY" style "title_text" yalign 0.25
            frame xfill True yfill True:
                style "black_tile_hollow"
                grid 5 5 spacing 15 xalign 0.5 yalign 0.5:
                    for slot in range(25):
                        fixed:
                            ysize 128
                            xsize 128
                            
                            button:
                                at selected_hover
                                ysize 128
                                xsize 128
                                xalign 0.5
                                yalign 0.5
                                action SetScreenVariable("slot_value", slot)
                                sensitive len(game_iventory) > slot
                                selected (slot_value == slot)
                                style "hover_button"
                                
                                if len(game_iventory) > slot:
                                    image "[game_iventory[slot].icon]" xalign 0.5 yalign 0.5
                    
        vbox:
            xsize 384
            hbox:
                frame:
                    style "black_tile"
                    xsize 60
                    ysize 60
                    text "*" xalign 0.5
                frame:
                    style "black_tile"
                    xsize 264
                    ysize 60
                    text "ITEMS" xalign 0.5 style "title_text" yalign 0.25
                frame:
                    style "black_tile"
                    xsize 60
                    ysize 60
                    text "*" xalign 0.5

            frame:
                            style "black_tile_75"
                            xfill True
                            vbox xalign 0.5 yalign 0.5:
                                text "-----------------" style "title_text" xalign 0.5
                                frame:
                                    background None
                                    xfill True
                                    ysize 35
                                    if slot_value is not None:
                                        text "[game_iventory[slot_value].name!u]" xalign 0.5 yalign 0.5 style "title_text" size 30
                                text "-----------------" style "title_text" xalign 0.5


            frame:
                style "black_tile_75"
                xfill True
                ysize 384
                vbox:
                    text "-----------------" style "title_text" xalign 0.5
                    xalign 0.5
                    fixed:
                        xfill True
                        yfill True
                        vbox:
                            if slot_value is not None:
                                text "[game_iventory[slot_value].desc]" style "desc_text"
                        text "-----------------" style "title_text" xalign 0.5 yalign 1.0
                            
            # Action buttons
            if screen_mode != "default":
                button xfill True ysize 50 style "hover_button":
                    sensitive slot_value is not None
                    if slot_value is not None:
                        action Call("char_item_reaction", game_iventory[slot_value], mode, character, slot_value)
                    text "SHOW ITEM" xalign 0.5 yalign 0.5 style "select_button_text"
                if screen_mode == "show_item": 
                    button xfill True ysize 50 style "hover_button":
                        text "< Return" xalign 0.5 yalign 0.5 style "select_button_text" 
                        action Hide()
            else:
                button xfill True ysize 50 style "hover_button":
                    sensitive slot_value is not None
                    #if slot_value is not None:
                    #    action Call("char_item_reaction", game_iventory[slot_value], mode, character, slot_value)
                    text "INSPECT ITEM" xalign 0.5 yalign 0.5 style "select_button_text"
            