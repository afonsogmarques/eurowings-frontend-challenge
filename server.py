import json
from http.server import BaseHTTPRequestHandler, HTTPServer

static_data = [
  {
    "origin": "OPO",
    "destination": "FCO",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 128,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a1",
  },
  {
    "origin": "LIS",
    "destination": "AMD",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 95,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a2",
  },
  {
    "origin": "LHR",
    "destination": "BUD",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 46,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a3",
  },
  {
    "origin": "AMD",
    "destination": "FCO",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 83,
      "currency": "EUR"
    },
    "offerType": "ExactMatch",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a4",
  },
  {
    "origin": "PRG",
    "destination": "MAD",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 253,
      "currency": "EUR"
    },
    "offerType": "ExactMatch",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a5",
  },
  {
    "origin": "ORY",
    "destination": "LHR",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 435,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a6",
  },
  {
    "origin": "FCO",
    "destination": "BUD",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 128,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a1",
  },
  {
    "origin": "BUD",
    "destination": "PRG",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 95,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a2",
  },
  {
    "origin": "BUD",
    "destination": "OPO",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 46,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a3",
  },
  {
    "origin": "MAD",
    "destination": "LIS",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 83,
      "currency": "EUR"
    },
    "offerType": "ExactMatch",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a4",
  },
  {
    "origin": "LIS",
    "destination": "ORY",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 253,
      "currency": "EUR"
    },
    "offerType": "ExactMatch",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a5",
  },
  {
    "origin": "OPO",
    "destination": "LIS",
    "departureDate": "2024-10-31",
    "returnDate": "2024-11-02",
    "seatAvailability": 47,
    "price": {
      "amount": 435,
      "currency": "EUR"
    },
    "offerType": "BestPrice",
    "uuid": "SA00003-b790715d-b2b8-4d23-ac27-d4e88c0e84a6",
  },
]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      self.send_response(200)
      # self.send_response(500, 'Something went wrong')

      self.send_header('Content-type', 'application/json')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      
      self.wfile.write(json.dumps(static_data).encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
