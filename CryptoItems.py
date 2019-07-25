
from Engine import Engine, Entity, Player, Command
from GameUtils import command_travel, command_pick_up, command_equip, command_attack, command_buy, add_descriptions
from BlockChainFuncs import *
from enum import Enum

'''
(1) - Equipment/ItemType
1 : OneHand
2 : TwoHand
3 : LegArmor
4 : Torso
5 : Boots
6 : Hands
7 : Hemlet
8 : auxiliary
9 : useItem

(2) - MagicRating
(3) - Damage
(4) - ArmorAdded 
(5) - Uses
(6) - Special
'''

class ItemTypes(Enum):
    ONEHAND = '1'
    TWOHAND = '2'
    LEGS = '3'
    CHEST = '4'
    FEET = '5'
    HANDS = '6'
    HEAD = '7'
    AUX = '8'
    USE = '9'

class CryptoItems:

    def __init__(self):
        self.cryptoItemsDict = dict()
        self.importCryptoItems()


    def createCryptoItem(self, name, description, examine):
        Item = Entity([name])
        Item.add_name(name)

        stats = getItemStatsBlockchainByName(name)
        if len(stats) != 8:
            print("couldn't find item on blockchain")
        
        #"equipement" : {"head":"", "torso": "", "hands":"", "feet":"", "auxiliary":"", "weapon":""}
        equipment = ""
        if stats[0] == ItemTypes.ONEHAND.value:
            equipment = "weapon"
        elif stats[0] == ItemTypes.TWOHAND.value:
            equipment = "weapon"
        elif stats[0] == ItemTypes.LEGS.value:
            equipment = "feet"
        elif stats[0] == ItemTypes.CHEST.value:
            equipment = "torso"
        elif stats[0] == ItemTypes.FEET.value:
            equipment = "feet"
        elif stats[0] == ItemTypes.HANDS.value:
            equipment = "hands"
        elif stats[0] == ItemTypes.HEAD.value:
            equipment = "head"
        elif stats[0] == ItemTypes.AUX.value:
            equipment = "auxiliary"
        elif stats[0] == ItemTypes.USE.value:
            equipment = "item"

        Item.data = {"equip": equipment, "damage": stats[2], "armor": stats[3], "magicRating": stats[1], "price":getPrice(name)}
        addr = getItemAddressBlockchain(name)
        Item.id = addr
        if getIsPurchasable(name):
            Item.add_command(command_buy(Item))
        
        add_descriptions(Item, description, examine)

        return Item

    def get_crypto_items_dict(self):
        return self.cryptoItemsDict

    def get_crypto_items_list(self):
        l = []
        for key in self.cryptoItemsDict:
            l.append(self.cryptoItemsDict[key])
        return l;

    def createItems(self):

        build_item("Potato", [9,0,0,0,1,5,0,0], 50000, True)
        build_item("Carrot", [9,0,0,0,1,4,0,0], 50000, True)
        build_item("GoldenDagger", [1,1,3,1,0,0,0,0], 10000000, True)
        build_item("ShinyShield", [1,0,0,7,0,0,0,0], 2000000, True)
        build_item("AmuletOfDragonsFire", [8,0,30,1,5,0,0,0], 280000000, True)
        build_item("Parrot", [9,0,0,0,0,0,0,0], 120000, True)
        build_item("Bow", [2,0,20,0,0,0,0,0], 9000000, True)
        build_item("LeggingsOfIncredibleTightness", [3,0,0,4,0,0,0,0], 6000000, True)
        build_item("HelmetOfCrockpots", [7,0,0,4,0,0,0,0], 3000000, True)
        build_item("GauntletsOfOgers", [6,5,3,10,0,0,0,0], 500000000, True)
    

    def importCryptoItems(self):
        self.cryptoItemsDict["Potato"] = self.createCryptoItem("Potato", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["Carrot"] = self.createCryptoItem("Carrot", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["GoldenDagger"] = self.createCryptoItem("GoldenDagger", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["ShinyShield"] = self.createCryptoItem("ShinyShield", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["AmuletOfDragonsFire"] = self.createCryptoItem("AmuletOfDragonsFire", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["Parrot"] = self.createCryptoItem("Parrot", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["Bow"] = self.createCryptoItem("Bow", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["LeggingsOfIncredibleTightness"] = self.createCryptoItem("LeggingsOfIncredibleTightness", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["HelmetOfCrockpots"] = self.createCryptoItem("HelmetOfCrockpots", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")
        self.cryptoItemsDict["GauntletsOfOgers"] = self.createCryptoItem("GauntletsOfOgers", "A feriatceous tuber", "it's a potato, it may not be useful now, but the devs love these")


    def __repr__(self):
        return "engine for storeing and creating items"


    