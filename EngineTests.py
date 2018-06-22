from Engine import Engine, Entity, Player, Command



def test_registration(engine):
    id = 1
    if (engine.register_player_id(id)):
        print("should be blank [" +engine.players[id].get_name() + "]")
    if (engine.register_player_name(id, "evan")):
        print("successfully registered name: " + engine.players[id].get_name())
    if (engine.register_player_description(id, "tall and good")):
        print("successfully registered description: " + engine.players[id].get_examine_description())
    

def test():
    engine = Engine(lambda player: player.speak_to_player("sup"))
    test_registration(engine)

test()