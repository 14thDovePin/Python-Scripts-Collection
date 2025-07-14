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

External Libraries Used:
  colorama
  dotenv
  googlesearch-python

Developer Notes
I overengineered this a little bit. But that's part
of trying to implement new things I've learned!
"""

import json
import os
import pprint
import re

from colorama import Fore, Back, Style
from googlesearch import search

from process_filename import process_filename, fn_check
from request_omdb import request_metadata
from utils.colors import Colors
from utils.templates import GenerateTemplate


TEST_MODE = False


def main():
    c.print_colored('PROCESSING MEDIA... ', Fore.LIGHTMAGENTA_EX, end='')
    print('[Type "', end='')
    c.print_warning('exit', end='')
    print('" or "', end='')
    c.print_warning('quit', end='')
    print('" to end script...]')

    # PROMPT USER
    if not TEST_MODE:
        # Prompt Files Directory
        while True:
            media_directory = c.input("Enter Media Directory: ")

            if media_directory.lower() in ['exit', 'quit']:
                c.reset()
                exit()

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

    # Request through each unique title sequence.
    # Prompt user to select the correct title sequence if there are multiple.
    title_sequences = []
    title_sequences.append(directory_title_sequence)

    for info in video_files_information:
        ts = info['title_sequence']
        if ts not in title_sequences:
            title_sequences.append(ts)

    # Grab IMDb IDs by parsing each title with Google.
    imdb_ids = []
    imdb_id_pattern = r'\/(tt\d+)\/'

    for title in title_sequences:
        full_title = ' '.join(title)

        print("Parsing Title > [", end='')
        c.print_colored(full_title, Fore.LIGHTMAGENTA_EX, end='')
        print("] ...")

        search_text = "site:imdb.com " + full_title
        results = search(search_text)

        # Store each unique results.
        for result in results:
            matched = re.search(imdb_id_pattern, result)

            if not matched:
                continue

            id = matched.group(1)

            if id not in imdb_ids:
                imdb_ids.append(id)

            break

    print('\n')


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
