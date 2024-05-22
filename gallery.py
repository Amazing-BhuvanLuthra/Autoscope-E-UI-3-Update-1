from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Replace with your image directory path
image_dir = "/path/to/your/images"

class GalleryHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == "/":
      # Send HTML content with image paths
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".jpg") or f.endswith(".png")]
      html_content = f"""
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Image Gallery</title>
        <link rel="stylesheet" href="style.css">
      </head>
      <body>
        <h1>Image Gallery</h1>
        <div id="images">
          {"".join([f'<img src="{img}">' for img in images])}
        </div>
      </body>
      </html>
      """
      self.wfile.write(html_content.encode())
    else:
      # Handle other requests (optional)
      self.send_error(404, "Not found")

if __name__ == "__main__":
  PORT = 8000  # Adjust port if needed
  server_address = ('', PORT)
  httpd = HTTPServer(server_address, GalleryHandler)
  print(f"Serving gallery on http://localhost:{PORT}")
  httpd.serve_forever()
    
