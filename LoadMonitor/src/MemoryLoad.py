'''
Created on Jan 4, 2013

@author: jslowik
'''
def getMemory():
    meminfo = open("/proc/meminfo")
    MemTotal = meminfo.readline()
    MemFree = meminfo.readline()
    MemTotalColumns = MemTotal.replace("    ","").split(" ")
    MemFreeColumns = MemFree.replace("    ","").split(" ")
    return int(MemTotalColumns[1]), int(MemFreeColumns[3])


