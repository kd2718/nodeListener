#CSC687 Data Trip Project

import RPi.GPIO as GPIO
import spidev
import time
import json
import websocket
import random
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)

#Set Threshold for irrigation system
threshold = 100

#Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

#Function to read SPI data from the ADC chip
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Function to convert data to voltage level
def ConvertVolts(data,places):
    volts = ((data * 3.3) / float(1023))
    volts = round(volts,places)
    return volts

#Function to calculate moisture content from data
def ConvertMoisture(data, places):
    moisture = ((data * 330) / float(1023))
    moisture = round(moisture,places)
    return moisture 
    
#Define sensor channel
moisture_channel = 0

#Define delay between samples
delay = 1

try:   
    print 'trying to create websocket'
    ws = websocket.WebSocket()
    ws.connect("ws://54.67.7.215:8080")
    print 'websocket created'
    
    # Main loop - read raw data and display
    while True:

        #Read moisture sensor data
        moisture_level = ReadChannel(moisture_channel)
        moisture_volts = ConvertVolts(moisture_level,2)

        #Print results
        print"----------------------------------"
        print("Moisture: {}".format(moisture_level, moisture_volts))

        payload = {
        'iTypeKey': 12, 
        'iUnitKey': 13, 
        'datDateTime': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]),
        'dValue': moisture_level,
        }

        # Output
        ws.send(json.dumps(payload))
        print 'data sent'
        
        #Delay loop repetition
        time.sleep(delay)

        #Illuminate LED if threshold is not met
        if moisture_level < threshold:
            GPIO.output(11, True)
        else:
            GPIO.output(11, False)
        
except Exception as e:
    print e.message, e.args
    print"!!!!!!!!!!!!!!!!!!!!!!!!!"
    raise e
    
finally:
    ws.close()
    
