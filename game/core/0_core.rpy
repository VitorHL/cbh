#init offset = -2

init python:

    # Basic functions


    # Function that takes the name of a given variable and return as a string
    def get_var_name(var, scope):
        return [name for name in scope if scope[name] is var]

    # Function that takes one string, add something to it and return as a variable name
    def get_var_suffix(var, suffix, scope=globals()):
        var_loc = get_var_name(var, scope)[0]
        var_new_loc = "{0}_{1}".format(var_loc, suffix)
        return globals()[var_new_loc]

    # Function that stops the talking animation once the text is done showing
    def callback_builder(character_sprite_basename):
        def char_callback(event, **kwargs):
            if event == "show_done":
                # Get current attributes and add "talk"
                current_attrs = renpy.get_attributes(character_sprite_basename)
                if current_attrs and "talk" not in current_attrs:
                    new_attrs = list(current_attrs) + ["talk"]
                    renpy.show(character_sprite_basename, at_list=[], layer="master", what=None, zorder=None, tag=None, behind=[])
                    # Use the proper show syntax
                    renpy.show(character_sprite_basename + " " + " ".join(new_attrs))
            elif event == "slow_done":
                # Get current attributes and remove "talk"
                current_attrs = renpy.get_attributes(character_sprite_basename)
                if current_attrs:
                    attrs_without_talk = [attr for attr in current_attrs if attr != "talk"]
                    renpy.show(character_sprite_basename + " " + " ".join(attrs_without_talk))
                    renpy.restart_interaction()
        return char_callback