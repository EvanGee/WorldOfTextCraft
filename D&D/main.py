#!/usr/bin/python3
"""
Higher level game logic
"""
import sys
sys.path.append("./")
from Engine import Engine, Entity, Player, Command
from tavern import *
def test_start(engine):
    id = 1
    engine.register_player_id(id)
    engine.register_player_name(id, "evan")
    engine.register_player_description(id, "tall and good")
    commands = [
        #"*explore tavern",
        #"*ex tavern",
        #"*e table",
        "*go to table",
        #"*ex chair1",
        "*e"

    ]
    for command in commands:
        engine.parse_command(engine.players[id], command)



def WelcomeMessage(player):
    player.speak_to_player("The tavern smells of alcohol and is filled with jubilus singing. The night air is alive with energy as adventurers from nabouring"+
    "villages drink merily and converse as they wait eagerly. Every month, a currier comes from the capital to distribute quests to any adventurer willing to take up the cause."+
    "What awaits you? try to explore the tavern")


def welcomeMessage(player):
    player.speak_to_player("-------------------------------------------------------------------")
    player.speak_to_player("welcome to WorldOfTextCraft! " + player.get_name() + "!!!")
    player.speak_to_player("if you just type something it will broadcast to all players. ")
    player.speak_to_player("if you type '*' and then a command we will try to figure it out. ")
    player.speak_to_player("*i [yourName] -- this will diplay your items. ")
    player.speak_to_player("*explore [target]  -- this will give you an overview of the target ")
    player.speak_to_player("*examine [target]  -- this will give you a closer view of the target ")
    player.speak_to_player("-------------------------------------------------------------------")
    WelcomeMessage(player)


def create_game():
    engine = Engine(welcomeMessage)
    engine.add_room("OilyRat", Tavern(engine))
    engine.start_room("OilyRat")
    
    #engine.run()
    test_start(engine)
    
#test()
if __name__ == "__main__":
    create_game()