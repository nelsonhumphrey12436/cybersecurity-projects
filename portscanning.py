import sys
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments")
	print("syntax: python3 scanner.py <ip>")
	
	
#template	
print("_" * 50)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("_" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket,SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indiator
		if result ==0:
			print("port {} is open",format(port))
		s.close()

except keyboardInterrupt:
	print("/nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("	Host name could not be resolved.")
	sys.exit()	
	
except socket.error:
	print("could not connect to server.")
	sys.exit()			
			