import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        print(raw)
        iv = Random.new().read(AES.block_size)
        print(base64.b64encode(iv))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        enc=cipher.encrypt(raw.encode())
        print(enc)
        return base64.b64encode(iv + enc)

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        print(enc)
        iv = enc[0:AES.block_size]
        print(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


obj=AESCipher("7gJkasQ89|asdTs^yb#4!2#&fJER2dpA")
val=obj.encrypt("June@2020jhvhvg")
print(val)
val=obj.decrypt(val)
print(val)