'''
Created on Jan 4, 2013

@author: jslowik
'''
from collections import namedtuple
import time

INTERVAL = 5

def getDiskIO(diskAssignment):
    """
    Fetches total sectors read and total sectors written for
    provided diskAssignment e.g. "sda"
    """
    
    io = namedtuple('IO', 'read write')
    for line in open("/proc/diskstats"):
        columns = line.split(" ")
        if columns[11] == diskAssignment:
            ioData = io(int(columns[14]),int(columns[18]))
    
    if ioData:
        return ioData
    return 0

def deltaTime(diskAssignment, interval):
    """
    Returns the difference of the disk statistics returned by getDiskIO
    that occurred in the given time delta.
    """
    time1 = getDiskIO(diskAssignment)
    time.sleep(interval)
    time2 = getDiskIO(diskAssignment)
 
    return int(time2.read-time1.read), int(time2.write-time1.write)

def getDiskLoad(diskAssignment):
    """
    Returns the disk load in Bytes per second
    """
    read, write = deltaTime(diskAssignment, INTERVAL)
    
    bytesPerSecondRead = (read * 512) / INTERVAL
    bytesPerSecondWrite = (write * 512) / INTERVAL
   
    return bytesPerSecondRead+bytesPerSecondWrite

