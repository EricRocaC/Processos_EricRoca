# -*- coding: utf-8 -*-

import hashlib
import json
import base64

from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode, b64encode
from Crypto.Util.Padding import unpad
from Crypto.Random import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random

#------------------------INICI DEL CODI---------------------------#

def GenerateKeys():
    key = RSA.generate(2048)
    return key

def ExportKeys(key, path):
    key2Export = key.exportKey('PEM')
    file2export = open(path+".pem", "wb")
    file2export.write(key2Export)
    file2export.close()

def ImportKeys(path):
    return RSA.import_key(open(path).read())

def EncryptRSAKey(data, key):
    cipher = PKCS1_OAEP.new(key)

    return cipher.encrypt(data.encode())

def DecryptRSAKey(encMsg, key):
    decipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(encMsg).decode('utf-8')

def GenSHA256Key():
    password = input("Please, write here your password ")
    key = hashlib.sha256(password.encode("utf-8")).digest()
    return key

def EncryptMsgAES(data, key):
    length = 16
    data = data + (length - len(data) % length) * chr(length - len(data) % length)
    vector = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, vector = vector)
    encMsg =  cipher.encrypt(data.encode())
    return base64.b64encode(vector + encMsg)

def DecrypMsgAES(encMsg, key):
    encMsg =  base64.b64decode(encMsg)
    vector = encMsg[:AES.block_size]
    extractedMsg = encMsg[AES.block_size:]
    decipher = AES.new(key, AES.MODE_CBC, vector)
    return cipher.decrypt(extractedMsg).decode("utf-8")
