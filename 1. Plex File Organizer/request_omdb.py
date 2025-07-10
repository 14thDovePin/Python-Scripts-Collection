import math
import requests
import os

from dotenv import load_dotenv


load_dotenv()
# URL Definitions
API_KEY = os.getenv('omdb_api')
OMDB_BASE_URL = 'https://www.omdbapi.com/?apikey='


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
    PARAMETERS = {
        'title' : 't=',
        'year' : 'y=',
        'type' : 'type=',  # [movie, series, episode]
        'imdb_id' : 'i=',
        'return_type' : 'r='  # [json, xml]
    }

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


def request_metadata(processed_filename: dict):
    """Return the json metadata of a given processed filename."""
    title_sequence = processed_filename['title_sequence']
    year = processed_filename['year']

    if not title_sequence:
        return

    print(f"Processing Title: {' '.join(title_sequence)}")

    # Attempt to match metadata with processed filename.
    url = construct_request(title_sequence, year)
    metadata = requests.get(url).json()

    if metadata['Response'] == 'False':
        print("Processing Failed! Match not found...")
    else:
        print("Processing Success! Match found...")

    # Return Metadata
    return metadata
