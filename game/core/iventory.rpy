
init python:

#####################################################################################################################################################

    class game_item(store.object):
        def __init__(self, icon, name, desc, game_label, interaction_mode=0):
            self.icon = icon
            self.name = name
            self.desc = desc
            self.game_label = game_label
            self.interaction_mode = interaction_mode
            self.characters_shown = []

    def inspect_item(item):
        renpy.hide_screen("inventory_screen")
        #renpy.show_screen("inventory_screen")
        #renpy.say("", "Annoying shit")
        #renpy.call(item.game_label)
        #renpy.jump(item.game_label)