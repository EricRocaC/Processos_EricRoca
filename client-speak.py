# Echo client program
import socket

HOST = 'localhost'        # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print "Send a message: "
    Message = raw_input()
    s.sendto(Message, (HOST, PORT))
    if Message == "bye":
        s.close()
        break
