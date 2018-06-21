#!/usr/bin/python3
"""
Higher level game logic
"""

from evansEngine import Engine, Entity, Player, Command

def travel(entities, player):
    player.move(entities[0])


def Kansas(room_containers):
    city = Entity(["city", "kanzas"])
    city.add_description("It is Kanzas city, it smells of barbecue chicken and craft beer")
    city.add_examine_description("You can't be more exited to leave this place")

    nextCity = Entity(["iowa"])
    nextCity.add_command(Command(travel, ["go", "travel"], [room_containers['Iowa']]))
    nextCity.add_description("There is a highway, and a roadsign that says 'next stop Iowa'")
    nextCity.add_examine_description("The road looks arduous")

    house = Entity(["house"])
    house.add_description("A small suburban house with a white picket fence (your house)")
    house.add_examine_description("your parents house")

    car = Entity(["car"])
    car.add_description("There is a car in your parents driveway, its a 1995 honda civic, it might get you to oregon...")
    car.add_examine_description("It looks like solid reliable transportation, its old but trusty, can fit a cramped 4, and has a full tank of gas")

    mom = Entity(["Mom", "lady", "parents", "woman"])
    mom.add_description("There is an older woman standing in your driveway")
    mom.add_examine_description("She says to you 'Hey, make sure to pack before you go, '")

    city.add_entity(nextCity)
    city.add_entity(house)
    house.add_entity(car)
    house.add_entity(mom)
    
    return city

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
        "* explore city",
        #"* explore house",
        #"* explore woman",
        #"* i evan",
        #"* examine car",
        "* go to Iowa",
        "* explore city",
    ]
    for command in commands:
        engine.parse_command(player_one, command)

def oreganTrailWelcomeMessage(player):
    player.speak_to_player("You start your journey in Kanzas city, a town known for its....Jazz?")
    player.speak_to_player("You have to find a way with your friends to get to Oregon where you have a job interview for a shit paying job that no one wants")
    player.speak_to_player("Anyway, your a millenial, so you have no money and everyone treats you like garbage, good luck!")


def welcomeMessage(player):
    player.speak_to_player("-------------------------------------------------------------------")
    player.speak_to_player("welcome to WorldOfTextCraft-Oregan Trail, Millenial edition! " + player.get_name() + "!!!")
    player.speak_to_player("Im pretty exited you decided to play! Here are some tips: ")
    player.speak_to_player("if you just type something it will broadcast to all players. ")
    player.speak_to_player("if you type '*' followed by a space, we will try to figure it out. ")
    player.speak_to_player("* i [yourName] -- this will diplay your items. ")
    player.speak_to_player("* explore room  -- this will give you an overview of the room ")
    player.speak_to_player("* examine [target of interest]  -- this will give you a closer view of the target ")
    player.speak_to_player("-------------------------------------------------------------------")
    oreganTrailWelcomeMessage(player)


def create_game():
    room_containers = dict()
    room_containers["Iowa"] = Iowa(room_containers)
    room_containers["Kansas"] = Kansas(room_containers)
    engine = Engine(room_containers["Kansas"], room_containers, welcomeMessage)

    
    #engine.run()
    test_start(engine)
    
#test()
if __name__ == "__main__":
    create_game()