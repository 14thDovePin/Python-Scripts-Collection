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

import os


# Format Console
os.system("title Plex File Organizer && color a")


def main():
    os.system("cls")

    # Prompt user for the movie/series directory & its type.
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
    file_names = []
    for _, _, files in os.walk(media_directory):
        file_names = files
        break

    # Cleanup Filename/s
    # Divide Letters by Spaces & Periods


    # Extract title metadata from OMDb
    if media_type == "1":
        pass

    # Extract series title from IMDb
    elif media_type == "2":
        pass


if __name__ == "__main__":
    while True:
        main()
