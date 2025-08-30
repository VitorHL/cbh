init python:
    import renpy.store as store
    import renpy.exports as renpy


    #Function used for the plus and minus buttons for adding or removing points in the skill menu

    def add_skill_point(skill, quantity):
        global att_pts_spent, att_pts_available
        skill.invested += quantity
        skill.current = skill.level + skill.invested
        att_pts_spent += quantity
        att_pts_available -= quantity


    #Function used for the Reset burtton in the skill menu

    def reset_skill_points ():
        global att_pts_available, att_pts_spent
        att_pts_available = att_pts_available + att_pts_spent
        att_pts_spent = 0
        for i in game_skills:
            i.invested = 0

    def apply_skill_points ():
        global att_pts_available, att_pts_spent
        att_pts_spent = 0
        for i in game_skills:
            i.level = i.current
        reset_skill_points()
