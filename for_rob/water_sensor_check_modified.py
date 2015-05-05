#!/usr/bin/python

import time
import json
import websocket
from datetime import datetime


import random


count = 0  
try:   
   print 'trying to create socket'
   ws = websocket.WebSocket()
   ws.connect("ws://*******:8080") # edited out my address name.
   print 'ws created'


   while True:
      soilOne = random.randint(0,100)
      
      print soilOne
      payload = {
      'iTypeNumber': 20, 
      'iUnitNumber': 15, 
      'datDateTime': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]),
      'dValue': soilOne, # just sending 1 right now...
      }

      # Output
      print "sending data"
      ws.send(json.dumps(payload))
      print "data has been sent \n"
      # check ws for flush...
      out = ws.recv()
      print 'out received'
      print out
      print"sleeping... \n\n"
      time.sleep(1)
except Exception as e:
   print e.message, e.args
finally:
   ws.close()