from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import urlopen
from urllib.error import URLError
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, content_type, body = 200, "text/plain", b"ok"
        if self.path == "/" and os.getenv("CATALOG_URL"):
            try:
                with urlopen(os.environ["CATALOG_URL"], timeout=2) as response:
                    book = response.read().decode().strip()
                from html import escape
                content_type = "text/html; charset=utf-8"
                body = f"<meta charset='utf-8'><title>Biblioteca demo</title><h1>Biblioteca demo</h1><p>Libro disponible: {escape(book)}</p>".encode()
            except (URLError, TimeoutError):
                status, body = 503, b"Catalog unavailable"
        elif self.path == "/book" and not os.getenv("CATALOG_URL"):
            body = b"Don Quijote"
        elif self.path != "/health":
            status, body = 404, b"Not found"
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
