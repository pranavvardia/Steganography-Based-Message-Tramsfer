# Python program to implement client side of chat room.
import socket
import select
import sys
import mysql.connector
from mysql.connector import Error
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

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
	print(imported_pk)

	while True:
		message = input()
		cipher = PKCS1_OAEP.new(imported_pk)
		ciphertext = cipher.encrypt(message)
		server.send(ciphertext)
		print(ciphertext)
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
