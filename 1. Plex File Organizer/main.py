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

from colorama import Fore, Back, Style

from utils.colors import Colors
from process_filename import process_filename, print_pf
from request_omdb import request_metadata


TEST_MODE = False


def main():
    # Prompt User
    if not TEST_MODE:
        # Prompt Files Directory
        while True:
            media_directory = C.input("Enter Media Directory: ")

            if not os.path.exists(media_directory):
                C.print_error("Invalid Directory!")
            else:
                break

        # Extract Directory Name
        directory_name = media_directory.split('\\').pop()

        # Extract Filenames
        _, _, filenames = next(os.walk(media_directory))

    if TEST_MODE:
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
    processed_filenames = [process_filename(i) for i in filenames]

    for i in processed_filenames:
        # print_pf(i)
        request_metadata(i)
    input("Press Any Key To Exit")

    # Extract metadata from OMDb with current title.
    # If it fails, prompt user to manually input title & year
    # to match & extract metadata from.


if __name__ == "__main__":
    # Format Console
    C = Colors()

    # Run Windows terminal commands.
    commands = [
        "title Plex File Organizer",
        "cls"
    ]

    for cmd in commands:
        os.system(cmd)

    # Run Script
    while True:
        main()
