from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Ontvangen data:", post_data.decode('utf-8'))
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'status': 'OK'}
        self.wfile.write(json.dumps(response).encode('utf-8'))

server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
print("Mock API draait op http://localhost:8080")
server.serve_forever()
