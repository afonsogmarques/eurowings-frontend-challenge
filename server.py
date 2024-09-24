import json
from flight_data import flight_data
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      self.send_response(200)
      # self.send_response(500, 'Something went wrong')

      self.send_header('Content-type', 'application/json')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      
      self.wfile.write(json.dumps(flight_data).encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
