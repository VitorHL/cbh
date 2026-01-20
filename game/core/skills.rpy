
init python:

#####################################################################################################################################################

    class game_skill(store.object):
        def __init__(self):
            self.level = 1
            self.invested = 0
            self.current = 1
            
        def GetName(self):
            return get_var_suffix(self, "loc")

        def GetDesc(self):
            return get_var_suffix(self, "desc")

        def GetQuote(self):
            return get_var_suffix(self, "quote")

########################

    def game_skill_roll(skill, difficulty, skill_buffs = []):
        global skill_success, available_skill_buffs , used_skill_buffs
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        roll = dice1 + dice2 + dice3

        total = roll + skill.level

        sum_buffs = 0
        for buff in skill_buffs:
            if buff in available_skill_buffs :
                sum_buffs = sum_buffs + buff.value
                buff.times_used += 1
                if buff.limit <> 0 and buff.times_used >= buff.limit:
                    available_skill_buffs .remove(buff)
                    used_skill_buffs.append(buff)
        total = total + sum_buffs

        skill_success = total >= difficulty

        renpy.call("skill_test_label", total, difficulty, dice1, dice2, dice3, skill,skill_buffs )

##########################

    def add_skill_buff(skill_buff):
        global available_skill_buffs , used_skill_buffs
        if skill_buff not in available_skill_buffs  and skill_buff not in used_skill_buffs:
            available_skill_buffs .append(skill_buff)

##########################

    def rollchance(skill,difficulty,skill_buffs = []):
        global available_skill_buffs
        die_table = {
            "die_3" : 1,
            "die_4" : 0.9954,
            "die_5" : 0.9815,
            "die_6" : 0.9537,
            "die_7" : 0.9074,
            "die_8" : 0.8380,
            "die_9" : 0.7407,
            "die_10" : 0.6250,
            "die_11" : 0.5,
            "die_12" : 0.3750,
            "die_13" : 0.2593,
            "die_14" : 0.1620,
            "die_15" : 0.0926,
            "die_16" : 0.0463,
            "die_17" : 0.0185,
            "die_18" : 0.0046,
            "die_impossible" : 0
        }

        difficulty -= skill.level
        for buff in skill_buffs:
            if buff in available_skill_buffs:
                difficulty -= buff.value

        if difficulty <= 3:
            difficulty = 3
        if difficulty > 18:
            difficulty = "impossible"
        chance = die_table["die_%r" % difficulty]

        return round(chance*100)

##########################

    class skill_check_buff(store.object):
        def __init__(self, value , limit = 0):
            self.times_used = 0
            self.value = value
            self.limit = limit
        def GetName(self):
            return get_var_suffix(self, "loc")