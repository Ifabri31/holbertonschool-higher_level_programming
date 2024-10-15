#!/usr/bin/env python3
import http.server
import socketserver
import json

PORT = 8000
user_info = {"name": "John", "age": 30, "city": "New York"}
api_details = {"version": "1.0", "description": "A simple API built with http.server"}
json_user_info = json.dumps(user_info)
json_api_details = json.dumps(api_details)

class CustomHTTPHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/user":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_user_info, "utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))

        elif self.path == "/api-info":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_api_details, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Error: Endpoint not found")

with socketserver.TCPServer(("", PORT), CustomHTTPHandler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()
