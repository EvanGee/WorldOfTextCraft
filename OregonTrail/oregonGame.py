#!/usr/bin/python3
"""
Higher level game logic
"""
import sys
sys.path.append("./")
from Engine import Engine, Entity, Player, Command
from Kansas import *

def Iowa(room_routes):
    city = Entity(["city", "Iowa"])
    city.add_description("It is Iowa city")
    city.add_examine_description("You can't be more exited to leave this place")
    return city

def test_start(engine):
    player_one = engine.new_player(1, "evan")
    player_one.add_description("Evan")
    player_one.add_examine_description("a tall man")
    commands = [
        "*explore city",
        "*explore small shop",
        "*examine small shop",
        "*explore man",
        "*examine man",
        "*talk to man",
        #"*explore house",
        #"* explore woman",
        #"*take snacks",
        #"*i evan",
        #"*examine car",
        #"* go to Iowa",
        #"* explore city",
    ]
    for command in commands:
        engine.parse_command(player_one, command)



def oreganTrailWelcomeMessage(player):
    player.speak_to_player("You start your journey in Kanzas city, a town known for its....Jazz?")
    player.speak_to_player("You have to find a way with your friends to get to Oregon where you have a job interview for a shit paying job that no one wants")
    player.speak_to_player("Anyway, you're a millenial, so you have no money and everyone treats you like garbage, good luck!")


def welcomeMessage(player):
    player.speak_to_player("-------------------------------------------------------------------")
    player.speak_to_player("welcome to WorldOfTextCraft-Oregan Trail, Millenial edition! " + player.get_name() + "!!!")
    player.speak_to_player("if you just type something it will broadcast to all players. ")
    player.speak_to_player("if you type '*' and then a command we will try to figure it out. ")
    player.speak_to_player("*i [yourName] -- this will diplay your items. ")
    player.speak_to_player("*explore [target]  -- this will give you an overview of the target ")
    player.speak_to_player("*examine [target]  -- this will give you a closer view of the target ")
    player.speak_to_player("-------------------------------------------------------------------")
    oreganTrailWelcomeMessage(player)


def create_game():
    engine = Engine(welcomeMessage)
    engine.add_room("Iowa", Iowa(engine))
    engine.add_room("Kansas", Kansas(engine))
    engine.start_room("Kansas")
    

    engine.run()
    #test_start(engine)
    
#test()
if __name__ == "__main__":
    create_game()