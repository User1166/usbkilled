# usbkilled
When you plug or unplug a usb, you can run commands like shutdowning computer or downloading files

# USB Device Monitor with White-list Functionality
This project provides a Python script that monitors USB devices on a Windows system. The script watches for USB devices being connected and disconnected. If a USB device is added or removed, the script checks whether the device is on a white-list. If it is, a specific function is called to handle allowed devices. If the device is not on the white-list, separate functions are called to handle device addition and removal, and an entry is made in a log file.

# Features
White-list Support: Devices on the white-list trigger a specific function when connected.
Logging: USB device addition and removal events are logged with a timestamp.
Differentiated Behavior: Custom functions for white-listed devices and other USB devices.
# Project Components
monitor_usb_devices(): The main function that monitors USB device events and handles logic based on the white-list.
run_custom_command_if_whitelisted(device_ids): This function checks if a device is on the white-list and, if so, triggers a special action.
log_usb_event(event_type, device_ids): This function logs USB device events to a text file.
whitelist.json: A JSON file that stores the list of white-listed USB devices.
# Usage
To use this script, ensure you have the necessary dependencies installed (e.g., wmi). Create or update whitelist.json with the list of allowed USB device IDs.
You can change the func.py file for changing the functions
Install Dependencies: Make sure you have Python and the wmi package installed.
Set Up White-list: Update whitelist.json with the device IDs of USB devices that should be allowed.
Run the Script: Execute the script to start monitoring USB device events.
## Note
This script is designed for Windows systems and uses the wmi module to interact with the system's USB devices.
Exercise caution when using scripts that monitor system hardware, and ensure appropriate security measures are in place.
