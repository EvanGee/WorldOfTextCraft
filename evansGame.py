#!/usr/bin/python3
"""
Higher level game logic
"""

from evansEngine import Engine, Entity, Player, Command
from rooms import start_room, wonderland_room, wonderland_room_welcome, test

def welcomeMessage(player):

    player.speak_to_player("-------------------------------------------------------------------")
    player.speak_to_player("welcome to Zork&Pals! " + player.get_name() + "!!!")
    player.speak_to_player("Im pretty exited you decided to play! Here are some tips: ")
    player.speak_to_player("if you just type something it will broadcast to all players. ")
    player.speak_to_player("if you type '*' followed by a space, we will try to figure it out. ")
    player.speak_to_player("* i [yourName] -- this will diplay your items. ")
    player.speak_to_player("* explore room  -- this will give you an overview of the room ")
    player.speak_to_player("* examine [target of interest]  -- this will give you a closer view of the target ")
    player.speak_to_player("-------------------------------------------------------------------")
    wonderland_room_welcome(player)


def create_game():


    rooms_containers = dict()
    room = wonderland_room(rooms_containers)
    rooms_containers["start"] = room
    engine = Engine(room, rooms_containers, welcomeMessage)
    engine.run()

    #rooms_containers = dict()
    #room = start_room(rooms_containers)
    #rooms_containers["start"] = room
    #game = Engine(room, rooms_containers, welcomeMessage)
    #game.run()


test()
if __name__ == "__main__":
    create_game()