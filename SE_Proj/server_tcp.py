# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
from PIL import Image
from steganography import decode
import base64
import codecs


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(5)

while True:
	conn, addr = server.accept()
	print('Got connection from', addr)
	data = conn.recv(1024)
	with open('received_file.png', 'wb') as f:
		print('file opened')
		while True:
			data = conn.recv(1024)
			print(data)
			f.write(data)
			if not data:
				break

	f.close()
	print('Successfully get the file')
	conn.close()
	print('connection closed')
	# msg = decode('received_file.png')
	# print(msg)

	# prints the address of the user that just connected
	# creates and individual thread for every user
	# that connects
	# start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
