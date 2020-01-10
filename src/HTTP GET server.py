from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import socketserver
import json
import os
import cgi

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        os.chdir(os.path.dirname(__file__))
        os.chdir("..")
        os.chdir("data")
        with open('data.json') as f:
            temp = json.load(f)
            self.philFile = json.dumps(temp).encode()

        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back the full json file
    def do_GET(self):
        self._set_headers()
        print("sending!!")
        self.wfile.write(self.philFile)
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print("Starting httpd port", port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()