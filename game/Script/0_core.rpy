init python:


    # Function that takes the name of a given variable and return as a string
    def get_var_name(var, scope):
        return [name for name in scope if scope[name] is var]

    # Function that takes one string, add something to it and return as a variable name

    def get_var_suffix(var, suffix, scope=globals()):
        var_loc = get_var_name(var, scope)[0]
        var_new_loc = "{0}_{1}".format(var_loc, suffix)
        return globals()[var_new_loc]
