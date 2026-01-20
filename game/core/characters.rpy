
init python:

    ########################################################################################################################################################

    class game_character(store.object):
        def __init__(self, name,game_label, small_talk_game_label, generic_show_label):
            self.name = name
            self.game_label = game_label # The intro dialogue played when you click in the character
            self.small_talk_game_label = small_talk_game_label
            self.generic_show_label = generic_show_label
            self.interested_talks = {}
            self.interested_items = {}
            self.relevant_itens = []
            self.flags = {}

            def add_talk(self, topic, dialogue):
                self.interested_talks[topic] = dialogue
            
            def add_item_reaction(self, item, reaction):
                self.interested_items[item] = reaction
            
            def set_flag(self, flag_name, value):
                self.flags[flag_name] = value

            def remove_talk(self, topic):
                if topic in self.interested_talks:
                    del self.interested_talks[topic]
            
            def remove_item_reaction(self, item):
                if item in self.interested_items:
                    del self.interested_items[item]
            
            def remove_flag(self, flag_name):
                if flag_name in self.flags:
                    del self.flags[flag_name]

#####################################################################################################################################################

    def generate_character_talks(character):
        """
        Creates a Ren'Py menu from a class object's interested_talks dictionary.
        
        Args:
            class_object: Object with interested_talks dictionary attribute
            
        Returns:
            The result of renpy.display_menu()
        """
        # Create tuples from the interested_talks dictionary
        menu_items = []
        label = "gia_show_coke"
        
        for key, value in character.interested_talks.items():
            # Create a lambda that captures the current value and class_object
            # This ensures the correct values are used when the menu item is selected
            menu_action = lambda v=value, obj=character: renpy.call(v, obj)
            
            # Create tuple: (display_text, action_function)
            menu_items.append((key, renpy.Choice(None, game_label=value, character=character) ))
        
        # Feed the tuple list to renpy.display_menu
        return renpy.display_menu(menu_items,"",interact=True,screen="choice_talks", args=[("character",character)])