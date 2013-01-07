'''
Created on Jan 4, 2013

@author: jslowik
'''

import urllib2

def send(CPU,USEDMEM,FREEMEM,TOTALMEM,DISK,TEMP,RX,TX):
    
    FORMKEY='YOUR_FORM_KEY_HERE'
    ENTRIES={'CPU': 'entry.0.single',
             'USEDMEM': 'entry.1.single',
             'FREEMEM': 'entry.6.single',
             'TOTALMEM': 'entry.8.single',
             'DISK': 'entry.5.single',
             'TEMP': 'entry.9.single',
             'RX': 'entry.10.single',
             'TX': 'entry.12.single'}
    
    URL='https://spreadsheets.google.com/formResponse?formkey='+FORMKEY+'&'+ENTRIES['CPU']+'='+str(CPU)+'&'+ENTRIES['USEDMEM']+'='+str(USEDMEM)+'&'+ENTRIES['FREEMEM']+'='+str(FREEMEM)+'&'+ENTRIES['TOTALMEM']+'='+str(TOTALMEM)+'&'+ENTRIES['DISK']+'='+str(DISK)+'&'+ENTRIES['TEMP']+'='+str(TEMP)+'&'+ENTRIES['RX']+'='+str(RX)+'&'+ENTRIES['TX']+'='+str(TX)+'&submit=Submit'

    submit = urllib2.urlopen(URL)
    return submit