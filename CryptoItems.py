from BlockChainFuncs import *


from Engine import Engine, Entity, Player, Command
from GameUtils import command_travel, command_pick_up, command_equip, command_attack

def luckyDragonGoldenDagger():




def luckyDragonGoldenDagger(id):
    dagger = Entity(["luckyDragonGoldenDagger"])
    dagger.add_description("A small rusty dagger")
    dagger.add_examine_description("this dagger looks like it could do a little bit of damage")
    dagger.data = {"equip": "weapon", "damage": 1}
    dagger.add_name("dagger")
    dagger.add_command(command_equip(dagger))
    dagger.add_command(command_pick_up(dagger))
    return dagger