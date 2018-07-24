
import sys
sys.path.append("./")

from Engine import Engine, Entity, Player, Command
from GameUtils import command_travel, command_pick_up, command_equip, command_attack



def dagger(id):
    dagger = Entity(["dagger"])
    dagger.add_description("A small rusty dagger")
    dagger.add_examine_description("this dagger looks like it could do a little bit of damage")
    dagger.data = {"equip": "weapon", "damage": 1}
    dagger.add_name("dagger")
    dagger.add_command(command_equip(dagger))
    dagger.add_command(command_pick_up(dagger))
    return dagger

def Table(id):
    table = Entity(["table"+str(id)])
    table.add_name("wooden table")
    table.add_description("a simple wooden table"+str(id))
    table.add_examine_description("a wooden table, it looks like a good place to place things, you could go to the table if you wished")
    table.data = {"health" : 1}
    table.add_entity(Chair(1))
    table.add_entity(Chair(2))
    table.add_command(command_travel(table))
    table.add_entity(dagger(""))
    table.add_command(command_attack(table))
    return table

def Chair(id):
    chair = Entity(["chair"+str(id)])
    chair.data = {"health" : 1}
    chair.add_description("Wooden chair" + str(id))
    chair.add_examine_description("its sturdy, you could 'sit' on it, or maybe 'use' it as a weapon.")
    chair.add_command(command_pick_up(chair))
    chair.add_command(command_attack(chair))
    return chair

def Tavern(engine):
    tavern = Entity(["tavern"])
    tavern.add_description("The Oily Rat tavern is alive and well! patrons from nearby towns gather to hear what quests the curier has to offer!")
    tavern.add_examine_description("The tavern is sturdily built, its location at the county's crossroads makes it an ideal place meet")
    tavern.add_entity(Table(""))
    return tavern
