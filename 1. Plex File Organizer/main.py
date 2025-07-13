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
import pprint

from colorama import Fore, Back, Style

from process_filename import process_filename, fn_check
from request_omdb import request_metadata
from utils.colors import Colors
from utils.templates import GenerateTemplate


TEST_MODE = False


def main():
    # PROMPT USER
    if not TEST_MODE:
        # Prompt Files Directory
        while True:
            media_directory = c.input("Enter Media Directory: ")

            if not os.path.exists(media_directory):
                c.print_error("Invalid Directory!")
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

        media_directory = os.getcwd()

    # PROCESS VIDEO FILES
    video_files_information = []
    directory_title_sequence = process_filename(directory_name)

    # Process Video Files Information
    for file in filenames:
        # Allow only video files.
        if not fn_check(file):
            continue

        # Process file metadata and information.
        file_metadata = gt.metadata()
        file_info = gt.file_info()

        title_sequence = process_filename(file, file_metadata, file_info)
        file_info['path'] = media_directory

        # Store & Append Information
        vf_information = gt.video_file_information()
        vf_information['title_sequence'] = title_sequence
        vf_information['metadata'] = file_metadata
        vf_information['file_information'] = file_info
        video_files_information.append(vf_information)

    sample = request_metadata(directory_title_sequence)
    pprint.pp(sample)
    print()
    pprint.pp(video_files_information)

    input("Press Any Key To Exit")
    exit()


if __name__ == "__main__":
    # Script Setup
    c = Colors()
    gt = GenerateTemplate()

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
