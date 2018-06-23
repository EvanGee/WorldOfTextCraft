from Engine import Engine, Entity, Player, Command


def create_character(engine, id):
    stats = {"attributes": {"str": 10, "dex":10, "con":10, "int": 10, "wis":10, "cha":10},
            "equipement" : {"head":"", "torso": "", "hands":"", "feet":"", "auxiliary":"", "weapon":""}
    }

    engine.players[id].data = stats



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
    print(equipement.get_name())
    player.data["equipement"][equipement.data["equip"]] = equipement.data

def command_equip(item):
    return Command(equip_item, ["equip"], [item])