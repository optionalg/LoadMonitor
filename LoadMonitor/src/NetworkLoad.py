'''
Created on Jan 7, 2013

@author: jslowik
'''
from collections import namedtuple
import time

INTERVAL = 5

def getNetworkTraffic(interface):
    '''
    returns the receive and transmit network traffic in a namedtuple
    '''
    traffic = namedtuple('network', 'rx tx')
    for line in open("/proc/net/dev"):
        columns = line.split()
        if columns[0] == interface:
            trafficData = traffic(int(columns[1]),int(columns[9]))
    
    return trafficData

def deltaTime(interface, interval):
    """
    Returns the difference of the network statistics returned by getNetworkTraffic
    that occurred in the given time delta.
    """
    time1 = getNetworkTraffic(interface)
    time.sleep(interval)
    time2 = getNetworkTraffic(interface)
 
    return int(time2.rx-time1.rx), int(time2.tx-time1.tx)


def getNetworkLoad(interface):
    """
    Returns the network load in Bytes
    """
    rx, tx = deltaTime(interface, INTERVAL)
    
    return rx, tx

getNetworkLoad("eth0:")
