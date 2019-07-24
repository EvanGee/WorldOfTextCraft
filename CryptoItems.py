
from Engine import Engine, Entity, Player, Command
from GameUtils import command_travel, command_pick_up, command_equip, command_attack, command_buy
from BlockChainFuncs import *

import json

#Read JSON data into the datastore variable
f = open("items.json", 'r')
jsonItems = json.load(f)


def loadCryptoItems():
    return


def luckyDragonGoldenDaggerBlockChain():
    name = "SexyItemTest"
    Item = Entity([name])
    Item.add_description("ITS A FUCKING DRAGON LOOKEN DAGGER " + "(" + name + ")")
    Item.add_examine_description("this dagger looks like it could do a little bit of damage")

    stats = getItemStatsBlockchainByName(name)
    if len(stats) != 8:
        print("couldn't find item on blockchain")

    print("item stats" + str(stats))
    
    Item.data = {"equip": "weapon", "damage": 1, "price":getPrice(name)}
    Item.add_name(name)
    #id needs to be set for buy/trade functions
    stats = getItemStatsBlockchainByName(name)
    addr = getItemAddressBlockchain(name)
    Item.id = addr
    Item.add_command(command_buy(Item))
    return Item

