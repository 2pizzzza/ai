import http.server
import os
import socketserver
import subprocess
import asyncio

PORT = 8000
UPLOAD_DIR = "media"


class VideoUploadHandler(http.server.BaseHTTPRequestHandler):
    async def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_name = "uploaded_video.mp4"
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, 'wb') as file:
            file.write(data)

        self.wfile.write(b"Video uploaded successfully.")

        create_face_video = ["python", os.path.join('video_trimming_by_face.py')]
        create_pass_video = ["python", os.path.join('video_trimming.py')]

        await asyncio.gather(
            self.async_run_command(create_face_video),
            self.async_run_command(create_pass_video)
        )

    async def async_run_command(self, command):
        process = await asyncio.create_subprocess_exec(*command)
        await process.wait()


if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), VideoUploadHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
