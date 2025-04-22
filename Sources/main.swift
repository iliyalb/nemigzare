import Vapor

let html = """
<!DOCTYPE html>
<html>
<head>
    <title>DVD Logo</title>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <style>
        body { 
            margin: 0; 
            overflow: hidden; 
            background: black;
        }
        #dvd {
            position: absolute;
            width:  200px;
            height: 200px;
            filter: brightness(0) invert(1);
        }
    </style>
</head>
<body>
    <img id="dvd" src="/dvd.png">
    <script>
        const dvd = document.getElementById('dvd');
        let x = window.innerWidth / 2;
        let y = window.innerHeight / 2;
        let dx = 3;
        let dy = 2;

        function randomColor() {
            const r = Math.random() * 0.7 + 0.3;
            const g = Math.random() * 0.7 + 0.3;
            const b = Math.random() * 0.7 + 0.3;
            return `rgb(${r * 255},${g * 255},${b * 255})`;
        }

        function animate() {
            x += dx;
            y += dy;

            if (x <= 0 || x >= window.innerWidth - 100) {
                dx *= -1;
                dvd.style.filter = `brightness(0) invert(1) opacity(1) drop-shadow(0 0 0 ${randomColor()})`;
            }
            
            if (y <= 0 || y >= window.innerHeight - 50) {
                dy *= -1;
                dvd.style.filter = `brightness(0) invert(1) opacity(1) drop-shadow(0 0 0 ${randomColor()})`;
            }

            dvd.style.left = x + 'px';
            dvd.style.top = y + 'px';
            requestAnimationFrame(animate);
        }

        animate();
    </script>
</body>
</html>
"""

struct DVDApp {
    static func main() throws {
        let app = try Application(.detect())
        defer { app.shutdown() }
        
        // Configure middleware to serve files from the Assets directory
        app.middleware.use(FileMiddleware(publicDirectory: "Assets"))
        
        // Serve the main page as raw HTML for now
        app.get { req -> Response in
            return Response(
                status: .ok,
                headers: ["Content-Type": "text/html"],
                body: .init(string: html)
            )
        }
        
        // Create a WebSocket route
        app.webSocket("ws") { req, ws in
            ws.send("Connected to DVD Screensaver!")
            
            ws.onText { ws, text in
                ws.send(text)
            }
        }
        
        try app.run()
    }
}

try DVDApp.main()
