""" July 18, 2025
What is this script about?
This script acts like a watchdog for specific softwares. When it detects a software
that is part of the watchlist, it will log that time and date into a data file, likewise
it will also log when it can't detect the software/program anymore.

This script is also designed to be paired with NSSM to run as a Windows service.

How does it work?
Below is the script's procedure. (may change as the script is developed)

1. Scan windows processes.
2. Check if any any of the listed programs matches a case inside the processes.
3. Log matched cases and flag progam in list as running.
4. If a program flagged as running has not been detected, log it in the file.

External Libraries Used:
  psutil

Developer Notes
I'm going to make this script for a specific case for now, in the future
I might add extra features that allows integration and tracking of more than
a single program.
"""
import json
from time import sleep

import psutil


def main():
    """Main function of the script"""

    process = find_process("Chrome")
    if process:
        print("Success")
    else:
        print("Fail")

    # Rest
    sleep(5)


def find_process(process_name: str) -> psutil.Process:
    """Return a process on a given process name."""
    # Scan through each process.
    process_numbers = psutil.pids()

    for pn in process_numbers:
        try:
            process = psutil.Process(pn)

            # Check if the given process name is inside the process.
            if process_name.lower() in process.name().lower():
                return process

        except:
            pass

    return None


if __name__ == "__main__":
    # Run Script
    while True:
        main()
