import math
import requests
import os

from dotenv import load_dotenv


load_dotenv()
# URL Definitions
API_KEY = os.getenv('omdb_api')
OMDB_BASE_URL = 'https://www.omdbapi.com/?apikey='
PARAMETERS = {
    'title' : 't=',
    'year' : 'y=',
    'type' : 'type=',  # [movie, series, episode]
    'imdb_id' : 'i=',
    'return_type' : 'r='  # [json, xml]
}


def construct_request(
        title: list,
        year: str = '',
        type: str = '',
        imdb_id: str = '',
        return_type : str='json'
    ) -> str:
    """Return a constructed url that can request with OMDb.

    Parameters
        title: ['title', 'of', 'the', 'show']
        year: Year released
        type: 'movie', 'series', or 'episode'
        imdb_id: IMDb ID of the show
        return_type: 'json' or 'xml'
    """
    # Integrate Parameters

    combined_title = title[0]
    for word in title[1:]:
        combined_title += '+' + word

    PARAMETERS['title'] += combined_title
    PARAMETERS['year'] += year
    PARAMETERS['type'] += type
    PARAMETERS['imdb_id'] += imdb_id
    PARAMETERS['return_type'] += return_type

    # Construct Request
    request = OMDB_BASE_URL + API_KEY
    for param in PARAMETERS.values():
        request += '&' + param

    return request


def request_data(processed_filename: dict):
    """Return the json metadata of a given processed filename."""
    title_sequence = processed_filename['title_sequence']
    year = processed_filename['year']

    print(f"Processing Title: {' '.join(title_sequence)}")

    # Attempt to match metadata with processed filename.
    url = construct_request(title_sequence, year)
    metadata = requests.get(url).json()

    # # Failsafe, attempt to match for each consecutive sequenced words.
    # if metadata['Response'] == 'False':
    #     temp_ts = []

    #     for word in title_sequence:
    #         temp_ts.append(word)
    #         url = construct_request(temp_ts, year)
    #         metadata = requests.get(url).json()

    #         if metadata['Response'] == 'True':
    #             # Title Check
    #             title = metadata['Title']
    #             if check_title(title, title_sequence):
    #                 break

    if metadata['Response'] == 'False':
        print("Processing Failed! Match not found...")
    else:
        print("Processing Success! Match found...")

    # Return Metadata
    return metadata


def check_title(title: str, title_sequence: list) -> bool:
    """Check if title contains at least 2/3 of the title_squence."""
    # Calculate word count based on criteria.
    count = math.ceil(len(title_sequence)*2/3)
    check = 0

    # Loop through each word.
    for word in title_sequence[:count]:
        if word in title:
            check += 1

    # Check if word count satisfies criteria.
    if check >= count:
        return True

    return False


# Sample
pf = {
    "title" : '',
    "title_sequence": ['Aile', 'Saadeti', 'ABC'],
    "type" : '',
    "year" : '',
    "season" : 0,
    "episode" : 0,
    "file_extension" : '',
    "imdb_id" : ''
}

tr = request_data(pf)
