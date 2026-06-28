#!/usr/bin/env python3
"""
Bridge & Bloom — Local Development Server
Run: python3 server.py
Then open: http://localhost:8888
"""

import http.server
import socketserver
import os
import webbrowser
from threading import Timer

# PORT = 8080
PORT = 8888
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")


def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\n" + "="*48)
        print("  🌸  Bridge & Bloom — Local Server")
        print("="*48)
        print(f"  Serving at:  http://localhost:{PORT}")
        print(f"  Directory:   {DIRECTORY}")
        print("  Press Ctrl+C to stop.\n")

        # Auto-open browser after short delay
        Timer(0.5, open_browser).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped. Goodbye! 🌸\n")
