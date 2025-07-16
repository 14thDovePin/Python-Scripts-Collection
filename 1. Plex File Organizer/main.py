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
import os
import re

from colorama import Fore
from googlesearch import search

from file_manager import prompt_media_info
from process_data import (
    process_directory_data,
    process_filenames_data,
    unify_title_sequences
)
from utils.colors import Colors
from utils.templates import GenerateTemplate


TEST_MODE = False


def main():
    # Prompt the user for the information of the media to be used.
    media_directory, directory_name, filenames = prompt_media_info()

    # Process media data.
    directory_data = process_directory_data(media_directory, directory_name)
    files_data = process_filenames_data(media_directory, filenames)

    # Unify Title Sequences
    title_sequences = unify_title_sequences(directory_data, files_data)

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

    # Parse ID Through OMDb
    imdb_results = []
    # Check if Movie or Series
    # If Movie, Construct Final Filename
    # If Seiries, Test if Beautifulsoup Can Extract Episode Names

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
