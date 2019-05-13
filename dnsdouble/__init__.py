import os
import getpass
import atexit
import shutil
import json
from http.server import *

if getpass.getuser() != "root":
    print("This tool must be used as root because it modifies local DNS behavior")
    print("Previous behaviour is restored on process exit")
    print("This tool does what it does by appending lines to /etc/hosts")
    exit(1)


def reset_etc_hosts_file():
    shutil.copy2("hosts", "/etc/hosts")
    print("Reset /etc/hosts to original")
    os.remove("hosts")
    print("Deleted the backup copy of /etc/hosts, which has now been reset to its previous behaviour")


atexit.register(reset_etc_hosts_file)


def copy_etc_hosts_file():
    shutil.copy2("/etc/hosts", "hosts")
    print("Saved current state of /etc/hosts")


copy_etc_hosts_file()


def append_localhost_redirect_to_etc_hosts_file(hostname):
    line_to_add = "127.0.0.1\t" + hostname + "\n"
    with open("/etc/hosts", "a") as hosts_file:
        hosts_file.write(line_to_add)


dns_mocks_host = "dnsmocks.local"
append_localhost_redirect_to_etc_hosts_file(dns_mocks_host)


class TestDoubleServer(BaseHTTPRequestHandler):
    request_paths = {}

    def request_host(self):
        return self.headers.get('Host')

    def do_GET(self):
        self.send_response(200)
        if self.request_host() == dns_mocks_host:
            self.send_mocks_information()
        else:
            self.send_stubbed_response()

    def send_mocks_information(self):
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(self.request_paths).encode('utf-8'))

    def send_stubbed_response(self):
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(self.get_text_content().encode('utf-8'))

    def get_text_content(self):
        text_content = ""
        for k in TestDoubleServer.mappings:
            if self.request_host() == k:
                text_content = TestDoubleServer.mappings[k]
                self.request_paths[k] = self.path
                break
        return text_content


TestDoubleServer.mappings = {}


def stub(hostname, text_to_return):
    TestDoubleServer.mappings[hostname] = text_to_return
    append_localhost_redirect_to_etc_hosts_file(hostname)


def activate_double():
    https_server_address = ('', 80)
    httpd = HTTPServer(https_server_address, TestDoubleServer)
    httpd.serve_forever()
