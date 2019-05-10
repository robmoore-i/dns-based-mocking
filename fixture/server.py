import sys
from http.server import *

if len(sys.argv) != 2:
    print("Pass the port")
    exit(1)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello from python3".encode('utf-8'))


class Server:
    def __init__(self, port):
        self.port = port

    def run(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.serve_forever()


server = Server(int(sys.argv[1]))
server.run()
