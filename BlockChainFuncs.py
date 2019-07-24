import requests
import sys
import json

url = "http://localhost:3030/blockchain/"
gaslimit = 300000


def getOwner(itemName):

        addr = getItemAddressBlockchain(itemName)
        r = requests.post(url + "call", json = {
                'contract': 'GameComponent',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getOwner",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getPlayerOwner(playerId):
    
        addr = getPlayerFromAddressBlockChain(playerId)
        r = requests.post(url + "call", json = {
                'contract': 'Player',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getOwner",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

#----------------------------------items----------------------------------

def deployItem(name, stats, itemRegistry):
        r = requests.post(url + "deploy", json = {
                'contract': 'Item',
                'id': name,
                'args': [stats],
                'gas': gaslimit
        })

        datastore = json.loads(r.text)
        itemAddr = datastore['payload']

        print("deployed: " + itemAddr)
        if itemAddr == "":
                return

        addedItem = addItemToRegistry(name, itemAddr, itemRegistry)
        return addedItem

def addItemToRegistry(name, itemAddr, itemRegistry):
        r2 = requests.post(url + "call", json = {
                "contract": "NameRegistry",
                "gas": gaslimit,
                "args": [name, itemAddr],
                "funcName": "addName",
        })
        print("added to registry: " + r2.text)
        datastore = json.loads(r.text)
        return datastore['payload']

def getItemAddressBlockchain(name):
        itemRegistry = getItemRegistry()
        r = requests.post(url + "call", json = {
                'contract': 'NameRegistry',
                'address': itemRegistry,
                'args': [name],
                'gas': '0',
                "funcName": "getAddress",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getItemStatsBlockchainByName(name):
        addr = getItemAddressBlockchain(name)

        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getStats"
        })

        datastore = json.loads(r.text)
        return datastore['payload']

def getItemStatsBlockchainByAddress(addr):
        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "getStats"
        })

        datastore = json.loads(r.text)
        return datastore['payload']

def checkIfItemIsInRegistryByAddress(address):
        itemReg = getItemRegistry()
        r = requests.post(url + "call", json = {
                'contract': 'NameRegistry',
                'address': itemReg,
                'args': [address],
                'gas': '0',
                "funcName": "getName"
        })
        datastore = json.loads(r.text)
        if datastore['payload'] == "0x0000000000000000000000000000000000000000":
                return False
        return True

#the account in the wallet will buy it, not metamask
def buy(itemName, value):
        addr = getItemAddressBlockchain(itemName)
        r = requests.post(url + "call", json = {
                'contract': 'Purchasable',
                'address': addr,
                'args': [],
                'gas': gaslimit,
                'value' : value,
                "funcName": "buy"
        })
        datastore = json.loads(r.text)
        return datastore['payload']


def getPrice(name):

        addr = getItemAddressBlockchain(name)
        r = requests.post(url + "call", json = {
                'contract': 'Purchasable',
                'address': addr,
                'args': [],
                'gas': gaslimit,
                "funcName": "getPrice",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

        
def setPrice(address, price):

        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': address,
                'args': [price],
                'gas': gaslimit,
                "funcName": "setPrice",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

#canTrade is a bool
def setIsPurchasable(itemAddr, canTrade):
        r = requests.post(url + "call", json = {
                'contract': 'Purchasable',
                'address': itemAddr,
                'args': [canTrade],
                'gas': gaslimit,
                "funcName": "setPurchasable",
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getIsPurchasable(name):
        r = requests.post(url + "call", json = {
                'contract': 'Item',
                'address': addr,
                'args': [],
                'gas': '0',
                "funcName": "isPurchasable",
        })
        datastore = json.loads(r.text)
        return datastore['payload']


#----------------------------------Players----------------------------------

def getPlayerFromAddressBlockChain(address):
 
        try: 
                playerReg = getPlayerRegistry()
                r = requests.post(url + "call", json = {
                        'contract': 'PlayerRegistry',
                        'funcName': 'getPlayerByAddress',
                        'address': playerReg,
                        'args': [address],
                        'gas': 0
                })

        except: 
                return "0x0000000000000000000000000000000000000000"


        datastore = json.loads(r.text)
        return datastore['payload']


def getAllPlayerItems(id):

        addr = getPlayerFromAddressBlockChain(id)

        items = getPlayerItemsFromBlockChain(addr)
        returnItems = {}

        for i in items:
                if checkIfItemIsInRegistryByAddress(i):
                        itemStats = getItemStatsBlockchainByAddress(i)
                        name = getItemName(i)
                        print(itemStats)
                        print(name)
                        returnItems[name] = itemStats



def getPlayerStatsFromBlockChain(address):

        addr = getPlayerFromAddressBlockChain(address)
   
        if addr == "0x0000000000000000000000000000000000000000":
                return ['7','7','7','7','7','7']

        try:
                r2 = requests.post("http://localhost:3030/blockchain/call", json = {
                        'contract': 'Player',
                        'funcName': 'getStats',
                        'address': addr,
                        'args': [],
                        'gas': '0'
                })
                
                datastore = json.loads(r2.text)    
                text = datastore['payload']

                if len(text) != 6:
                        return ['7','7','7','7','7','7']
                
        except:
                return ['7','7','7','7','7','7']

        return text

def getPlayerItemsFromBlockChain(address):
        addr = getPlayerFromAddressBlockChain(address)
        if addr == "0x0000000000000000000000000000000000000000":
                return []

        r = requests.post("http://localhost:3030/blockchain/call", json = {
                'contract': 'Player',
                'funcName': 'getItems',
                'address': addr,
                'args': [],
                'gas': '0'
        })

        datastore = json.loads(r.text)
        items = datastore['payload']
        print("player items on blockchain: " + str(items))
        return items

def getDefaultAddress():
        r = requests.get("http://localhost:3030/accounts/defaultAddress")
        datastore = json.loads(r.text)
        return datastore['payload']

#------------------------------Registr--------------------------------------
def deployGameRegistry():
        r = requests.post(url + "deploy", json = {
                'contract': 'Game',
                'id': 'Game',
                'args': [],
                'gas': gaslimit
        })
        datastore = json.loads(r.text)
        return datastore['payload']
        
def getItemRegistry():
        r = requests.post(url + "call", json = {
                'contract': 'Game',
                'id': 'Game',
                'args': [],
                'funcName': "getItemRegistry",
                'gas': 0
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getPlayerRegistry():
        r = requests.post(url + "call", json = {
                'contract': 'Game',
                'id': 'Game',
                'args': [],
                'gas': 0,
                'funcName': "getPlayerRegistry"
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getItemName(addr):
        itemReg = getItemRegistry()
        r = requests.post(url + "call", json = {
                'contract': 'NameRegistry',
                'address': itemReg,
                'args': [addr],
                'funcName': "getName",
                'gas': 0
        })
        datastore = json.loads(r.text)
        return datastore['payload']

def getitemAddress(name):
        itemReg = getItemRegistry()
        r = requests.post(url + "call", json = {
                'contract': 'NameRegistry',
                'address': itemReg,
                'args': [names],
                'funcName': "getAddress",
                'gas': 0
        })
        datastore = json.loads(r.text)
        return datastore['payload']
#------------------------------Integration--------------------------------------

def build_item(name, stats, price, isPurchasable):
        itemRegistry = getItemRegistry()
        itemAddr = deployItem(name, stats, itemRegistry)
        setPrice(itemAddr, price)
        setIsPurchasable(itemAddr, isPurchasable)


def deployAllItems():
        id = "0xcca4d2b2a1a38e8030c33861b97108680cd28cf0"
        #build_item("luckyDragonGoldenDagger", [7,7,7,7,7,7,7,7], 50000, True)

def unitTests():
                
        playerAddr = getDefaultAddress()
        print("defaultAddr: " + playerAddr)
        stats = getPlayerStatsFromBlockChain(playerAddr)
        print("stats: " + str(stats))
        items = getPlayerItemsFromBlockChain(playerAddr)
        for i in items:
                if checkIfItemIsInRegistryByAddress(i):
                        itemStats = getItemStatsBlockchainByAddress(i)
                        name = getItemName(i)
                        print(itemStats)
                        print(name)

#unitTests()