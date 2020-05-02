# -*- coding: utf-8 -*-

from GenerateKeys_EricRoca import *

#----------------Creació Claus------------------------

key = GenerateKeys()
print(key.exportKey())

#---------------------Exportació Claus-------------------
ExportKeys("privatekey", key)
ExportKeys("publickey", key.publickey())

#---------------------Importació Claus-------------------

keyPrv = ImportKeys("privatekey.pem")
print("Key Privada ->>" + str(keyPrv))
keyPub = ImportKeys("publickey.pem")
print("Key Publica ->>" + str(keyPub))

#----------------Encriptació 1------------------------

msgEncriptat = EncryptRSAKey("It's time to e e e e encrypt!", keyPublica)
print("Missatge encriptat ->> " +str(msgEncriptat))

#----------------Desencripació 1------------------------

msgDecp = DecryptRSAKey(msgEncriptat,keyPrivada)
print("Missatge desencriptat ->> " + str(msgDecp))

#-----------------Generar SHA 256-----------------------

KeySHA = GenSHA256Key()
print(KeySHA)

#-------------------Encriptació 2---------------------7

DaEncAES = EncryptMsgAES("It's time to e e e e encrypt (AES Version)!", KeySHA)
print("Data Encriptada AES ->>" + str(DaEncAES))

#-------------------Desencrpitació 2---------------------8
msgDesenc = DesencriptaMsgAES(DaEncAES , KeySHA)
print("El missatge desencriptat ->> " + msgDesenc)
