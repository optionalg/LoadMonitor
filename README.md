LoadMonitor
===========

## General ##

Simple python scripts to monitor server resources using Google spreadsheets and charts.

Uses google spreadsheet to archive data. Google spreadsheet provides timeline graphs for each resource tracked. 

Current implementation tracks:
<ul>
<li>CPU (over 5 seconds)</li>
<li>CPU temp</li>
<li>Memory utilization (free, used, total)</li>
<li>Disk I/O (bytes per second total for disk "sda1")</li>
<li>Network load (tx, rx for "eth0")</li>
</ul>

Project is specific to Raspberry Pi due to CPU temp monitoring.

## Usage ##
<ul>
<li>Make a copy of my google spreadsheet: https://docs.google.com/spreadsheet/ccc?key=0As-0hIWBcQmFdGZzSW1YNGdldjVybnJHYkJFeUFHRGc</li>
<li>In your copy of the spreadsheet, go to "Form -> Go to live form". When you get to the next page, copy the form key. The form key is the obscure text after "formkey=" up to the hash ("#") symbol.</li>
<li>Edit GoogleSheet.py and paste the key into the value FORMKEY</li>
<li>You may have to edit the ENTRIES dictionary in the event those values change; you can confirm this by going to the live form and viewing the source for each entry field.</li>
</ul>


## Limitations ##
<ul>
<li>Disk I/O only monitors the "sda1" drive. If that drive doesn't exist the script will report "0" every time it runs. This code also assumes each sector is 512 bytes.</li>
<li>CPU Temp can be configured for Celsius, Fahrenheit, and Kelvin (for fun). The script is using Fahrenheit by default because I'm a lazy American who can't be bothered memorizing Celsius conversion.</li>
<li>If this package of scripts are ever intended to run on a machine that is not a Raspberry Pi, the CPU Temp code should be ignored</li>
<li>The network utilization code only monitors the "eth0" network interface. If that interface does not exist or is not used, a "0" will be reported every time the script runs.</li>
<li>With the exception of CPU temp, all of the resources this script monitors looks at /proc/ kernel files.</li>
</ul>


## Author ##
You may contact me at slowikjw at gmail.com.

Enjoy~
