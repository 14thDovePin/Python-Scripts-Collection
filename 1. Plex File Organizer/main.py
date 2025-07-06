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
import re


# Format Console
os.system("title Plex File Organizer && color a")
TEST_MODE = True


def main():
    os.system("cls")

    # Prompt user for the movie/series directory & its type.
    if not TEST_MODE:
        while True:
            media_directory = input("Enter Media Directory: ")

            if not os.path.exists(media_directory):
                print("Invalid Directory!")
            else:
                break

        print("\nMedia Type")
        print("1 -> Movie")
        print("2 -> Series\n")

        while True:
            media_type = input("Enter Type: ")

            if media_type == "1" or media_type == "2":
                break
            else:
                print("Invalid Type!")

    # Extract file names.
    if not TEST_MODE:
        filenames = []
        for _, _, files in os.walk(media_directory):
            filenames = files
            break
    else:
        # Find Samples
        directory = __file__.split('\\')[:-1]
        directory = '\\'.join(directory)
        directory += '\\samples_ignore.json'

        # Process Samples
        with open(directory, 'r') as f:
            raw_string = ""
            for i in f.readlines(): raw_string += i
            filenames = json.loads(raw_string)

    # Cleanup Filename/s
    clean_filenames = [clean_filename(i) for i in filenames]

    for i in clean_filenames: print(i)
    input("Press Any Key To Exit")

    # Extract title metadata from OMDb
    if media_type == "1":
        pass

    # Extract series title from IMDb
    elif media_type == "2":
        pass


def clean_filename(filename: str) -> str:
    """Return a clean filename."""
    # Check File Extension

    # Pull all word sequences.
    pattern_raw = r'[^. \s]+'
    results_raw = re.findall(pattern_raw, filename)

    # For Movies ---
    # Cut list from start to the last date detected.
    pattern_date = r'19\d\d|20\d\d'
    results_raw.reverse()
    date = None

    for item in results_raw:
        if re.search(pattern_date, item):
            date = item
            break

    results_raw.reverse()

    if date:
        date_index = results_raw.index(date)
        results_rough = results_raw[:date_index+1]
    else:
        results_rough = results_raw

    return results_rough


if __name__ == "__main__":
    while True:
        main()
