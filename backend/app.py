# Basit HTTP server
# Bu server 8080 portunda çalışır ve "/" isteğine cevap verir

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Eğer kullanıcı "/" adresine gelirse
        if self.path == "/":
            self.send_response(200)  # HTTP 200 OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            
            # Ekrana yazılacak cevap
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

# Server başlatma
if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Server started on port 8080")
    server.serve_forever()