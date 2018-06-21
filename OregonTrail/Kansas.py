
from Engine import Engine, Entity, Player, Command

from gameFunctions import *


def TalkToShopOwner(entities, player):
    owner = entities[0]
    player.speak_to_player("Welcome! to Gary's  goods, we have a wide selection....oh, you're a melenial? listen, just go home and see "
    +"if your parents will give you what you need, I don't have time for privilaged brats.... Oh you're still here? well very well here is some garbage")
    player.speak_to_player("To select an item type *buy #")
    player.speak_to_player("1: Garbage")

def KansasStore(): 
    store = Entity(["shop", "store"])
    store.add_description("Small Shop")
    store.add_examine_description("The shop sign reads 'Gary's goods - take as much as you can cary' maybe they have supplies")
    store.add_command(Command(KansasStore, ["go"], [store]))

    owner = Entity(["gary", "owner", "man"])
    owner.add_description("There is a flamboyant man wearing purple robes and a wizard hat, hes probably the owner")
    owner.add_examine_description("he's in his 50's maybe, looks like hes had a hard life")
    owner.add_command(Command(TalkToShopOwner, ["talk", "ask", "converse", "say"], [owner]))

    store.add_entities([owner])
    return store

def KansasHouse():

    house = Entity(["house"])
    house.add_description("A small suburban house with a white picket fence (your house)")
    house.add_examine_description("your parents house")
    
    car = Entity(["car"])
    car.add_description("There is a car in your parents driveway, its a 1995 honda civic, it might get you to oregon...")
    car.add_examine_description("It looks like solid reliable transportation, its old but trusty, can fit a cramped 4, and has a full tank of gas")

    mom = Entity(["mom", "lady", "parents", "woman"])
    mom.add_description("There is an older woman standing in your driveway")
    mom.add_examine_description("She says to you 'Hey, make sure to pack before you go, '")

    snacks = Entity(["money"])
    snacks.add_description("Maybe she has some money if you ask nicely")
    snacks.add_examine_description("$100")
    snacks.add_command(Command(pickUpItems, ["take", "get", "ask", ], [snacks]))

    mom.add_entity(snacks)
    house.add_entity(car)
    house.add_entity(mom)
    return house

def Kansas(engine):
    city = Entity(["city", "kanzas"])
    city.add_description("It is Kanzas city, it smells of barbecue chicken and craft beer")
    city.add_examine_description("You can't be more exited to leave this place")

    nextCity = Entity(["iowa"])
    nextCity.add_command(Command(travel, ["go", "travel"], [engine.get_room('Iowa')]))
    nextCity.add_description("There is a highway, and a roadsign that says 'next stop Iowa'")
    nextCity.add_examine_description("The road looks arduous")

    city.add_entity(nextCity)
    city.add_entity(KansasHouse())
    city.add_entity(KansasStore())
    
    return city