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
    
    def generate_skill_check_id(caption, skill, difficulty):
        """
        Generates a unique identifier for a skill check based on its properties.
        """
        return (caption, skill.GetName(), difficulty)

# Track which skill checks have already awarded XP (persists across saves)
default awarded_skill_checks = set()

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
            
            # Check if the item is marked as important choice
            $ item_important = item.kwargs.get("important", False)
            
            # Determine if this choice should be available and handle XP
            python:
                # Default: choice is available
                choice_available = True
                
                # Skill checks block the choice if skill level is too low
                if item_skill_check:
                    choice_available = item_skill_check[0].level >= item_skill_check[1]
                    
                    # Award XP for seeing this skill check (only once per unique check)
                    check_id = generate_skill_check_id(item.caption, item_skill_check[0], item_skill_check[1])
                    award_skill_check_xp_once(check_id)
            
            button:
                xalign 0.5
                xsize 800
                selected False
                sensitive choice_available
                if item_important:
                    style "important_choice_button"
                else:
                    style "choice_menu_button"
                
                # Set up the action based on skill type
                if item_skill_roll:
                    # Skill roll: always available, but success is random
                    if len(item_skill_roll) > 2:
                        action [
                            Function(game_skill_roll, item_skill_roll[0], item_skill_roll[1], item_skill_roll[2]),
                            item.action
                        ]
                    else:
                        action [
                            Function(game_skill_roll, item_skill_roll[0], item_skill_roll[1]),
                            item.action
                        ]
                else:
                    # Regular choice or skill check (XP already awarded on display)
                    action item.action
                
                # Choice content
                hbox:
                    # Skill Roll indicator (inlined)
                    if item_skill_roll:
                        vbox:
                            #background None
                            xsize 200
                            frame xalign 0.5:
                                style "skill_tile"
                                ypadding 13
                                xpadding 13
                                
                                vbox:
                                    text "-SKILL ROLL-" yalign 0.5 xalign 0.5 style "yellow_text" size 14
                                    
                                    # Display active buffs for this roll
                                    if len(item_skill_roll) > 2 and item_skill_roll[2]:
                                        python:
                                            active_buffs = [b for b in item_skill_roll[2] if b in available_skill_buffs]
                                        
                                        if active_buffs:
                                            vbox:
                                                xalign 0.5
                                                spacing 5
                                                
                                                for buff_row in chunk(active_buffs, 2):
                                                    hbox:
                                                        spacing 40
                                                        align (0.5, 0.5)
                                                        
                                                        for buff in buff_row:
                                                            if buff.value >= 0:
                                                                text "[buff.GetName()]: +[buff.value]":
                                                                    yalign 0.5
                                                                    xalign 0.5
                                                                    style "dialogue_entry_text"
                                                                    color "#0adc28"
                                                                    size 14
                                                            else:
                                                                text "[buff.GetName()]: [buff.value]":
                                                                    yalign 0.5
                                                                    xalign 0.5
                                                                    style "dialogue_entry_text"
                                                                    color "#dc2020"
                                                                    size 14
                                    
                                    # Display roll chance
                                    if len(item_skill_roll) > 2:
                                        $ roll_chance = rollchance(item_skill_roll[0], item_skill_roll[1], item_skill_roll[2])
                                    else:
                                        $ roll_chance = rollchance(item_skill_roll[0], item_skill_roll[1])
                                    
                                    text "< [item_skill_roll[0].GetName()!u]:[roll_chance]% >" yalign 0.5 xalign 0.5 style "yellow_text" size 16
                        
                    # Skill Check indicator (inlined)
                    if item_skill_check:
                            vbox:
                                #background None
                                xsize 200
                                frame:
                                    xalign 0.5
                                    style "skill_check_border"
                                    
                                    vbox:
                                        text "-SKILL CHECK-" yalign 0.5 xalign 0.5 style "check_skill_text" size 14
                                        
                                        # Show current level vs required                                    
                                        text "< [item_skill_check[0].GetName()!u]:[item_skill_check[0].level]/[item_skill_check[1]] >":
                                            yalign 0.5
                                            xalign 0.5
                                            style "check_skill_text"
                                            size 16
                    
                    vbox:
                        if item_skill_check or item_skill_roll:
                            yalign 0.5
                        # Choice text
                        frame:
                            xfill True
                            background None
                            if choice_available:
                                hbox:
                                    text "> ":
                                        if item_important:
                                            style "dialogue_entry_text"
                                        else:
                                            style "dialogue_entry_text"
                                    text "[item.caption]": 
                                        if item_important:
                                            style "dialogue_entry_text"
                                        else:
                                            style "dialogue_entry_text"
                            else:
                                text "< LOCKED >" style "dialogue_entry_text" xalign 0.15 yalign 0.5 size 38
                        if item_important == True:
                            text "ADVANCE >>>" style "dialogue_entry_important_text" size 14 xpos 38

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
                at dialogue_entry
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
            at dialogue_entry
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
    
    vbox spacing 20:
        xalign 0.1
        yalign 0.5
        
        # Character name header
        frame:
            background Transform(Frame("gui/tiles/white_tile.webp", 3, 3))
            text "[character.name!u]" size 45 xalign 0.5 yalign 0.5 color "#000000"
        
        # Interaction buttons
        vbox spacing 10:
            # Small Talk button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call(character.small_talk_game_label, character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SMALL TALK" yalign 0.5 size 45 style "dialogue_entry_text"
            
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
                        text "CONVERSATION" yalign 0.5 size 45 style "dialogue_entry_text"
            
            # Show Item button
            button:
                yalign 0.5
                hover_sound "audio/menu_hover.wav"
                activate_sound "audio/menu_select.wav"
                action Call("show_char_item", 1, character)
                hbox spacing 5:
                    frame xsize 64 ysize 64:
                        style "hover_button"
                    frame xsize 320 ysize 64:
                        style "hover_button"
                        text "SHOW ITEM" yalign 0.5 size 45 style "dialogue_entry_text"
            
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
                        text "< GO BACK" yalign 0.5 size 45 style "dialogue_entry_text"

################################################################################
## Inventory Screen
################################################################################

screen inventory_screen(mode=0, character=None, selected_slot=None):
    
    default slot_value = selected_slot
    
    frame:
        xfill True
        yfill True
        background Transform("black", alpha=0.5)
        
        hbox spacing 20:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.5
            
            # Left panel: Item grid
            frame:
                xanchor 0.5
                xpos 0.5
                background None
                
                vbox spacing 5:
                    # Header
                    frame:
                        xalign 0.5
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                        text "INVENTORY" size 45 xalign 0.5 yalign 0.5
                    
                    # Divider
                    frame:
                        ysize 5
                        xsize 592
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    
                    # Item grid (5x4 = 20 slots)
                    grid 5 4 spacing 15 xalign 0.5:
                        for slot in range(20):
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
                    
                    # Bottom divider
                    frame:
                        ysize 5
                        xsize 592
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
            
            # Right panel: Item details
            frame:
                xsize 384
                xanchor 0.5
                xpos 0.5
                background None
                
                vbox spacing 5:
                    # Item name header
                    frame:
                        xalign 0.5
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                        
                        if slot_value is not None:
                            text "[game_iventory[slot_value].name!u]" size 45 xalign 0.5
                        else:
                            text "SELECT ITEM" size 45 xalign 0.5
                    
                    # Divider
                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    
                    # Item icon display
                    frame:
                        xalign 0.5
                        xfill True
                        ysize 128
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3), alpha=0.5)
                        
                        if slot_value is not None:
                            image "[game_iventory[slot_value].icon]" xalign 0.5 yalign 0.5
                    
                    # Divider
                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    
                    # Item description
                    frame:
                        xalign 0.5
                        xfill True
                        ysize 384
                        background Transform(Frame("gui/tiles/black_tile.webp", 3, 3))
                        
                        if slot_value is not None:
                            text "[game_iventory[slot_value].desc]" style "desc_text"
                    
                    # Divider
                    frame:
                        ysize 5
                        xfill True
                        xalign 0.5
                        background Frame("gui/tiles/white_tile.webp", 3, 3)
                    
                    # Action buttons
                    frame:
                        xfill True
                        ysize 48
                        background None
                        
                        hbox spacing 3:
                            align (0.5, 0.5)
                            
                            # Back button
                            button:
                                xalign 0.5
                                yalign 0.5
                                hover_sound "audio/menu_hover.wav"
                                activate_sound "audio/menu_select.wav"
                                style "hover_button"
                                
                                if mode == 1:
                                    action Call("char_interaction", character)
                                else:
                                    action Return()
                                
                                text "< GO BACK" yalign 0.5 style "dialogue_entry_text"
                            
                            # Inspect/Show button
                            button:
                                xalign 0.5
                                yalign 0.5
                                sensitive slot_value is not None
                                hover_sound "audio/menu_hover.wav"
                                activate_sound "audio/menu_select.wav"
                                style "hover_button"
                                
                                if mode == 0:
                                    if slot_value is not None:
                                        action Call(game_iventory[slot_value].game_label)
                                    text "INSPECT" yalign 0.5 style "dialogue_entry_text"
                                else:
                                    if slot_value is not None:
                                        action Call("char_item_reaction", game_iventory[slot_value], mode, character, slot_value)
                                    text "SHOW" yalign 0.5 style "dialogue_entry_text"
