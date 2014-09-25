# listens for pushbutton presses to control the logging and updating of the LCD

import os 
import time 
import datetime 
import array 
import subprocess 
import commands 
import RPi.GPIO as GPIO 

# on first display IP addresses and start logging
os.system('sudo python /home/pi/tempLogger/netInfo.py 2>&1 &')
os.system('sudo python /home/pi/tempLogger/tempLog.py')

# setup pin 22 for pushbuttton input
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# set states so pushbutton works intuitively
curState = GPIO.input(22)
prevState = GPIO.input(22)

while True:
	curState = GPIO.input(22)
	print curState
	if curState == 1 and prevState == 0:
		s = str(commands.getstatusoutput('ps aux | grep tempLog.py'))
		if s.find('tempLog.py') != -1:
			ss = str(commands.getstatusoutput('`ps auxwww | grep tempLog.py | head -1 | awk '{print $2}'`'))
			os.system('kill -9 ' + ss)
			print "stopping"
    else:
	  os.system('sudo python /home/pi/tempLogger/tempLog.py&')
	  print "starting"
	prevState = curState
	time.sleep(0.1)
