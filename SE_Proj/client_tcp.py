# Python program to implement client side of chat room.
import socket
import select
import sys
from PIL import Image
import mysql.connector
from mysql.connector import Error
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from steganography import modPix, encode_enc, encode, genData, decode
import base64
import codecs
import png

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if len(sys.argv) != 3:
		print ("Correct usage: script, IP address, port number")
		exit()
	IP_address = str(sys.argv[1])
	Port = int(sys.argv[2])
	server.connect((IP_address, Port))
	public_key = ''.join((get_public_key(IP_address)))
	# print (public_key)
	imported_pk = RSA.importKey(public_key)
	# print(imported_pk)

	while True:
		message = input()
		message = message.encode('ascii')
		cipher = PKCS1_OAEP.new(imported_pk)
		ciphertext = cipher.encrypt(message)
		text = ciphertext.decode('latin-1')
		# print(type(text))

		# text = ciphertext.decode("ascii")
		encode("cat.png",text)

		ms = decode('new.png')
		msg = bytes(ms,'latin-1')
		# new_msg = "{:<256}".format(msg)
		priv_key = RSA.importKey(open('private.pem').read())
		cipher1 = PKCS1_OAEP.new(priv_key)
		final = cipher1.decrypt(msg)
		print(final)
		fname = 'new.png'
		# print(type(fname))
		with open(fname, 'rb') as f:
		# r = png.Reader(file=fname)
			l = f.read()
			# while (l)
		print(l)
		server.sendall(l)
				# print('Sent', repr(l))
				# l = f.read(1024)
		f.close()
		sys.stdout.flush()
		server.close()

def get_public_key(ip):
	try:
		connection = mysql.connector.connect(host='172.16.134.148', database='python_db', user='root', password='se_proj')
		if connection.is_connected():
			cursor = connection.cursor()
			sql = "select public_key from User where ip = ip"
			cursor.execute(sql)
			result = cursor.fetchall()
			return result[0]
	except Error as e:
		print("Error connecting to MySQL", e)

if __name__ == '__main__':
	main()
