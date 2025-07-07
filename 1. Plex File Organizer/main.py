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
# Video Extensions
VE = ['webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 'gifv', 'mng', 'mov',
      'avi', 'qt', 'wmv', 'yuv', 'rm', 'asf', 'amv', 'mp4', 'm4p', 'm4v',
      'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'm4v', 'svi', '3gp', '3g2', 'mxf',
      'roq', 'nsv', 'flv', 'f4v', 'f4p', 'f4a', 'f4b', 'mod']
# Vide Qualities
VQ  = ['240p', '360p', '480p', '720p', '1080p', '1440p', '2160p', '4320p']


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

    # Extract metadata from OMDb with current title.
    # If it fails, prompt user to manually input title & year
    # to match & extract metadata from.

    for i in clean_filenames: print(' '.join(i))
    input("Press Any Key To Exit")

    # Extract title metadata from OMDb
    if media_type == "1":
        pass

    # Extract series title from IMDb
    elif media_type == "2":
        pass

    # Prompt user it title, year, and type is correct.


def clean_filename(filename: str) -> str:
    """Return a clean filename."""
    # Pull all word sequences.
    word_pattern = r'[^. \s]+'
    results = re.findall(word_pattern, filename)

    # Preserve File Extension
    for word in results:
        if word in VE:
            file_extension = '.' + word

    # Cut list from start to before file extension.
    for extension in VE:
        for word in results[:]:
            if extension == word:
                extension_index = results.index(word)
                results = results[:extension_index]
                break

    # For Movies ---
    # Cut list from start to the last date detected.
    date_pattern = r'19\d\d|20\d\d'
    results.reverse()
    date = None

    for item in results:
        if re.search(date_pattern, item):
            date = item
            break

    results.reverse()

    if date:
        date_index = results.index(date)
        results = results[:date_index+1]
    else:
        results = results

    # For Series ---
    # Cut list from start to season/episode number.
    pattern_se = r'SEASON[\s.]?\d+|EPISODE[\s.]?\d+|S\d+|EP?\d+'
    for word in results[:]:
        results_se = re.findall(pattern_se, word, re.IGNORECASE)
        if results_se:
            se_index = results.index(word)
            results = results[:se_index]
            results += results_se
            break

    # Special Exceptions ---
    # Cut from video quality to the end
    for word in results[:]:
        if word in VQ:
            vq_index = results.index(word)
            results = results[:vq_index]
            break

    # Add file extension.
    # results[-1] = results[-1] + file_extension
    results.append(file_extension)

    # Return cleaned filename
    return results


if __name__ == "__main__":
    while True:
        main()
