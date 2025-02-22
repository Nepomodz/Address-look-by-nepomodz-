#!/bin/bash

# nepomodz_script.sh
# Script created by NEPOMODZ

echo "Welcome to nepomodz's script!"

# Function to check and install packages
install_pkg() {
    if ! pkg list-installed | grep -q "$1"; then
        echo "Installing $1..."
        pkg install "$1" -y
    else
        echo "$1 is already installed."
    fi
}

# Function to check and install pip packages
install_pip() {
    if ! pip show "$1" &> /dev/null; then
        echo "Installing $1..."
        pip install "$1"
    else
        echo "$1 is already installed."
    fi
}

# Ask for permission
echo "Do you want to execute the script? (y/n)"
read permission

if [ "$permission" != "y" ]; then
    echo "Script execution cancelled."
    exit 1
fi

echo "Starting nepomodz's script..."

# Update and upgrade packages
echo "Updating and upgrading packages..."
pkg update -y && pkg upgrade -y

# Install required pkg packages
install_pkg "python"
install_pkg "git"
install_pkg "opencv-python"

# Install required pip packages
install_pip "flask"
install_pip "requests"
install_pip "opencv-python"

# Grant Termux storage access
echo "Granting Termux storage access..."
termux-setup-storage

# Clone the repository
echo "Cloning the repository..."
if [ -d "yourrepository" ]; then
    echo "Repository already exists. Pulling latest changes..."
    cd yourrepository
    git pull
else
    git clone https://github.com/yourusername/yourrepository.git
    if [ $? -ne 0 ]; then
        echo "Failed to clone the repository. Please check the URL and try again."
        exit 1
    fi
    cd yourrepository
fi

# Run the Python server
echo "Starting nepomodz's Python server..."
python nepomodz_server.py
