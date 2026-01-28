
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
        global skill_success, available_skill_buffs, used_skill_buffs
        
        # Changed from 3d6 to 2d6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll = dice1 + dice2  # Now only 2 dice

        total = roll + skill.level

        sum_buffs = 0
        for buff in skill_buffs:
            if buff in store.available_skill_buffs:  # Use store explicitly
                sum_buffs = sum_buffs + buff.value
                buff.times_used += 1
                if buff.limit != 0 and buff.times_used >= buff.limit:
                    store.available_skill_buffs.remove(buff)
                    store.used_skill_buffs.append(buff)
        total = total + sum_buffs

        # Special rules: Natural 2 always fails, Natural 12 always succeeds
        if roll == 2:  # Snake eyes - always fail
            roll_result = False
        elif roll == 12:  # Boxcars - always succeed
            roll_result = True
        else:
            roll_result = total >= difficulty
        
        store.skill_success = roll_result  # Use store explicitly

        # Record the Result
        register_skill_roll_result(roll_id, roll_result)

        renpy.call_in_new_context("skill_test_label", total, difficulty, dice1, dice2, skill, skill_buffs)

        

##########################

    def add_skill_buff(skill_buff):
        if skill_buff not in store.available_skill_buffs and skill_buff not in store.used_skill_buffs:
            store.available_skill_buffs.append(skill_buff)

##########################

    def rollchance(skill, difficulty, skill_buffs=None):
        if skill_buffs is None:
            skill_buffs = []
        
        # 2d6 probability table
        SUCCESS_PROBABILITIES = {
            2: 1.0000,   # 100% - need 2 or higher
            3: 0.9722,   # 97.22%
            4: 0.9167,   # 91.67%
            5: 0.8333,   # 83.33%
            6: 0.7222,   # 72.22%
            7: 0.5833,   # 58.33%
            8: 0.4167,   # 41.67%
            9: 0.2778,   # 27.78%
            10: 0.1667,  # 16.67%
            11: 0.0833,  # 8.33%
            12: 0.0278,  # 2.78%
        }
        
        # Calculate effective difficulty
        effective_difficulty = difficulty - skill.level
        
        for buff in skill_buffs:
            if buff in available_skill_buffs:
                effective_difficulty -= buff.value
        
        # Clamp to valid range for 2d6 (2-12)
        if effective_difficulty <= 2:
            return 100
        if effective_difficulty > 12:
            return 3  # Still 2.78% chance due to natural 12 rule
        
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
        Returns a difficulty descriptor based on DC for 2d6 system.
        """
        difficulty_ranges = [
            (2, 6, "TRIVIAL"),      # Very easy
            (7, 8, "EASY"),         # Easy  
            (9, 10, "MODERATE"),     # Medium
            (11, 12, "CHALLENGING"), # Hard
            (13, 14, "HARD"),  # Very hard
            (15, 16, "VERY HARD"),     # Near impossible without buffs
            (17, 18, "EXTREME")
        ]
        
        for min_val, max_val, descriptor in difficulty_ranges:
            if min_val <= DC <= max_val:
                return descriptor
        
        return "HEROIC" if DC > 16 else "TRIVIAL"

    def get_difficulty_color(DC):
        """
        Returns a color based on difficulty level.
        """
        descriptor = get_difficulty_descriptor(DC)
        
        color_map = {
            "TRIVIAL": "#95c795",
            "EASY": "#9fc084",
            "MODERATE": "#a9b973",
            "CHALLENGING": "#b2b362",
            "HARD": "#b59f6e",
            "VERY HARD": "#c78254",
            "EXTREME": "#c76363",
            "HEROIC": "#c73232",
            "UNKNOWN": "#808080"  # gray fallback
        }
    
        return color_map.get(descriptor, "#808080")