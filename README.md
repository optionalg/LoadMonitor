LoadMonitor
===========

Simple python scripts to monitor server resources using Google spreadsheets and charts.

Uses google spreadsheet to archive data. Google spreadsheet provides timeline graphs for each resource tracked. 

Current implementation tracks:
<ul>
<li>CPU (over 5 seconds)</li>
<li>CPU temp</li>
<li>Memory utilization (free, used, total)</li>
<li>Disk I/O (bytes per second total for disk "sda")</li>
<li>Network load (tx, rx for "eth0")</li>
</ul>

Project is specific to Raspberry Pi due to CPU temp monitoring.

To use:
<ul>
<li>Make a copy of my google spreadsheet: https://docs.google.com/spreadsheet/ccc?key=0As-0hIWBcQmFdGZzSW1YNGdldjVybnJHYkJFeUFHRGc</li>
<li>Go to your Google Drive account, select the copied spreadsheet and go to 'Share settings'. In the share settings copy the key from the 'Link to share' field. The key is the obscure string of characters after "key="</li>
<li>Edit GoogleSheet.py and paste the key into the value FORMKEY</li>
<li>You may have to edit the ENTRIES dictionary in the event those values change; you can confirm this by going to the live form and viewing the source for each entry field.</li>
</ul>
