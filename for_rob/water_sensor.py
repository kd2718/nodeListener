#!/usr/bin/python

# Monitor two soil sensors on MCP3008, ch 2 and 3 
# (pin 3 and 4)

import spidev
import time
import os # not sure what this is needed for... KD
import json
import websocket
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
      
      print soilOne
      # Rob I need more info on what Rick is expecting ehre. I Tried to debug this, but its too late now...
      payload = {
      'iReadingsKey': 1,# what
      'iTypeKey': 1, # are..
      'iUnitKey': 1, # these?
      'datDateTime': datetime.now().isoformat(),
      'dValue': soilOne, # just sending 1 rihgt now...
      }

      # Output
      print "Soil1=",soilOne," : Soil2=",soilTwo
      def date_handler(obj):
          return obj.isoformat() if hasattr(obj, 'isoformat') else obj

      ws.send(json.dumps(payload, default=date_handler))
      out  = ws.recv()
      print out
      time.sleep(0.5)
except Exception as e:
   print e.message, e.args
finally:
   ws.close()