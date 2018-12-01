# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *
from PIL import Image
from steganography import decode
import base64
import codecs
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

IP_address = str(sys.argv[1])

Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(5)

while True:
	conn, addr = server.accept()
	data = conn.recv(1024)
	with open('received_file.png', 'wb') as f:
		f.write(data)
		while True:
			data = conn.recv(1024)
			f.write(data)
			if not data:
				break
	f.close()
	ms = decode('received_file.png')
	msg = bytes(ms,'latin-1')
	# print(msg)
	priv_key = RSA.importKey(open('private.pem').read())
	cipher1 = PKCS1_OAEP.new(priv_key)
	final = cipher1.decrypt(msg)
	final1 = final.decode('utf-8')
	# f_str = final1 + 'received from'
	# print(f_str)
	# print(cipher1)
	with open('output.txt', 'a') as f:
		f.write(final1 + "\n")

conn.close()
server.close()
