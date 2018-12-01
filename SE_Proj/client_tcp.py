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
	IP_address = str(sys.argv[1])
	Port = int(sys.argv[2])
	public_key = ''.join((get_public_key(IP_address)))
	imported_pk = RSA.importKey(public_key)

	while True:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if len(sys.argv) != 3:
			print ("Correct usage: script, IP address, port number")
			exit()
		server.connect((IP_address, Port))

		message = input()
		message = message.encode('ascii')
		cipher = PKCS1_OAEP.new(imported_pk)
		ciphertext = cipher.encrypt(message)
		# print(ciphertext)
		text = ciphertext.decode('latin-1')

		encode("cat.png",text)

		fname = 'new.png'
		with open(fname, 'rb') as f:
			str_img = f.read()
		f.close()
		server.sendall(str_img)
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
