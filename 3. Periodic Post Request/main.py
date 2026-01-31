""" January 30, 202
What is this script about?
A simple script that loops a get request with a given url inside `url.txt`.
This script is also designed to be paired with NSSM to run as a Windows service.

How does it work?
1. Construct the path to grab the `url.txt`.
1. Load the URL written inside `url.txt`.
2. Loops forever every given `interval` to execute a post request.

External Libraries Used:
  requests

Developer Notes
This is literally just it. A super dooper simple script.
"""


from time import sleep
from requests import post


def main(interval=60):
    # Construct file directory.
    directory = __file__.split('\\')
    directory = '\\'.join(directory[:-1])
    file = directory + '\\url.txt'

    # Import URL.
    with open(file, 'r') as f:
        URL = f.readlines()[0]

    # Start uptime push request loop.
    while True:
        try:
            post(URL)
        except:
            print(f"POST failed. Retrying in {interval} seconds.")
        sleep(interval)


if __name__ == "__main__":
    main(50)
