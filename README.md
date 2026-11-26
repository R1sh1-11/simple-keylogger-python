# Simple Python Keylogger ⌨️

A keylogger tool built in Python using the `pynput` library. This project demonstrates the mechanics of input monitoring, event listeners, and file handling in a Windows environment.

**DISCLAIMER: This project was built for educational purposes only**
This tool was created to understand the security implications of keylogging and input monitoring. Do not use this software on any system where you do not have explicit permission from the owner!

## Features/Instructions:
* **Live Logging:** Captures all alphanumeric keys and special characters.
* **Timestamping:** detailed logs with date and time for every keystroke (`YYYY-MM-DD HH:MM:SS`).
* **Kill Switch:** Press `Esc` to immediately terminate the script.

## How to Install:

1. **Clone the repository**
   ```bash
   git clone [https://github.com/R1sh1-11/simple-keylogger-python.git](https://github.com/R1sh1-11/simple-keylogger-python.git)

2. **Install Dependencies**
pip install -r requirements.txt

## Run the Script:
python main.py

## Note on antivirus
Windows Defender correctly flags this script as a keylogger and may quarantine main.py. That is expected; it shows endpoint protection catching this behavior.

## Disclaimer
For educational use only. Run it only on machines you own or have explicit permission to test.
