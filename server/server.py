
from http.server import SimpleHTTPRequestHandler, HTTPServer
import time

class Server(SimpleHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.05)
        super().do_GET()

    def copyfile(self, source, outputfile):
        while chunk := source.read(8192):
            outputfile.write(chunk)
            outputfile.flush()
            time.sleep(0.002)

HTTPServer(("localhost", 8000), Server).serve_forever()
