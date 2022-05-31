import base64
import hashlib

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad, pad


def decryptData():
    enc = "a7BOtp+JjLAFhIDfs6n0l8Gpu2uOkS7nhwfoBWpAaRNgVcakoMVMFzMpcDR/zxm1"
    print(enc)
    passKey = "12801417909200937970"
    passKey = hashlib.sha256(passKey.encode('utf-8')).digest()
    iv = bytes(passKey[0:16])
    cipher = AES.new(passKey, AES.MODE_CBC, iv)
    enc = base64.b64decode(enc)
    decValue = cipher.decrypt(enc[16:])

    return unpad(decValue, 16).decode("utf-8")

def encryptData():
    piiAttribute = "Dimpal.Kalita@netapp.com"
    passKey = "12801417909200937970"
    piiAttribute = piiAttribute.encode('utf-8')
    rawArray = bytearray(piiAttribute)
    passKey = hashlib.sha256(passKey.encode()).digest()
    iv = bytes(passKey[:16])
    cipher = AES.new(passKey, AES.MODE_CBC,iv)
    ct_bytes = cipher.encrypt(pad(rawArray, 16))
    ct = base64.b64encode(iv+ct_bytes)
    return ct.decode("utf-8")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # print(encryptData())
    print(decryptData())
