
import sys
sys.path.append("./")

from Engine import Engine, Entity, Player, Command
from GameUtils import command_travel, command_pick_up

def Table(engine):
    table = Entity(["table"])
    table.add_description("Wooden table")
    table.add_examine_description("a wooden table, it looks like a good place to place things")
    table.add_entity(Chair(engine, 1))
    table.add_entity(Chair(engine, 2))
    return table

def Chair(engine, id):
    chair = Entity(["chair"+str(id)])
    chair.add_description("Wooden chair" + str(id))
    chair.add_examine_description("its sturdy, you could 'sit' on it, or maybe 'use' it as a weapon.")
    return chair

def Tavern(engine):
    tavern = Entity(["tavern"])
    tavern.add_description("The Oily Rat tavern is alive and well! patrons from nearby towns gather to hear what quests the curier has to offer!")
    tavern.add_examine_description("The tavern is sturdily built, its location at the county's crossroads makes it an ideal place meet")
    tavern.add_entity(Table(engine))

    return tavern
