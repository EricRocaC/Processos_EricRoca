# Echo server program
import socket
import time
from threading import Thread

def rebre(conn):
    while True:
        data = conn.recv(1024)
        print "Message: ", data
        if data.lower() == "bye":
            conn.sendall(data)
            print "Closing server..."
            time.sleep(1)
            break

def enviar(conn):
    while True:
        data = raw_input("Send message: ")
        conn.sendall(data)
        if data.lower() == "bye":
            print "Closing server..."
            time.sleep(1)
            break

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
conn.sendall('Connected')

send = Thread(target = enviar, args=[conn,])
send.daemon = True
send.start()
recive = Thread(target = rebre, args=[conn,])
recive.start()

recive.join()
conn.close()
