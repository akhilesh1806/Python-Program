# Author: AKHILESH

# This script helps to find the devices (mobiles and computers) connected to my wifi

# This script needs python-nmap as a pre-requisite. To install: sudo pip3 install python-nmap

import subprocess 

for ping in range(1,10): 
	address = "127.0.0." + str(ping) 
	res = subprocess.call(['ping', '-c', '3', address]) 
	if res == 0: 
		print( "ping to", address, "OK") 
	elif res == 2: 
		print("no response from", address) 
	else: 
		print("ping to", address, "failed!") 

