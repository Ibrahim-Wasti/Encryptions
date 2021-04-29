from Crypto.Cipher import AES
from Crypto import Random
from secrets import token_bytes
import hashlib
from base64 import b64encode, b64decode

key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    cipher_text, tag = cipher.encrypt_and_digest(msg.encode())
    return nonce, cipher_text, tag

def decrypt(nonce, cipher_text, tag):
    cipher = AES.new(key,AES.MODE_EAX,nonce=nonce)
    plain_text = cipher.decrypt(cipher_text)
    try:
        cipher.verify(tag)
        return plain_text.decode('ascii')
    except:
        return False
n, ct, t = encrypt(input('Enter a message:'))
pt = decrypt(n, ct, t)

# print(f'Cipher text: {ct}')
# print(f'Plain text: {pt}')




    