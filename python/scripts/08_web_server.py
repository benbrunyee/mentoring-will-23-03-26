# =============================================================================
# WEB SERVER
# Concepts: http.server (built-in module), classes, inheritance,
#           how HTTP works, serving HTML, request/response cycle
# =============================================================================
#
# Run this script, then open http://localhost:8080 in your browser.
# Press Ctrl+C in the terminal to stop the server.
#
# No external libraries needed — http.server is built into Python.
# =============================================================================

import http.server
import json
from datetime import datetime, timezone

PORT = 8080

# ---------------------------------------------------------------------------
# The HTML page we'll serve — stored as a Python string.
# In a real web app you'd keep this in a separate .html file.
# ---------------------------------------------------------------------------

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Web Server</title>
    <style>
        body  { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; padding: 0 20px; background: #f5f5f5; }
        h1    { color: #2c3e50; }
        p     { color: #555; line-height: 1.6; }
        .card { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        code  { background: #eee; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
        a     { color: #3498db; }
    </style>
</head>
<body>
    <h1>Hello from Python!</h1>

    <div class="card">
        <p>This page is being served by a Python script using nothing but the
        built-in <code>http.server</code> module — no extra software needed.</p>
        <p>Every time you reload this page, your browser sends an <strong>HTTP GET
        request</strong> to Python, which responds with this HTML.</p>
    </div>

    <div class="card">
        <h2>Try these URLs</h2>
        <ul>
            <li><a href="/">/</a> &mdash; This page (HTML)</li>
            <li><a href="/time">/time</a> &mdash; Current server time (JSON)</li>
            <li><a href="/about">/about</a> &mdash; About page</li>
        </ul>
    </div>
</body>
</html>
"""

ABOUT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About - Python Web Server</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; padding: 0 20px; background: #f5f5f5; }
        h1   { color: #2c3e50; }
        .card { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        a { color: #3498db; }
    </style>
</head>
<body>
    <h1>About</h1>
    <div class="card">
        <p>This is a simple web server written in Python for learning purposes.</p>
        <p>It demonstrates how HTTP works: your browser sends a <strong>request</strong>,
        the server processes it and sends back a <strong>response</strong>.</p>
        <p><a href="/">Back to home</a></p>
    </div>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Request handler — this class decides what to send back for each URL
# ---------------------------------------------------------------------------

class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    We inherit from BaseHTTPRequestHandler and override do_GET to handle
    HTTP GET requests. Inheritance means we get all its built-in behaviour
    for free, and only write the parts we want to customise.
    """

    def do_GET(self):
        """This method is called automatically for every incoming GET request."""
        now = datetime.now(timezone.utc)

        match self.path:
            case "/":
                self.send_html(HTML_PAGE)
            case "/about":
                self.send_html(ABOUT_PAGE)
            case "/time":
                self.send_json({"time": now.strftime("%H:%M:%S UTC"),
                                "date": now.strftime("%A %d %B %Y")})
            case _:
                self.send_not_found()

    # ------------------------------------------------------------------
    # Helper methods for sending different types of responses
    # ------------------------------------------------------------------

    def send_html(self, html_content):
        """Send a 200 OK response with an HTML body."""
        body = html_content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, data):
        """Send a 200 OK response with a JSON body."""
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_not_found(self):
        """Send a 404 Not Found response."""
        body = b"<h1>404 - Page Not Found</h1>"
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        """Override the default logger to print a cleaner message."""
        print(f"  {self.address_string()} -> {fmt % args}")


# ---------------------------------------------------------------------------
# Start the server
# ---------------------------------------------------------------------------

def main():
    print("=== Python Web Server ===\n")
    print(f"Starting server on port {PORT}...")
    print(f"Open your browser and go to:  http://localhost:{PORT}")
    print("Press Ctrl+C to stop.\n")

    # TCPServer creates a socket that listens for incoming connections
    with http.server.HTTPServer(("", PORT), RequestHandler) as server:
        try:
            # serve_forever() keeps the server running until we stop it
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")


if __name__ == "__main__":
    main()
