#!/usr/bin/python

# Monitor two soil sensors on MCP3008, ch 2 and 3 
# (pin 3 and 4)

import spidev
import time
import os # not sure what this is needed for... KD
import json
import websocket
from datetime import datetime

# set up socket info
url = "ws://54.677.215:8080"

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
    ws = websocket.WebSocket()
    ws.connect(url)
    # Main loop - read raw data and display

    while True:
        soilOne = ReadChannel(2)
        soilTwo = ReadChannel(3)
        
        payload = {
        iReadingsKey: 1,# what...
        iTypeKey: 1, # are..
        iUnitKey: 1, # these?
        datDateTime: datetime.now(),
        dValue: soilOne, # just sending 1 rihgt now...
        }
   
        # Output
        print "Soil1=",soilOne," : Soil2=",soilTwo
   
        time.sleep(0.5)
except Exception as e:
    print e.message, e.args
finally:
    ws.close()