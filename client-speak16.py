# Echo client program
import socket
import time
from threading import Thread

def rebre(s):
    while True:
        data = s.recv(1024)
        print "Message: ", data
        if data.lower() == "bye":
            s.sendall(data)
            print "Closing client..."
            time.sleep(1)
            break

def enviar(s):
    while True:
        data = raw_input("Send message: ")
        s.sendall(data)
        if data.lower() == "bye":
            print "Closing client..."
            break

HOST = 'localhost'        # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

send = Thread(target = enviar, args=[s,])
send.daemon = True
send.start()
recive = Thread(target = rebre, args=[s,])
recive.start()

recive.join()
s.close()
