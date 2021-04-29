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

print(f'Cipher text: {ct}')
print(f'Plain text: {pt}')




# class AESCipher(object):
#     def __init__(self, key):
#         self.block_size = AES.block_size
#         self.key = hashlib.sha256(key.encode()).digest()

#     def encrypt(self, plain_text):
#         plain_text = self.__pad(plain_text)
#         iv = Random.new().read(self.block_size)
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         encrypted_text = cipher.encrypt(plain_text.encode())
#         return b64encode(iv + encrypted_text).decode("utf-8")

#     def decrypt(self, encrypted_text):
#         encrypted_text = b64decode(encrypted_text)
#         iv = encrypted_text[:self.block_size]
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
#         return self.__unpad(plain_text)

#     def __pad(self, plain_text):
#         number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
#         ascii_string = chr(number_of_bytes_to_pad)
#         padding_str = number_of_bytes_to_pad * ascii_string
#         padded_plain_text = plain_text + padding_str
#         return padded_plain_text

#     @staticmethod
#     def __unpad(plain_text):
#         last_character = plain_text[len(plain_text) - 1:]
#         bytes_to_remove = ord(last_character)
#         return plain_text[:-bytes_to_remove]


    