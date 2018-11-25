from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from steganography import modPix, encode_enc, encode, genData, decode


message = b'You can attack now!'
pub_key = RSA.importKey(open('public.pem').read())
cipher = PKCS1_OAEP.new(pub_key)
ciphertext = cipher.encrypt(message)
print(ciphertext)
encode('cat.png', ciphertext)
msg = decode('new.png')
print(msg)
# priv_key = RSA.importKey(open('private.pem').read())
# cipher1 = PKCS1_OAEP.new(priv_key)
# final = cipher1.decrypt(msg)
# print(final)
