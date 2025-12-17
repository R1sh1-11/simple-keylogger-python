# Simple Python Keylogger ⌨️

A keylogger tool built in Python using the `pynput` library. This project demonstrates the mechanics of input monitoring, event listeners, and file handling in a Windows environment.

**DISCLAIMER: This project is for educational purposes only (I am not trying to get in trouble).**
This tool was created to understand the security implications of keylogging and input monitoring. Do not use this software on any system where you do not have explicit permission from the owner!

## Features/Instructions:
* **Live Logging:** Captures all alphanumeric keys and special characters.
* **Timestamping:** detailed logs with date and time for every keystroke (`YYYY-MM-DD HH:MM:SS`).
* **Kill Switch:** Press `Esc` to immediately terminate the script.
* **Stealth:** Runs in the background (terminal) until terminated.

## How to Install:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/R1sh1-11/simple-keylogger-python.git](https://github.com/R1sh1-11/simple-keylogger-python.git)

2. **Install Dependencies**
pip install -r requirements.txt

## Run the Script:
python main.py

**Security Note:**
This script may be flagged by Windows Defender (eyeroll). It will continue to delete main.py until and unless you add an exclusion to your specific project file.