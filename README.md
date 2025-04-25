# WiFiPassX  
**WiFi Password Extractor Tool**  

<img src="https://img.shields.io/badge/Category-Security_Tools-blue" alt="Category">
<img src="https://img.shields.io/badge/Platform-CircuitPython-green" alt="Platform">



## 📌 Project Introduction
**WiFiPassX** is a tool for extracting passwords for WiFi networks that are stored on a system.

## 🌟 Main Features
- Advanced HID device emulation
- Minimize the PowerShell window to hide it.
- Clear command history in PowerShell
- LED to display information to the hacker about the operation progress
- Equipped with a process start button
- Save data as a txt file on your board

## ❓ Help
This program extracts all the WiFi passwords that a computer system is connected to and saves them as a P.txt file on your board.

## 🛠️ Configuration
Download `adafruit_hid` from github: https://github.com/adafruit/Adafruit_CircuitPython_HID & add `adafruit_hid` to lib directory of raspberry pi pico

---
``$l="CIRCUITPY"``: **CIRCUITPY** is name of drive that This is the drive name that appears after the board is inserted into the system (it must match the drive name that the board has)
- You can even connect a separate memory to the system, in which case **CIRCUITPY** must match the memory name.
---
``$f="P.txt"``: **P.txt** is name of file that save in board or memory

---
For small window size you should insert ``SMALL_SHELL_WINDOW`` in ``pass_stealer()`` 
EX:``pass_stealer(command=SMALL_SHELL_WINDOW)`` or ``pass_stealer(SMALL_SHELL_WINDOW)``
- To use this option, you must use Run as Administrator

For Run as Administrator: You should use ``open_power_shell(run_as_admin=True)``

---
To start the process there is a button embedded on pin **GP1** which you need to press to start the process (connect GP1 to GND)

