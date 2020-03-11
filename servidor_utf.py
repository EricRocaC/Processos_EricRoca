from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import time
import smtplib
from socket import gaierror

hostName = "localhost"
serverPort = 8081
path = "/servidor"

class Servidor(BaseHTTPRequestHandler):
    #Obtindre la IP del clinet
    def handle_one_request(self):
        print("The client", self.client_address[0], "is connected")
        return BaseHTTPRequestHandler.handle_one_request(self)

    def do_GET(self):
        if self.path == "/servidor":
            #Mostrar la imatge al navegador
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")
            self.end_headers()
            self.wfile.write(load('loremipsum.jpeg'))
            #Enviar correu al carregar
            fromaddr = 'erinrc98@gmail.com'
            toaddrs  = 'erinrc98@gmail.com'
            msg = "\r\n".join([
            "From: erinrc98@gmail.com",
            "To: erinrc98@gmail.com",
            "Subject: Just a message",
            "",
            str(self.client_address)
            ])
            username = 'erinrc98@gmail.com'
            password = '3223Eric@'
            smtp_server = smtplib.SMTP('smtp.gmail.com:587')
            smtp_server.starttls()
            smtp_server.login(username,password)
            smtp_server.sendmail(fromaddr, toaddrs, msg)
            smtp_server.quit()
        else:
            self.send_error(404, "Not found")

def load(file):
    with open(file, 'rb') as file:
        return file.read()

print("Serving local directory")
httpd = socketserver.TCPServer(("", 8080), Servidor)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Servidor)
    print("Server started http://%s:%s%s" % (hostName, serverPort, path))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("Closing server...")
        pass

    webServer.server_close()
    print("Server off")
