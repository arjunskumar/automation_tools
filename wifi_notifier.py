import urllib
import time
import os

while True:
	try:
	    url = "https://www.google.com"
	    urllib.urlopen(url)
	    status = "Connected"
	except:
	    status = "Not connected"
            os.system('spd-say "Wifi connection not available"')
	print status
        time.sleep(5)
