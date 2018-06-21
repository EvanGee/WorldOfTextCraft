
from evansEngine import Engine, Entity, Player, Command, exploring_word_set, examine_word_set, action_word_set

#command functions
def broadcast(player, text):
    player.engine.broadcast_msg(player, text)
    
def getDescriptions(entities, player):
    for e in entities:
        player.speak_to_player(e.get_description())
        player.speak_to_player("")

def deepExplore(entities, player):
    for e in entities[0].get_entities():
        player.speak_to_player(e.get_description())
        player.speak_to_player("")

def deepExamine(entities, player):
    for e in entities[0].get_entities():
        e.examine(entities, player)
    
def examine(entities, player):
    player.speak_to_player(entities[0].get_examine_description())

def playRock(entities, player):
    player.speak_to_player("IIIiiii want to Rock and Roll allll nigggghhhhhhtttt...")
    broadcast(player, "some nerd is playing rock and roll way too loud")
    
def pickup(entities, player):
    player.get_entities().append(entities[0])
    player.speak_to_player("You picked up a rock")
    entities[0].add_description("its a rock, good for smashing, might make a nice pet")
    player.current_room.remove(entities[0])

def touchField(entities, player):
    Forcefield = entities[0]
    if Forcefield.get_description() == "The force field is down":
        player.speak_to_player("You exit the room")
    player.kill(entities, player)
    broadcast(player, "ZAAAAAAAAAAAAP" + player.get_name() + " is now a molten heap on the ground")

def attackPannelWithRock(entities, player):
    rock = entities[0]
    panel = entities[1]
    room = entities[2]
    door = entities[3]
    if (player.has_entity(rock) == False):
        player.speak_to_player("Maybe there is an item you can use!")
        return

    door.add_description("The force field is down")
    door.add_examine_description("Looks safe, it's off")
    player.speak_to_player("You brutally smash the panel! with a rock!")
    panel.add_description("The panel buzzes, electicity sparking off of it")
    panel.add_examine_description("The panel is broke af")
    player.speak_to_player(panel.get_description())
    room.add_description("The lights flicker on and off, something must have happened to the power, is the force field off?")
    broadcast(player, "SMASH BANG BANG " + player.get_name() + " is smashing the panel with the rock")

def start_room(room_dictionary):
#CREATE ENTITIES
    #Create Room
    room = Entity(["room", "around", "area"])
    room.add_description("""The room is cold, covered in steal, with a force field blocking your exit, there is a small panel on the wall that looks like it could be used to turn off the force field""")
    room.add_examine_description("its definetly a room")
    #Create Panel
    panel = Entity(["panel"])
    panel.add_description("There is a panel on the wall, it looks like some kind of control console")
    panel.add_examine_description("The panel hums, i wonder if you could damage it with something")

    #Add Rock
    rock = Entity(["rock", "weapon"])
    rock.add_description("There is  a rock...you know...a rock? on the ground")
    rock.add_examine_description("This looks like you could smash some serious face with this")

    #Add Forcefield
    door = Entity(["field", "door", "force", "exit"])
    door.add_description("A murderous hum eminates from the light enfused force field")
    door.add_examine_description("It looks dangerous, maybe you shouldn't touch it")

#ADD COMMANDS
    rock.add_command(Command(playRock, ["play"], []))
    room.add_command(Command(deepExplore, ["explore"], [room]))
    rock.add_command(Command(attackPannelWithRock, action_word_set, [rock, panel, room, door]))
    rock.add_command(Command(pickup, action_word_set, [rock]))
    door.add_command(Command(touchField, action_word_set, [door]))

 #ADD ENTITIES
    room.add_entity(panel)
    room.add_entity(rock)
    room.add_entity(door)
    return room

def wonderland_room_welcome(player):
    player.speak_to_player("As it turns out, Wonderland isn’t as wonderful as it seems… ")
    player.speak_to_player("""\
You’ve gone through the mirror and into the looking glass and explored Wonderland to your heart’s content. \
You’ve slain Jabberwockies, painted roses, and have had far too much pepper in, well… everything. All while \
being accosted by high-strung rabbits and philosophical cats. Strange. Whimsical. Eccentric. Wonderland is \
both wholly familiar and unfamiliar all at once. And yet, you find yourself wanting to leave.""")
    player.speak_to_player("")
    player.speak_to_player("""And yet… the longer you stay, the more you find yourself wholly unable to do so. Curiouser and curiouser…""")
    player.speak_to_player("")
    player.speak_to_player("""Luckily (or perhaps unluckily), the Red Queen has called for your heads, and her guards are quickly catching up. Follow the Cheshire Cat’s clues in order to retrace your steps, recover your bearings, and find your way out of Wonderland before it’s too late!""")
    player.speak_to_player("")

def start_room_test(engine):

    player_one = engine.new_player(1, "evan")
    player_one.add_description("A boy stands here")
    commands = [
        "* explore room", 
        #"* examine door",
        #"* look at force field",
        #"* touch force field"
        #"* explore panel",
        #"* smash panel",
        "* try rock",
        #"* play rock",
        "* use rock on panel",
        "* examine panel",
        "* explore room",


    ]
    for command in commands:
        engine.parse_command(player_one, command)

def takeCards(entities, player):
    hat = entities[3]
    for i in range(3):
        player.add_entity(entities[i])
        hat.remove(entities[i])

    player.speak_to_player("I took the cards")
    player.engine.broadcast_msg(player, player.get_name() + "reaches into the hat and places the three cards into their pocket")
    hat.add_description("A hat")
    hat.add_examine_description("Its a hat, someone took the playing cards out of it")

count = 0
def placeCardInFigurine(entities, player):
    card = entities[0]
    firgurine = entities[1]
    lock_box = entities[2]
    global count 
    if player.has_entity(card) == False:
        player.speak_to_player("Looks like I don't have the right items")
        return
    if card.get_description() == "three of hearts":
        player.speak_to_player("I place the three of hearts card on the horse with three legs in the air... The \
firgurine glows bright as its arms wrap around the card... its visage transforms into a nobel white night \
chess piece")
        player.remove(card)
        firgurine.add_examine_description("the red horse with three legs in the air is now a white knight chess piece ")
        count+=1

    elif card.get_description() == "ace of spades":
        player.speak_to_player("I place the ace of spades card on the black horse with one legs in the air... The \
firgurine glows bright as its arms wrap around the card... its visage transforms into a nobel white night \
chess piece")
        player.remove(card)
        firgurine.add_examine_description("the black horse with one legs in the air is now a white knight chess piece ")
        count+=1

    elif card.get_description() == "two of diamonds":
        player.speak_to_player("I place the two of diamonds card on the red horse with two legs in the air... The \
firgurine glows bright as its arms wrap around the card... its visage transforms into a nobel white night \
chess piece")
        player.remove(card)
        firgurine.add_examine_description("the red horse with two legs in the air is now a white knight chess piece ")
        count+=1

    if  count == 3:
        player.speak_to_player("The lockbox creaks open and a beautifu key appears... what could it be for!")
        player.speak_to_player("THANK YOU FOR PLAYING, that is as far as i got in this game jam, i built the engine \
for this game in 2 days, its far from perfect! ")
    

def wonderland_room(room_containers):
#CREATE ENTITIES
    room = Entity(["room", "around", "area"])
    room.add_description("In the center of the room, a giant chess game with red and white pieces.")

    #queen
    queen = Entity(["queen"])
    queen.add_description("Amongst the chess board stands a tall terrifying red queen wearing extravagant cloths")
    queen.add_examine_description("As I get closer to her, she follows me with her eyes, her stare is overwhelming \
I don't think i can pass""")

    #hat
    hat = Entity(["hat", "cards"])
    hat.add_description("Top hat with playing cards in the brim")
    hat.add_examine_description("the playing cards in the brim resinate with me, maybe I should take them...")

    #cards
    three_of_hearts = Entity(["three", "hearts"])
    three_of_hearts.add_description("three of hearts")
    three_of_hearts.add_examine_description("The card depicts a white chess piece, its the three of hearts, it looks like it could be `placed` somewhere")

    ace_of_spades = Entity(["ace", "spades"])
    ace_of_spades.add_examine_description("The card depicts a white chess piece, its the ace of spades, it looks like it could be `placed` somewhere")
    ace_of_spades.add_description("ace of spades")

    two_of_diamonds = Entity(["two", "diamonds"])
    two_of_diamonds.add_description("two of diamonds")
    two_of_diamonds.add_examine_description("The card depicts a white chess piece, its the two of diamonds, it looks like it could be `placed` somewhere")

    #figureins & lockbox
    lock_box = Entity(["lock", "box", "figurines", "lockbox", "ornate"])

    lock_box.add_description("In the corner of the room a dim light shines on a ornate lockbox.")
    lock_box.add_examine_description("The lock box has 3 horse figurines on top of it")

    three_of_hearts_horse = Entity(["horse", "hourse", "three", "hearts"])
    three_of_hearts_horse.add_examine_description("red horse with three hooves in the air")

    ace_of_spades_horse = Entity(["horse", "hourse", "ace", "spades"])
    ace_of_spades_horse.add_examine_description("black horse with one hoof in the air")

    two_of_diamonds_horse = Entity(["horse","hourse", "two", "diamonds"])
    two_of_diamonds_horse.add_examine_description("one red horse with 2 hooves in the air.")
    
    count = 0
    lock_box.add_command(Command(placeCardInFigurine, ["place"], [three_of_hearts, ace_of_spades, two_of_diamonds, lock_box, count]))
    lock_box.add_command(Command(deepExamine, ["examine"], [lock_box]))
    ##COMMANDS

    three_of_hearts.add_command(Command(placeCardInFigurine, ["place"], [three_of_hearts, three_of_hearts_horse, lock_box, count]))
    ace_of_spades.add_command(Command(placeCardInFigurine, ["place"], [ace_of_spades, ace_of_spades_horse, lock_box, count]))
    two_of_diamonds.add_command(Command(placeCardInFigurine, ["place"], [two_of_diamonds, two_of_diamonds_horse, lock_box, count]))

    hat.add_command(Command(takeCards, ["take", "get", "fetch", "out"], [three_of_hearts, ace_of_spades, two_of_diamonds, hat]))
    #hat.add_command(Command(pickupItem, ["pickup", "fetch"], [three_of_hearts, ace_of_spades, two_of_diamonds, hat]))
    
    ##ADDING TO SCENE

    lock_box.add_entity(three_of_hearts_horse)
    lock_box.add_entity(ace_of_spades_horse)
    lock_box.add_entity(two_of_diamonds_horse)

    hat.add_entity(three_of_hearts)
    hat.add_entity(ace_of_spades)
    hat.add_entity(two_of_diamonds)

    room.add_entity(lock_box)
    room.add_entity(queen)
    room.add_entity(hat)
    room.add_command(Command(deepExplore, ["explore"], [room]))
    return room


def wonderland_room_test(engine):
    player_one = engine.new_player(1, "evan")
    player_one.add_description("A boy stands here")
    commands = [
        #"* explore around", 
        #"* examine with queen",
        #"* examine hat",
        "* take cards out of hat",
        #"* i evan",
        #"* examine three of hearts"
        #"* examine hat",
        #"* examine lockbox",
        #"* place three of hearts on red hourse with three legs in the air "
        #"* examine lockbox",
        "* place three of hearts on horse with three legs",
        "* place ace of spades on black horse with one legs",
        "* place two of diamonds on red horse with two legs"
    ]
    for command in commands:
        engine.parse_command(player_one, command)

def test():
    rooms_containers = dict()
    #room = start_room(rooms_containers)
    room = wonderland_room(rooms_containers)
    rooms_containers["start"] = room
    engine = Engine(room, rooms_containers, wonderland_room_welcome)
    #start_room_test(engine)
    wonderland_room_test(engine)

