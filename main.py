from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

# Simple HTTP server to serve our files
def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server started at http://localhost:{port}")
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
