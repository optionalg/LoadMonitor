'''
Created on Jan 7, 2013

@author: jslowik
'''
import os

def getCPUtemperature(tempScale):
    ''' returns the temperature data of the cpu,
    this code was adapted from 
    "http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=22180"'''
    res = os.popen('vcgencmd measure_temp').readline()
    cTemp = float(res.replace("temp=","").replace("'C\n",""))
    if tempScale == 'C':
        return cTemp
    if tempScale == 'F':
        return cTemp * 9/5 + 32
    if tempScale == 'K':
        return cTemp + 273.15