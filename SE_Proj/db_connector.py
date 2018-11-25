import mysql.connector
from mysql.connector import Error
import subprocess
from Crypto.PublicKey import RSA
import base64

# try:
#     connection = mysql.connector.connect(host='172.16.134.148',
#                              database='python_db',
#                              user='root',
#                              password='se_proj')
#     if connection.is_connected():
#        db_Info = connection.get_server_info()
#        print("Connected to MySQL database... MySQL Server version on ",db_Info)
#        cursor = connection.cursor()
#        cursor.execute("select database();")
#        record = cursor.fetchone()
#        print ("Your connected to - ", record)
# except Error as e :
#     print ("Error while connecting to MySQL", e)
# finally:
#     #closing database connection.
#     if(connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

def db_insert_info(ip,key):
    try:
        connection = mysql.connector.connect(host='172.16.134.148',
                                 database='python_db',
                                 user='root',
                                 password='se_proj')
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           cursor = connection.cursor()
           sql = "insert into User (ip, public_key) values (%s,%s)"
           val = (ip,key)
           cursor.execute(sql,val)
           connection.commit()
           cursor.execute("select * from User")
           myresult = cursor.fetchall()
           for x in myresult:
               print(x)
    except Error as e :
        print ("Error while connecting to MySQL", e)

def get_ip():
    output = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True)
    return output


def main():
    ip = get_ip()
    new_ip = ip[:-1]
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    public_key = key.publickey().export_key()
    file_out.write(private_key)
    file_out_pub = open("public.pem", "wb")
    file_out_pub.write(public_key)
    print(key.publickey())
    db_insert_info(new_ip,public_key)


if __name__ == '__main__':
    main()
