################################################################################
## Daniel's Apartment
################################################################################

label daniel_apartment_label:

    # $ char_gia.add_item_reaction( burgar, "gia_show_burger" )
    # $ char_gia.add_item_reaction( coke, "gia_show_coke" )
    # $ char_gia.add_talk( "Relationship", "char_gia_talk_relationship" )
    # $ char_gia.add_talk( "Val", "char_gia_talk_val" )
    # $ char_gia.add_talk( "The Building", "char_gia_talk_building" )

    $ char_gia.interested_items[burgar] = "gia_show_burger"
    $ char_gia.interested_items[coke] = "gia_show_coke"
    $ char_gia.relevant_itens.append(coke)
    $ char_gia.interested_talks["Relationship"] = "char_gia_talk_relationship"
    $ char_gia.interested_talks["The Building"] = "char_gia_talk_building"
    $ char_gia.interested_talks["Val"] = "char_gia_talk_val"

    
    scene daniel_apartment_bg with fade
    #show image "gui/overlay/summer_overlay.webp" onlayer underlay
    show Claire front_shy
    call screen character_interaction(char_gia)
    $ check_for_event()
    call daniel_apartment_label_menu
label daniel_apartment_label_menu:
    menu:
        "Talk with someone":
            menu:
                "About the milkshake sack..." (skill_check=[skill_inquiry,10]):
                    "Ok"
                "I don't know much about the boss either." (skill_roll=[skill_communion,14]):
                    #$ skill_check(skill_communion, 14)
                    #show screen dice_roll(1,1)
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "I don't have time for it, just say where you left it." (skill_roll=[skill_sentiment,14]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "I would prefer to not say my reasons." (skill_roll=[skill_acuity,5]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
                "Hey, don't speak about Val like that!" (skill_roll=[skill_inquiry,18]):
                    if skill_success == True:
                        "The test was a success"
                    if skill_success == False:
                        "The test was a failure"
        "Next Day":
            $ calendar.next_day()
        "Fridge":
            $ run_interaction(kitchen_interaction)
        "Travel":
            call screen travel()
    call daniel_apartment_label_menu

