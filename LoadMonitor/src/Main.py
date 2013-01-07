'''
Created on Jan 4, 2013

@author: jslowik
'''
import GoogleSheet
import CPULoad
import DiskLoad
import MemoryLoad
import CPUTemp
import NetworkLoad
    
CPULOAD = CPULoad.getCpuLoad()*100.0
MEMTOTAL, MEMFREE = MemoryLoad.getMemory()
MEMUSED = MEMTOTAL-MEMFREE
DISKLOAD = DiskLoad.getDiskLoad("sda1")
TEMP = CPUTemp.getCPUtemperature('F')
RX,TX = NetworkLoad.getNetworkLoad("eth0:")

result = GoogleSheet.send(CPULOAD,MEMUSED,MEMFREE,MEMTOTAL,DISKLOAD,TEMP,RX,TX)
