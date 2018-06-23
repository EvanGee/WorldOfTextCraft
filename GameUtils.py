from Engine import Engine, Entity, Player, Command

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