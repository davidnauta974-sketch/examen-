from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from html import escape
from urllib.request import urlopen
from urllib.error import URLError
import os

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Biblioteca demo</title>
<style>
:root { color-scheme: dark; font-family: 'Segoe UI', sans-serif; background: #101c18; color: #f9f2df; }
* { box-sizing: border-box; }
body { margin: 0; background: radial-gradient(ellipse at top right,#304c36,transparent 64%); min-height: 100vh; }
main { max-width: 980px; margin: auto; padding: clamp(24px,7vw,76px); }
header { display:flex; justify-content:space-between; gap:16px; align-items:center; padding-bottom:20px; border-bottom:1px solid #596b55; }
strong { letter-spacing:.12em; text-transform:uppercase; font-size:.8rem; }
small { color:#c9e5ae; }
article { display:grid; grid-template-columns:minmax(125px,1fr) 2fr; align-items:center; gap:clamp(22px,6vw,64px); margin-top:40px; }
.cover { aspect-ratio: .77; display:grid; place-items:center; border:1px solid #edd3a1; border-radius:6px 22px 22px 6px; background: repeating-radial-gradient(ellipse at 35% 65%,#ac794c 0 2px,#563928 3px 19px); box-shadow:10px 14px 0 #09110b; }
.cover span { padding: .3em .4em; color:#ffe2a4; background:#563928; border:1px solid; font:clamp(32px,8vw,88px) Georgia,serif; }
h1 { font:clamp(37px,8vw,84px)/.98 Georgia,serif; margin:14px 0; text-wrap:balance; }
p { color:#d1dacb; line-height:1.55; margin:0; }
@media(max-width:460px) { article { grid-template-columns:1fr; } .cover { max-width:145px; } }
</style></head><body><main>
<header><strong>Biblioteca demo</strong><small>● Catálogo disponible</small></header>
<article><div class="cover" aria-hidden="true"><span>B</span></div>
<section><small>Libro disponible</small><h1>{title}</h1>
<p>El servicio web consultó el catálogo y recibió este título.</p></section></article>
</main></body></html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, content_type, body = 200, "text/plain", b"ok"
        if self.path == "/" and os.getenv("CATALOG_URL"):
            try:
                with urlopen(os.environ["CATALOG_URL"], timeout=2) as response:
                    book = response.read().decode().strip()
                content_type = "text/html; charset=utf-8"
                body = PAGE.replace("{title}", escape(book)).encode("utf-8")
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
