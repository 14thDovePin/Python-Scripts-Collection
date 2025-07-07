""" June 30, 2025
What is this script about?
This script formats any Movie or Series file names into their proper
titles that are readable by Plex's media file namescheming.

How does it work?
Below is the script's procedure. (may change as the script is developed)

1. Locate the files for the media.
2. Determine media type.
3. Obtain the title from the movies metadata from OMDb or IMDb.
4. Format title to Plex's media file namescheming.
5. Rename all media files.
"""

import json
import os

from process_filename import process_filename, print_pf


TEST_MODE = True


def main():

    # Prompt User
    if not TEST_MODE:
        # Prompt Files Directory
        while True:
            media_directory = input("Enter Media Directory: ")

            if not os.path.exists(media_directory):
                print("Invalid Directory!")
            else:
                break

        print("\nMedia Type")
        print("1 -> Movie")
        print("2 -> Series\n")

        # Prompt Type
        while True:
            media_type = input("Enter Type: ")

            if media_type == "1" or media_type == "2":
                break
            else:
                print("Invalid Type!")

    # Extract Filenames
    if not TEST_MODE:
        filenames = []
        for _, _, files in os.walk(media_directory):
            filenames = files
            break
    else:
        # For TEST_MODE Only
        # Locate Samples
        directory = __file__.split('\\')[:-1]
        directory = '\\'.join(directory)
        directory += '\\samples_ignore.json'

        # Extract Samples
        with open(directory, 'r') as f:
            raw_string = ""
            for i in f.readlines(): raw_string += i
            filenames = json.loads(raw_string)

    # Cleanup Filename/s
    clean_filenames = [process_filename(i) for i in filenames]

    for i in clean_filenames:
        # print(' '.join(i[:-1]) + i[-1])
        print_pf(i)
    input("Press Any Key To Exit")

    # Extract metadata from OMDb with current title.
    # If it fails, prompt user to manually input title & year
    # to match & extract metadata from.

    # Extract title metadata from OMDb
    if media_type == "1":
        pass

    # Extract series title from IMDb
    elif media_type == "2":
        pass

    # Prompt user it title, year, and type is correct.


if __name__ == "__main__":
    # Format Console
    commands = [
        "title Plex File Organizer",
        "color a",
        "cls"
    ]

    for cmd in commands:
        os.system(cmd)

    # Run Script
    while True:
        main()
