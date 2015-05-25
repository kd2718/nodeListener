# Basic websocket program to 

import json
#import websocket
from websocket import create_connection


print 'trying to create websocket'
#ws = websocket.WebSocket() 
#ws.connect("ws://54.67.7.215:8080")
ws = create_connection("ws://54.67.7.215:8080")
print 'websocket created'
    
#loop 3 times
for i in range(3):

    #prepare javascript
    payload = {
    'iTypeNumber': 20, # place-holder 
    'iUnitNumber': 15, # place-holder 
    'datDateTime': '2015-04-28 12:33:44.703',
    'dValue': 999,
    }
    
    # Output
    ws.send(json.dumps(payload))
    print 'data sent'
    print

    
ws.close()