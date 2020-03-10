from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080
path = "/servidor"

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/servidor":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head>", "utf-8"))
            self.wfile.write(bytes("<meta charset='UTF-8'>", "utf-8"))
            self.wfile.write(bytes("<title>Practica webserver</title>", "utf-8"))
            self.wfile.write(bytes("</head><body>", "utf-8"))
            self.wfile.write(bytes("<h1>Això és una pàgina</h1>", "utf-8"))
            self.wfile.write(bytes("<p>Mooooolt bàsica!!!</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_error(404, "Not found")

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
