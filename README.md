Network Information Collector
This repository contains a Python script, NetworkInfoCollector.py, that collects and displays detailed information about the network connections on your machine.

Features
IP Address Collection: The script collects all the local and remote IP addresses used by the machine and stores them in a list.

Timezone Information: The script can determine the timezone based on latitude and longitude using the TimezoneFinder library.

Detailed Connection Information: The script provides detailed information about each network connection, including the process name and process ID.

useful for monitoring hidden processes, which are not shown in the task manager 

Usage
To use this script, simply run NetworkInfoCollector.py. The script will continuously monitor the network connections on your machine and print information about them to the console.

Dependencies
This script uses the psutil and timezonefinder Python libraries. You can install these with pip:

pip install psutil timezonefinder

Note
This script is intended for educational purposes and should be used responsibly.
