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
import os
import time

import psutil


# The list of programs the user want's to time track.
PROGRAMS = [
    "Chrome",
    "Discord"
]
DATA_FILEPATH = os.path.join(
    os.getenv("userprofile"),
    r'Documents\Software Runtime Tracker'
)
DATA_FILENAME = 'data.json'
FULL_FILEPATH = os.path.join(DATA_FILEPATH, DATA_FILENAME)


def main():
    """Main function of the script"""
    # Create data json file if it doesn't exist yet.
    if not os.path.exists(DATA_FILEPATH):
        # Create Data
        data = {}
        for program in PROGRAMS:
            build_data(program.lower(), data)

        # Create File & Write Data
        write_data = json.dumps(data, indent=4)
        os.mkdir(DATA_FILEPATH)

        with open(FULL_FILEPATH, 'w') as f:
            f.writelines(write_data)

    input('Success')

    process = find_process("Chrome")
    if process:
        print("Success")
    else:
        print("Fail")

    # Rest
    time.sleep(5)


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


def build_data(process_name: str, data: dict) -> None:
    """Builds the data structure of a process inside a given dictionary."""
    data[process_name.lower()] = {
        "raw_seconds" : int(),
        "raw_minutes" : int(),
        "raw_hours" : int(),
        "raw_days" : int(),
        "raw_months" : int(),
        "raw_years" : int(),
        "seconds" : int(),
        "minutes" : int(),
        "hours" : int(),
        "days" : int(),
        "months" : int(),
        "years" : int(),
        "time_elapsed" : str()
    }


def process_time(seconds: int, data: dict) -> None:
    """Converts raw seconds to their respective format to insert in a give dict data."""
    gm_time = time.gmtime(seconds)

    # Calculate Raw Time
    raw_mins = seconds // 60
    raw_hours = raw_mins // 60
    raw_days = raw_hours // 24
    raw_months = raw_mins // 43830
    raw_years = raw_mins // 525960

    data["raw_minutes"] = raw_mins
    data["raw_hours"] = raw_hours
    data["raw_days"] = raw_days
    data["raw_months"] = raw_months
    data["raw_years"] = raw_years

    # Calculate Time
    years = seconds // 31557600
    seconds -= years * 31557600 if years > 0 else 0

    months = seconds // 2629800
    seconds -= months * 2629800 if months > 0 else 0

    days = seconds // 86400
    seconds -= days * 86400 if days > 0 else 0

    hours = seconds // 3600
    seconds -= hours * 3600 if hours > 0 else 0

    minutes = seconds // 60
    seconds -= minutes * 60 if minutes > 0 else 0

    data["seconds"] = seconds
    data["minutes"] = minutes
    data["hours"] = hours
    data["days"] = days
    data["months"] = months
    data["years"] = years

    time_elapsed = f"{years} Year/s, {months} Month/s, {days} Day/s, "
    time_elapsed += f"{hours} Hour/s, {minutes} Minute/s, {seconds} Seconds"

    data["time_elapsed"] = time_elapsed


if __name__ == "__main__":
    main()
