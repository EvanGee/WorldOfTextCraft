#!/usr/bin/python3
"""
Higher level game logic
"""

from Engine import Engine, Entity, Player, Command
from World import *
from CryptoItems import CryptoItems
from BlockChainFuncs import *

def test_start(engine):
    id = "0xcca4d2b2a1a38e8030c33861b97108680cd28cf0"
    engine.register_player_id(id)
    engine.register_player_name(id, "Evan")
    engine.register_player_description(id, "tall and good")
    

    #print("GETTING PLAYER OWNER" + str(getPlayerOwner("0xcca4d2b2a1a38e8030c33861b97108680cd28cf0")))
    #print("GETTING PLAYER OWNER" + str(getPlayerOwner("0xa78a5ec4d0bc1c1321729cbf18ffb8d9a588e775")))

    commands = [
        #"e",
        #"*ex tavern",
        #"*e table",
        #"go to table",
        #"e",
        #"*e",
        #"*ex",
        #"*i",
        #"get chair1",
        #"e",
        #"i",
        #"get dagger",
        #"e",
        #can't equip if in inventory
        #"equip dagger",#
        #"*e",
        #"attack table"
        #*back",
        #"stats",
        #"stats table"
        "e",
        "ex tavern",
        "ex store",
        "go store",
        "e",
        "ex",
        "ex Potato",
        "stats Potato",
        "stats GauntletsOfOgers",
        "stats Potato",
        "back",
        "e"
    ]

    for command in commands:
        engine.parse_command(engine.players[id], command)



def WelcomeMessage(player):
    player.speak_to_player("The 'Oily Rat' tavern smells of alcohol and is filled with jubilus singing. The night air is alive with energy as adventurers from nabouring "+
    "villages drink merily and converse as they wait eagerly for the summons to adventure. Every month, a currier comes from the capital to distribute quests to any adventurer willing to take up the cause."+
    "What awaits you? try to explore the tavern, introduce yourselfs to the locals!")


def welcomeMessage(player):
    player.speak_to_player("-------------------------------------------------------------------")
    player.speak_to_player("welcome to WorldOfTextCraft! " + player.get_name() + "!!!")
    player.speak_to_player("i [player] -- this will diplay items. 'i' to check your own quickly.")
    player.speak_to_player("explore [target]  -- (e for short) this will give you an overview of the target you can only type *e to explore your current room.")
    player.speak_to_player("examine [target]  -- (ex for short) this will give you a closer view of the target *ex to examine your current room.")
    player.speak_to_player("equip   [target]  -- this will equip your character with an item from your inventory.")
    player.speak_to_player("back -- will bring you to the room you came from.")
    player.speak_to_player("attack  [target]  -- will attack the target with your currently equiped weapon.")
    player.speak_to_player("go [target]    -- will move you to a different room if you can.")
    player.speak_to_player("get [target]      -- will allow you to pick up an item.")
    player.speak_to_player("say [target]      -- will talk to other players")
    player.speak_to_player("buy [target]      -- will allow you to purchase an Item if available for purchase")
    player.speak_to_player("-------------------------------------------------------------------")
    WelcomeMessage(player)


def create_game():
    #deployGameRegistry()
    #deployAllItems()
    cryptoItemEngine = CryptoItems()
    engine = Engine(welcomeMessage, create_character, cryptoItemEngine)
    engine.add_room("OilyRat", Tavern(cryptoItemEngine))

    engine.start_room("OilyRat")
    #engine.run()
    test_start(engine)
    
#test()
if __name__ == "__main__":
    create_game()