#!/usr/bin/python

# Monitor two soil sensors on MCP3008, ch 2 and 3 
# (pin 3 and 4)

import spidev
import time
import os # not sure what this is needed for... KD
import json
import websocket # https://pypi.python.org/pypi/websocket-client
from datetime import datetime

import random


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
   adc = spi.xfer2([1,(8+channel)<<4,0])
   data = ((adc[1]&3) << 8) + adc[2]
   return data

count = 0
   
try:   
   print 'trying to create socket'
   ws = websocket.WebSocket()
   ws.connect("ws://54.67.7.215:8080")
   print 'ws created'
   # Main loop - read raw data and display

   while True:
      soilOne = ReadChannel(2)
      soilTwo = ReadChannel(3)
      #soilOne = random.randint(0,100)
      
      print soilOne # if this is python 3, change all the print to print()
      
      payload = {
      'iTypeKey': 20, # place-holder while we get user authentication figured out
      'iUnitKey': 15, # place-holder while we get user authentication figured out
      'datDateTime': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]),
      'dValue': soilOne, # just sending 1 right now...
      }

      # Output
      ws.send(json.dumps(payload, default=date_handler))
      
      time.sleep(0.5)
except Exception as e:
   print e.message, e.args
finally:
   ws.close()