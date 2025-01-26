from http.server import HTTPServer, BaseHTTPRequestHandler
from engine import Engine
import sys
import signal
from urllib.parse import urlparse, parse_qs


# Open engine API
if (len(sys.argv) != 2):
    print(f"usage: python {sys.argv[0]}.py path/to/engine")
    exit(1)
myengine = Engine()
print("Opening chess engine API...", end="", flush=True)
myengine.open(sys.argv[1])
print("done", flush=True)


# Listen for interrupt signal to close engine API (Ctrl+C)
def handler():
    print("Closing chess engine API...", end="", flush=True)
    myengine.close()
    print("done")
    exit(0)
signal.signal(signal.SIGINT, handler)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(202)
        self.end_headers()
        query = parse_qs(urlparse(self.path).query)
        print("fen:", query["fen"][0])
        print("wtime:", query["wtime"][0])
        print("btime:", query["btime"][0])
        move = myengine.search(query["fen"][0], float(query["wtime"][0]), float(query["btime"][0]))
        self.wfile.write(bytes(move, encoding="utf-8"))


httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1