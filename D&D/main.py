#!/usr/bin/python3
"""
Higher level game logic
"""
import sys
sys.path.append("./")
from Engine import Engine, Entity, Player, Command
from GameUtils import create_character
from tavern import *

def test_start(engine):
    id = 1
    engine.register_player_id(id)
    engine.register_player_name(id, "Evan")
    engine.register_player_description(id, "tall and good")
    create_character(engine, id)

    commands = [
        "*e",
        #"*ex tavern",
        #"*e table",
        "*go to table",
        "*e",
        #"*e",
        #"*ex",
        #"*i",
        "*get chair1",
        "*e",
        "*i",
        "*get dagger",
        "*e",
        #can't equip if in inventory
        "*equip dagger",
        #"*i",
        #"*e",
        "*attack table"
        #"*back",
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
    player.speak_to_player("*i [player] -- this will diplay items. '*i' to check your own quickly.")
    player.speak_to_player("*explore [target]  -- this will give you an overview of the target 'e' for short.")
    player.speak_to_player("*examine [target]  -- this will give you a closer view of the target 'ex' for short.")
    player.speak_to_player("*equip   [target]  -- this will equip your character with an item from your inventory.")
    player.speak_to_player("*back -- will bring you to the room you came from.")
    player.speak_to_player("*attack  [target]  -- will attack the target with your currently equiped weapon.")
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