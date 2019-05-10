import sys
import random
import requests
from http.server import *

if len(sys.argv) != 2:
    print("Pass the port")
    exit(1)


class RequestHandler(BaseHTTPRequestHandler):
    def search_github(self, query):
        url = "https://github.com/search?q=" + query
        response = requests.get(url)
        css_classes = list(
            map(lambda s: s[7:], list(filter(lambda s: s.startswith("class="), response.text.split(" ")))))
        return str(css_classes)

    def random_string(self):
        return "".join(list(map(lambda i: "abcdefghij"[int(i)], str(random.randint(100000, 1000000)))))

    def do_GET(self):
        message = self.search_github(self.random_string())
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


class Server:
    def __init__(self, port):
        self.port = port

    def run(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.serve_forever()


server = Server(int(sys.argv[1]))
server.run()
