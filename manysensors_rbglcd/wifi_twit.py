# Tweet the temperature, light, and sound levels with our Raspberry Pi
# http://dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/sensor-twitter-feed/

# GrovePi + Sound Sensor + Light Sensor + Temperature Sensor + LED
# http://www.seeedstudio.com/wiki/Grove_-_Sound_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit

'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
'''

import time
import grovepi
from grove_rgb_lcd import *
import math

# Connections
sound_sensor = 2        # port A0
light_sensor = 1        # port A1
temperature_sensor = 5  # port D4



last_sound = 0
screen = False


while True:
    # Error handling in case of problems communicating with the GrovePi
    try:
        # Get value from temperature sensor
        [temp,humidity] = grovepi.dht(temperature_sensor,0)


        # Get value from light sensor
        light_intensity = grovepi.analogRead(light_sensor)
        if light_intensity/10>10:
            screen = True
        else:
            setText("")
            textCommand(0x00)
            screen = False

        # Get sound level
        sound_level = grovepi.analogRead(sound_sensor)
        if sound_level > 0:
            last_sound = sound_level

        # Post a tweet
        out_msg=("T: %.0dC H: %.1f%% \nL: %d S: %d" %(temp,humidity,light_intensity/10,last_sound))
        R=int(light_intensity/10.*255)
        G=int(last_sound/500.*255)
        B=int(humidity/100.*255)
        if screen:
            setRGB(R,G,B)
            setText(out_msg)
        print out_msg
        time.sleep(1)
    except IOError:
        print "Error"
