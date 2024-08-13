import http.server
import socketserver
import os

PORT = 8000

class CustomContentRequestHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if (self.path.startswith("/ui/api/query")):
            return 'application/json'
        return super().guess_type(path)

Handler = CustomContentRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()