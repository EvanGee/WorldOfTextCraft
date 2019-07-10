import requests
import sys

url = "http://localhost:3030/blockchain/"


def getOwner(itemName):

        addr = getItemAddressBlockchain(itemName)
        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getOwner",
        })
        return r.text   

#----------------------------------items----------------------------------

def deployItem(name, stats):
        r = requests.post(url + "deploy", json = {
                'contract': 'Item',
                'id': name,
                'args': [stats],
                'gas': '500000000'
        })


        print("deployed: " + r.text)
        if r.text == "":
                return

        r2 = requests.post(url + "call", json = {
                "contract": "NameRegistry",
                "gas": "5000000",
                "args": [name, r.text],
                "funcName": "addName",
                "id" : "NameRegistry"
        })
        print("added to registry: " + r2.text)
        return r2.text

def getItemAddressBlockchain(name):

        r = requests.post(url + "call", json = {
                'contract': 'NameRegistry',
                'id': "NameRegistry",
                'args': [name],
                'gas': '0',
                "funcName": "getAddress",
        })
        return r.text

def getItemStatsBlockchain(name):
        addr = getItemAddressBlockchain(name)

        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getStats"
        })

        return r.text

#the account in the wallet will buy it, not metamask
def buy(itemName, value):
        addr = getItemAddressBlockchain(itemName)
        r = requests.post(url + "call", json = {
                'contract': 'purchasable',
                'address': addr,
                'args': [],
                'gas': '50000',
                'value' : value,
                "funcName": "buy"
        })
        return r.text


def getPrice(name):

        addr = getItemAddressBlockchain(name)
        r = requests.post(url + "call", json = {
                'contract': 'purchasable',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getPrice",
        })
        return r.text

        
def setPrice(name, price):

        addr = getItemAddressBlockchain(name)
        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [price],
                'gas': '50000',
                "funcName": "setPrice",
        })
        return r.text

#canTrade is a bool
def setTradeAble(name, canTrade):
        addr = getItemAddressBlockchain(name)
        r = requests.post(url + "call", json = {
                'contract': 'Purchasable',
                'address': addr,
                'args': [canTrade],
                'gas': '50000',
                "funcName": "setTradeAble",
        })
        return r.text

def getisTradeAble(name):
        addr = getItemAddressBlockchain(name)
        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "isTradable",
        })
        return r.text



#----------------------------------Players----------------------------------

def getPlayerFromAddressBlockChain(address):
 
        try: 
                r = requests.post("http://localhost:3030/blockchain/getContractAddress", json = {
                        'contract': 'PlayerRegistry',
                        'id': 'PlayerRegOne',
                        'args': [],
                        'gas': '5000000'
                })       

                r = requests.post(url + "call", json = {
                        'contract': 'PlayerRegistry',
                        'funcName': 'getPlayerByAddress',
                        'address': r.text,
                        'args': [address],
                        'gas': '0'
                })

        except: 
                return "0x0000000000000000000000000000000000000000"

        return r.text


def getPlayerItems(id):

        addr = getPlayerFromAddressBlockChain(id)
        try:
                r = requests.post(url + "call", json = {
                        'contract': 'Player',
                        'address': addr,
                        'args': [],
                        'gas': '0',
                        "funcName": "getItems",
                })
        except: 
                return []

        return r.text


def getPlayerStatsFromBlockChain(address):

        addr = getPlayerFromAddressBlockChain(address)
        if addr == "0x0000000000000000000000000000000000000000":
                return ['7','7','7','7','7','7','7','7']

        r2 = requests.post("http://localhost:3030/blockchain/call", json = {
                'contract': 'Player',
                'funcName': 'getStats',
                'address': addr,
                'args': [],
                'gas': '0'
        })
        text = r2.text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("'", "")
        text = text.replace("\"", "")
        text = text.split(',')

        return text


#------------------------------Registr--------------------------------------
def deployGameRegistry():
        try: 
                r = requests.post("http://localhost:3030/blockchain/getContractAddress", json = {
                        'contract': 'PlayerRegistry',
                        'id': 'PlayerRegOne',
                        'args': [],
                        'gas': '5000000'
                })       
        
        except:
                return
        

        if r.text != "":
                return
        
        r = requests.post("http://localhost:3030/blockchain/deploy", json = {
                'contract': 'PlayerRegistry',
                'id': 'PlayerRegOne',
                'args': [],
                'gas': '5000000'
        })

        r = requests.post("http://localhost:3030/blockchain/call", json = {
                "contract": "PlayerRegistry",
                "gas": "5000000",
                "address": res.data,
                "args": [[10,10,10,10,10,11]],
                "funcName": "newPlayer",
                "id" : "PlayerRegOne"
        })
#------------------------------Integration--------------------------------------

def build_item(name, stats, price, isTradable):
        print(deployItem(name, stats))
        print(setPrice(name, price))
        print(setTradeAble(name, isTradable))


def deployAllItems():
        id = "0xcca4d2b2a1a38e8030c33861b97108680cd28cf0"
        #print(getItemAddressBlockchain("luckyDragonDagger"))
        #print(getItemStatsBlockchain("luckyDragonDagger"))
        #build_item("luckyDragonGoldenDagger", [7,7,7,7,7,7,7,7], 50000, True)
