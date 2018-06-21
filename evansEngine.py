#!/usr/bin/python3

from re import match

Entity_id_count = 0


class Engine:
    # Map player ids to their entities
    def __init__(self, RootContainer, container_dict, welcomeMessage):
        self.players = dict()
        self.container_dict = container_dict
        self.start_container = RootContainer
        self.welcomeMessage = welcomeMessage

    def register_player_name(self, id, name):
        if id not in self.players:
            self.new_player(id, name.lower().replace(" ", ""))
            self.players[id].speak_to_player("please enter a description of your character:")
            return True
        
        
    def register_player_description(self, id, text):
        player = self.players[id]
        if player.description == "":
            player.add_description(player.name)
            player.add_examine_description(text)
            player.speak_to_player("Looking good: " + player.name + " good luck!")
        else:
            return False
        return True

    def run(self):
        "Execute game loop"
        while True:
            id, text = get_id(input())

            #try:
            if text == "None":
                continue


            if(self.register_player_name(id, text)):
                continue

            if(self.register_player_description(id, text)):
                continue

            self.parse_command(self.players[id], text)

    def new_player(self, id, name):
        "Create and register a new player"
        newPlayer = Player(id, name, self)
        for key, player in self.players.items():
            if player.name == name:
                newPlayer.speak_to_player("someone is using that name please enter a new name")
                return 
                
        self.players[id] = newPlayer
        self.welcomeMessage(newPlayer)
        self.start_container.add_entity(newPlayer)
        return newPlayer

    def parse_command(self, player, text):
        if (text[0] == '*'): 
            trigger_words = text.split()
            if (trigger_words[0] != '*'):
                player.speak_to_player("Please make sure you start commands with *, following with a space")
            else:
                trigger_words = list(map(lambda x: x.lower(), trigger_words))
                self.check_room_for_triggers(trigger_words[1:], player)
                
        else:
            self.broadcast_text(player, text)


    def broadcast_text(self, fromPlayer, text):
        for _id in self.players:
            if (_id != fromPlayer.id and fromPlayer.current_room.has_entity(self.players[_id])):
                self.players[_id].speak_to_player(fromPlayer.get_name()+": "+text)
    
    def broadcast_msg(self, fromPlayer, msg):
        for _id in self.players:
            if (_id != fromPlayer.id):
                self.players[_id].speak_to_player(msg)
    
    def check_room_for_triggers(self, trigger_words, player):
       
        list_of_entities = []

        self.find_entitites_with_triggers(trigger_words, player.current_room, list_of_entities)

        for entity in list_of_entities:
            entity.try_commands(trigger_words, player)

        print(list_of_entities)

    def find_entitites_with_triggers(self, trigger_words, entity, list_of_entities):    
        if (len(intersection(entity.get_trigger_words(), trigger_words)) != 0):
            list_of_entities.append(entity)

        children = entity.get_entities()
        for child in children:
            self.find_entitites_with_triggers(trigger_words, child, list_of_entities)

    def remove_player(self, player):
        player.current_room.remove(player)
        del self.players[player.id]

def get_id(command):
    "Extract player id from command"
    result = match("(^.+):\s*(.+)", command)
    if result == None:
        return "None", "None"
    return result.groups(0)[0], result.groups(0)[1]


class Entity:
    """Components in the video game, they are litterally everything
        that you can interact with
    """
    def __init__(self, trigger_words):
        global Entity_id_count
        self.id = Entity_id_count
        Entity_id_count += 1
        self.entities = []
        self.description = ""
        self.examine_description = ""
        self.commands = []
        self.add_command(Command(self.examine, examine_word_set, [self]))
        self.add_command(Command(self.explore, exploring_word_set, [self]))
        self.trigger_words = trigger_words
        
    def add_entity(self, entity):
        self.entities.append(entity)

    def examine(self, entities, player):
        player.speak_to_player("-------------------------------------------------------------------")
        player.speak_to_player(self.examine_description)
        player.speak_to_player("")
        

    def explore(self, entities, player):
        player.speak_to_player("-------------------------------------------------------------------")
        player.speak_to_player(self.get_description())
        player.speak_to_player("")

        for e in self.entities:
            player.speak_to_player(e.get_description())
            player.speak_to_player("")

    def get_entities(self):
        return self.entities

    def remove(self, entity):
        indexToRemove = 0
        for i in range(len(self.entities) - 1):
            if self.entities[i].id == entity.id:
                indexToRemove = i
        self.entities.pop(indexToRemove)

    def add_command(self, command):
        self.commands.append(command)

    def try_commands(self, trigger_words, player):
        for command in self.commands:
            command.try_command(trigger_words, player)

    def add_description(self, description):
        self.description = description

    def add_examine_description(self, description):
        self.examine_description = description
    
    def get_examine_description(self):
        return self.examine_description

    def add_trigger_words(self, words):
        self.trigger_words.add(words.toLower())

    def delete_trigger_words(self, words):
        self.trigger_words = self.trigger_words.difference(words.toLower())

    def get_trigger_words(self):
        return self.trigger_words

    def get_description(self):
        return self.description

    def has_entity(self, item):
        for entity in self.entities:
            if (entity.id == item.id):
                return True
        return False

    def __repr__(self):
        return self.description
    



class Command:
    """Each Entity has commands equiped to them, that perform
        a user defined command (function) based on 
        trigger words [door, lever], and the entities it interacts with [door, lever]
    """
    def __init__(self, command, trigger_words, entities):
        self.trigger_words = trigger_words
        self.command = command
        self.entities = entities

    def do(self, player):
        self.command(self.entities, player)
    
    def try_command(self, trigger_words, player):
        if(len(intersection(self.trigger_words, trigger_words)) !=0):
            self.do(player)

    def __repr__(self):
        return self.trigger_words


class Player(Entity):
    def __init__(self, id, name, engine):
        super().__init__([name])
        self.add_command(Command(self.kill, ["kill"], [self]))
        self.add_command(Command(self.display_items, ["items", "i", "inventory"], [self]))
        self.id = id
        self.name = name
        self.engine = engine
        self.current_room = engine.start_container
    
    #command for killing players
    def kill(self, entities, player):
        ##TODO DROP looots
        self.speak_to_player("YOU'RE DEAD SUCKER...enter a new name to reconnect")
        self.current_room.remove(self)
        self.engine.remove_player(self)
        self.current_room.get_entities().extend(self.entities)
        
    def display_items(self, entities, player):
        player.speak_to_player("Items: ")
        entities = player.get_entities()
        for e in entities:
            player.speak_to_player(e)
        player.speak_to_player("")


    def speak_to_player(self, text):
        "Write text for client with id"
        print("{}:{}".format(self.id, text))

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name

    def move(self, newRoom):
        self.current_room.remove(self)
        self.current_room = newRoom
        newRoom.add_entity(self)

#Utils https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))



exploring_word_set = ["look", "discover", "survey", "tour", "scout", "peer", "gander", "explore"]
examine_word_set = ["search", "probe", "scrutinize", "research", "examine", "analyze", "seek", "prospect", "inspect", "question", "sift"]
action_word_set = ["try", "attempt", "attack", "experiment", "endeavor", "tryout", "venture", "touch", "interact"]

