from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

server = HTTPServer(("0.0.0.0", 8000), HelloHandler)

print("Server running on port 8000...")
server.serve_forever()
