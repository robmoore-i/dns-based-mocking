from http.server import *


class TestDoubleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers.get('Host'))

        text_content = ""
        for k in TestDoubleServer.mappings:
            if self.headers.get('Host') == k:
                text_content = TestDoubleServer.mappings[k]
                break

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(text_content.encode('utf-8'))


TestDoubleServer.mappings = {}


def stub(hostname, text_to_return):
    TestDoubleServer.mappings[hostname] = text_to_return


def activate_double():
    https_server_address = ('', 80)
    httpd = HTTPServer(https_server_address, TestDoubleServer)
    httpd.serve_forever()
