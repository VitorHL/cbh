
init python:

#########################

    def add_xp(quantity,reason):
        global player_xp, player_level, xp_progression, xp_progression
        player_xp += quantity
        next_level = player_level + 1
        if quantity >= 0:
            renpy.notify(f"{reason}{{color=#0adc28}}+{quantity}XP{{/color}}")
        else:
            renpy.notify(f"{reason}{{color=#dc2020}}-{quantity}XP{{/color}}")
        if next_level in xp_progression and player_xp >= xp_progression[next_level]:
            player_levelup()
            

########################

    def player_levelup():
        global player_level, player_xp, att_pts_available, level_up_loc, level_prefix
        player_xp -= xp_progression[player_level + 1]
        player_level += 1
        att_pts_available += 1
        renpy.notify(f"{level_up_loc}{{color=#0adc28}}{level_prefix}{player_level}{{/color}}")