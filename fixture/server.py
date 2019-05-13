import sys
import random
import requests
from http.server import *

if len(sys.argv) != 2:
    print("Pass the port")
    exit(1)


class RequestHandler(BaseHTTPRequestHandler):
    def search_github(self, query):
        url = "http://github.com/search?q=" + query
        response = requests.get(url)
        css_classes = list(
            map(lambda s: s[6:], list(filter(lambda s: s.startswith("class="), response.text.split(" ")))))
        return_value = str(css_classes[random.randint(0, len(css_classes) - 1)])
        print("github: " + return_value)
        return return_value

    def random_string(self):
        return "".join(list(map(lambda i: "abcdefghij"[int(i)], str(random.randint(100000, 1000000)))))

    def search_google(self, query):
        url = "http://www.google.com/search?client=safari&rls=en&q=" + query + "&ie=UTF-8&oe=UTF-8"
        response = requests.get(url)
        random_position = random.randint(0, len(response.text) - 20)
        return_value = "".join(list(reversed(query))) + " " + response.text[random_position:random_position + 10]
        print("google: " + return_value)
        return return_value

    def do_GET(self):
        oracle_prediction = self.search_google(self.search_github(self.random_string()))
        text_content = "The oracle has seen your future: \"" + oracle_prediction + "\""
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(text_content.encode('utf-8'))


class Server:
    def __init__(self, port):
        self.port = port

    def run(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, RequestHandler)
        httpd.serve_forever()


server = Server(int(sys.argv[1]))
server.run()
