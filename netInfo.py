# displays IP addresses on the LCD

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import commands
import subprocess 
import os

# Initialize the LCD plate.
lcd = Adafruit_CharLCDPlate()

# change colour
lcd.backlight(lcd.VIOLET)

# output ETH and wlan IPs
lcd.clear()
ipaddr = str(commands.getstatusoutput('ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1'))
ipaddr2 = str(commands.getstatusoutput('ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1'))
lcd.message('ETH %s\n' % ( ipaddr2 ) )
lcd.message('WLAN %s' % ( ipaddr ) )
