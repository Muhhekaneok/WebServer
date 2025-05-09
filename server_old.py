from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "templates/index.html"
        elif self.path.startswith("/static/"):
            self.path = self.path.lstrip("/")
        elif self.path.endswith(".js") or self.path.endswith(".css") or self.path.endswith(".png"):
            self.path = self.path.lstrip("/")
        else:
            self.send_error(404, "File not found")
            return

        return super().do_GET()


if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"The server is running: http://localhost:{PORT}")
    httpd.serve_forever()
