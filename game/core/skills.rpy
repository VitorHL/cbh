
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

    def game_skill_roll(skill, difficulty, skill_buffs = [], roll_id=None):
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
                if buff.limit != 0 and buff.times_used >= buff.limit:
                    available_skill_buffs .remove(buff)
                    used_skill_buffs.append(buff)
        total = total + sum_buffs

        # Determine success
        roll_result = total >= difficulty
        skill_success = roll_result

        # Record the Result
        register_skill_roll_result(roll_id, roll_result)

        renpy.call_in_new_context("skill_test_label", total, difficulty, dice1, dice2, dice3, skill,skill_buffs )

        

##########################

    def add_skill_buff(skill_buff):
        global available_skill_buffs , used_skill_buffs
        if skill_buff not in available_skill_buffs  and skill_buff not in used_skill_buffs:
            available_skill_buffs.append(skill_buff)

##########################

    def rollchance(skill, difficulty, skill_buffs=None):
        if skill_buffs is None:
            skill_buffs = []
        
        # More readable table
        SUCCESS_PROBABILITIES = {
            3: 1.0000,
            4: 0.9954,
            5: 0.9815,
            6: 0.9537,
            7: 0.9074,
            8: 0.8380,
            9: 0.7407,
            10: 0.6250,
            11: 0.5000,
            12: 0.3750,
            13: 0.2593,
            14: 0.1620,
            15: 0.0926,
            16: 0.0463,
            17: 0.0185,
            18: 0.0046,
        }
        
        # Calculate effective difficulty
        effective_difficulty = difficulty - skill.level
        
        for buff in skill_buffs:
            if buff in available_skill_buffs:
                effective_difficulty -= buff.value
        
        # Clamp to valid range
        effective_difficulty = max(3, min(18, effective_difficulty))
        
        if effective_difficulty > 18:
            return 0
        
        return round(SUCCESS_PROBABILITIES[effective_difficulty] * 100)

##########################

    class skill_check_buff(store.object):
        def __init__(self, value , limit = 0):
            self.times_used = 0
            self.value = value
            self.limit = limit
        def GetName(self):
            return get_var_suffix(self, "loc")

######################################################################################################################################################

    def get_difficulty_descriptor(DC):
        """
        Returns a difficulty descriptor based on success chance percentage.
        """
        difficulty_ranges = [
            (3, 5, "TRIVIAL"),
            (6, 8, "EASY"),
            (9, 11, "MODERATE"),
            (12, 14, "CHALLENGING"),
            (15, 17, "DIFFICULT"),
            (18, 18, "HEROIC"),
        ]
        
        for min_val, max_val, descriptor in difficulty_ranges:
            if min_val <= DC <= max_val:
                return descriptor
        
        return "UNKNOWN"  # Fallback, should never happen

    def get_difficulty_color(DC):
        """
        Returns a color based on difficulty level.
        """
        descriptor = get_difficulty_descriptor(DC)
        
        color_map = {
            "TRIVIAL": "#95c795",
            "EASY": "#a0c089",
            "MODERATE": "#abb87d",
            "CHALLENGING": "#b6af71",
            "DIFFICULT": "#c1a665",
            "HEROIC": "#c76363",
            "UNKNOWN": "#808080"  # gray fallback
        }
    
        return color_map.get(descriptor, "#808080")