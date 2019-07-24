from Engine import Engine, Entity, Player, Command
from BlockChainFuncs import *


def pickUpItems(entities, player):
    if entities[0].current_parent.is_player:
        return
    entities[0].move(player)

def travel(entities, player):
    player.move(entities[0])

def broadcast(entities, player):
    engine.broadcast_msg(player, entities[0])

def command_travel(room):
    return Command(travel, ["go", "travel"], [room])

def command_pick_up(item):
    return Command(pickUpItems, ["get", "pick"], [item])

def command_use_item(item):
    return Command(use_item, ["use"], [item])

def use_item(entities, player):
    return

def equip_item(entities, player):
    equipement = entities[0]
    if (equipement.current_parent != player):
        player.speak_to_player("Cannot equip " + equipement.get_name() +", it's not in your inventory")
        return
    player.data["equipment"][equipement.data["equip"]] = equipement.data
    player.speak_to_player("equiped " + equipement.get_name())

def command_equip(item):
    return Command(equip_item, ["equip"], [item])

def attack(entities, player):
    enemy = entities[0]

    print(player.data["equipement"])

    if(player.data["equipement"]["weapon"] == ""):
        player.speak_to_player("no weapon equiped.")
        return

    enemy.data["health"] -= player.data["equipement"]["weapon"]["damage"]
    if (enemy.data["health"] < 1):
        player.speak_to_player("you killed the " + enemy.get_name())
    else:
        player.speak_to_player("you damaged " + enemy.get_name())

def command_attack(target):
    return Command(attack, ["attack"], [target])

def buy(entities, player):
    item = entities[0]
    player.speak_to_player("buy:"+item.id+"")

def command_buy(target):
    return Command(buy, ["buy"], [target])


     