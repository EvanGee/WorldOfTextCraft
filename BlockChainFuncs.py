import requests
import sys
def getPlayerStatsFromBlockChain(address):


        r = requests.post("http://localhost:3030/blockchain/call", json = {
                'contract': 'PlayerRegistry',
                'funcName': 'getPlayerByAddress',
                'id': 'PlayerRegOne',
                'args': [address],
                'gas': '0'
        })

        if len(r.text) != 42:
                sys.stderr.write(r.text)
                return ['7','7','7','7','7','7']

        r2 = requests.post("http://localhost:3030/blockchain/call", json = {
                'contract': 'Player',
                'funcName': 'getStats',
                'address': r.text,
                'args': [],
                'gas': '0'
        })

        text = r2.text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("'", "")
        text = text.replace("\"", "")
        text = text.split(',')
        return text


def test():
        getPlayerStatsFromBlockChain("0x83c0f0b82e2fda8f7695eac7ac3b714826f14c81")
