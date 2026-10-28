from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent.resolve()

class SiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def send_head(self):
        path = self.translate_path(self.path)
        if not Path(path).exists() and not self.path.startswith('/assets/') and '.' not in Path(self.path).name:
            self.path = '/index.html'
        return super().send_head()

if __name__ == '__main__':
    print('A.S. Computer Education running at http://localhost:8000')
    ThreadingHTTPServer(('127.0.0.1', 8000), SiteHandler).serve_forever()
