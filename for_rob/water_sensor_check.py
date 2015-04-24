#!/usr/bin/python

# Monitor two soil sensors on MCP3008, ch 2 and 3 
# (pin 3 and 4)

#import spidev
import time
import os # not sure what this is needed for... KD
import json
import websocket
from datetime import datetime


import random


# Open SPI bus
#spi = spidev.SpiDev()
#spi.open(0,0)

# Function to read SPI data from MCP3008 chip
#def ReadChannel(channel):
#   adc = spi.xfer2([1,(8+channel)<<4,0])
#   data = ((adc[1]&3) << 8) + adc[2]
#   return data

count = 0
   
try:   
   print 'trying to create socket'
   ws = websocket.WebSocket()
   ws.connect("ws://54.67.7.215:8080")
   print 'ws created'
   # Main loop - read raw data and display

   while True:
#      soilOne = ReadChannel(2)
#      soilTwo = ReadChannel(3)
      soilOne = random.randint(0,100)
      
      print soilOne
      # Rob I need more info on what Rick is expecting ehre. I Tried to debug this, but its too late now...
      # INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:55 am', 115)
      payload = {
      'iTypeNumber': 20, 
      'iUnitNumber': 15, 
      'datDateTime': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
      'dValue': soilOne, # just sending 1 right now...
      }

      # Output
      #print "Soil1=",soilOne," : Soil2=",soilTwo

      ws.send(json.dumps(payload))
      out  = ws.recv()
      print out
      time.sleep(0.5)
except Exception as e:
   print e.message, e.args
finally:
   ws.close()