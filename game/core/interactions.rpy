
init 0:
    default interactions_played_today  = []

init python:
    

#####################################################################################################################################################


    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds), loop=True)
        

        elif event == "slow_done" or event == "end":
            renpy.sound.stop(fadeout=1.0)

#####################################################################################################################################################

    class game_interaction(store.object): 
        def __init__(self,game_label,**kwargs):
            self.game_label = game_label
            self.state = 0 # used mainly to set this interaction in diferent "modes"
            self.runs = 0
            self.runs_today = 0

    def run_interaction(interaction_to_run):
        global available_interactions, ongoing_interaction
        if not available_interactions or interaction_to_run in available_interactions:
            ongoing_interaction = interaction_to_run
            renpy.call(interaction_to_run.game_label)
        else:
            renpy.say("", cdt_message )

    def end_interaction():
        global available_interactions, ongoing_interaction, interactions_played_today
        ongoing_interaction.runs += 1
        ongoing_interaction.runs_today += 1
        interactions_played_today.append(ongoing_interaction)
        del ongoing_interaction
        renpy.return_statement()