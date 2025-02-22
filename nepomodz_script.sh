#!/bin/bash

# nepomodz_script.sh
# Script created by NEPOMODZ

# Function to print colorful messages
print_message() {
    echo -e "\e[1;36m=============================================\e[0m"
    echo -e "\e[1;36m            Welcome to NEPOMODZ's Script       \e[0m"
    echo -e "\e[1;36m=============================================\e[0m"
    echo -e "\e[1;33mThis script will help you set up the environment.\e[0m"
    echo -e "\e[1;33mPlease follow the instructions below.\e[0m"
}

# Function to list required packages
list_packages() {
    echo -e "\e[1;32m=== Required Packages ===\e[0m"
    echo -e "\e[1;32m1. Python\e[0m"
    echo -e "\e[1;32m2. Git\e[0m"
    echo -e "\e[1;32m3. Flask (Python library)\e[0m"
    echo -e "\e[1;32m4. Requests (Python library)\e[0m"
    echo -e "\e[1;32m5. OpenCV (Python library, optional for camera)\e[0m"
}

# Function to print installation commands
print_commands() {
    echo -e "\e[1;35m=== Installation Commands ===\e[0m"
    echo -e "\e[1;35m1. Install Python:\e[0m"
    echo -e "\e[1;35m   pkg install python -y\e[0m"
    echo -e "\e[1;35m2. Install Git:\e[0m"
    echo -e "\e[1;35m   pkg install git -y\e[0m"
    echo -e "\e[1;35m3. Install Flask:\e[0m"
    echo -e "\e[1;35m   pip install flask\e[0m"
    echo -e "\e[1;35m4. Install Requests:\e[0m"
    echo -e "\e[1;35m   pip install requests\e[0m"
    echo -e "\e[1;35m5. Install OpenCV (optional):\e[0m"
    echo -e "\e[1;35m   pip install opencv-python\e[0m"
}

# Main script
print_message
list_packages
print_commands

# Ask for permission
echo -e "\e[1;31mDo you want to continue? (y/n)\e[0m"
read permission

if [ "$permission" != "y" ]; then
    echo -e "\e[1;31mScript execution cancelled.\e[0m"
    exit 1
fi

# Grant Termux storage access
echo -e "\e[1;33mGranting Termux storage access...\e[0m"
termux-setup-storage

# Clone the repository
echo -e "\e[1;33mCloning the repository...\e[0m"
if [ -d "yourrepository" ]; then
    echo -e "\e[1;33mRepository already exists. Pulling latest changes...\e[0m"
    cd yourrepository
    git pull
else
    git clone https://github.com/yourusername/yourrepository.git
    if [ $? -ne 0 ]; then
        echo -e "\e[1;31mFailed to clone the repository. Please check the URL and try again.\e[0m"
        exit 1
    fi
    cd yourrepository
fi

# Run the Python server
echo -e "\e[1;33mStarting NEPOMODZ's Python server...\e[0m"
python nepomodz_server.py
