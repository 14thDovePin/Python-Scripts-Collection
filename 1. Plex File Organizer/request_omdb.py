import math
import requests
import os

from colorama import Fore, Back, Style
from dotenv import load_dotenv

from utils.colors import Colors


load_dotenv()
C = Colors()
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


def request_metadata(title_sequence: list, year: str=''):
    """Return the json metadata of a given title seqeunce.

    Parameters
    ----------
    title_sequence : list
        A sequenced list of string composing the rough title to search for.
    year : str
        The year of the title if there's any.
    """

    if not title_sequence:
        return

    # Attempt to match metadata with processed filename.
    url = construct_request(title_sequence, year)
    metadata = requests.get(url).json()

    title = ' '.join(title_sequence)

    if metadata['Response'] == 'False':
        C.print_error("Failed Processing ", end='')
        print(f"---- [{title}]")
    else:
        C.print_success("Succeeded Processing ", end='')
        print(f"- [{title}]")

    # Return Metadata
    return metadata
