#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, sys
from flowmeter import *
from request import *

FLOW_SENSOR = 22


fm = FlowMeter('metric', 'water')
myRequest = MyRequest()


GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if fm.enabled == True:
    fm.update(currentTime)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse, bouncetime=20)

myRequest.post("","Water Monitor Boot up")

while True:
    try:
  	currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
        time.sleep(1)
	
 	if (fm.thisPour > 0.23 and currentTime - fm.lastClick > 10000): # 10 seconds of inactivity causes a tweet
	    tweet = time.strftime("%Y-%m-%d %H:%M") + " " + fm.getFormattedThisPour() + " of " + fm.getBeverage()
	    myRequest.post(fm.getThisPour(), fm.getFormattedThisPour())
	    lastTweet = int(time.time() * FlowMeter.MS_IN_A_SECOND)
	    fm.thisPour = 0.0
	    print tweet

    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()

