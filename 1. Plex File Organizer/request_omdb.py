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
    """Return a constructed url that can request with OMDb."""
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
