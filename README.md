<h2>About</h2>
This project is based around Python and the <a href="http://en.wikipedia.org/wiki/Raspberry_Pi">Raspberry Pi</a>, a credit-card sized computer with GPIO, USB, 10/100 Ethernet and more. TempLogger collects, stores, and displays temperature data from up to 8 different sensors. There is a physical LCD to display all of temperatures with a pushbutton to activate and deactivate all functions. Time and sensor data are stored in CSV format and collected at a configurable interval. An Apache webserver with PHP is hosted on the Raspberry Pi for display of the temperature data via <a href="http://dygraphs.com/">dygraph</a> and for start/stop functions.

<h2>Hardware Set-up</h2>
<ul>
	<li><a href="http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf">DS18B20</a> digital temperature sensors are used. Each sensor has a unique 64-bit address and multiple sensors can be used with a single input pin to the Pi, leaving all of the other GPIO pins for other tasks. Since they are digital no ADC is required (no ADC is present on the Pi)</li>
	<li>A USB (nano) wifi module is used for connection to a network</li>
	<li><a href="http://www.adafruit.com/products/499">A 20x4 RGB LCD</a> driven by a <a href="http://www.adafruit.com/datasheets/HD44780.pdf">HD44780</a> controller is used for display of the temperature data. Changes in background colour are used to signify a started or stopped state</li>
	<li>A generic pushbutton is used for starting and stopping the collection of data</li>
</ul>

<h2>Software Requirements</h2>
The following modules should be installed using apt-get after installing <a href="http://www.raspbian.org/">Raspbian</a> on the Raspberry Pi:
<ul>
	<li><a href="http://httpd.apache.org/">Apache</a> and <a href="http://php.net/">PHP</a> required for web display of the data</li>
	<li>w1-gpio and w1-therm kernel modules (should be included by default in Raspbian)</li>
</ul>
The <a href="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCDPlate">Adafruit_CharLCDPlate</a> library is included in the source and is used for low-level control of the LCD display.
<h2 id="Installation"><div class="anchor">Installation</div></h2>
<ol>
	<li>The script in the init.d directory should be placed in /etc/init.d/ and the command 'sudo update-rc.d tempLogger defaults' executed to make the program run on startup. The files in the www directory should be placed in the server's webroot. All other files should be placed in /home/pi/tempLogger/</li>
	<li>A symbolic link should be made from /home/pi/tempLogger/tempData.csv to the server's webroot directory</li>
</ol>
<h2>Notes</h2>
All of the parts should be available from <a href="http://www.adafruit.com">Adafruit.</a>