# nepomodz Script

Welcome to the **nepomodz Script** repository! This project is a Python-based script designed for educational purposes to demonstrate how web servers, camera access, and location tracking work. Please read this document carefully before using the script.

---

## **Description**

This script consists of two main components:

1. **Python Flask Server (`nepomodz_server.py`)**:
   - Creates a local web server.
   - Requests access to the user's camera and location.
   - If access is granted, it captures images continuously and saves them to the `captured_images` directory.
   - Fetches the user's approximate location using their IP address.

2. **Termux Execution Script (`nepomodz_script.sh`)**:
   - Automates the setup process in Termux.
   - Installs all required packages (`pkg` and `pip`).
   - Clones this repository and runs the Python server.

---

## **Disclaimer**

⚠️ **This script is for educational purposes only.** ⚠️

- **Do not use this script for malicious purposes.**
- **Respect privacy laws and regulations.**
- **Obtain explicit consent from users before running this script on their devices.**
- **The creator of this script is not responsible for any misuse or illegal activities.**

By using this script, you agree to use it responsibly and ethically.

---

## **Features**

- **Automated Setup**: Installs all required packages automatically.
- **Camera Access**: Captures images if the user grants camera access.
- **Location Tracking**: Fetches approximate location using the user's IP address.
- **Continuous Capture**: Captures images every second until the server is stopped.
- **Termux Integration**: Works seamlessly in Termux with storage and camera access.

---

## **How to Use**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
