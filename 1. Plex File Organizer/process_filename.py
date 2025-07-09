import re

from data_sets import video_extensions, video_qualities


VE = video_extensions()
VQ = video_qualities()


def print_pf(processed_filename: dict) -> None:
    # Verbosely print on terminal the processed filename.
    pf = processed_filename

    print(f'\nTitle ----------> {pf['title']}')
    print(f'Title Sequence--> {pf['rough_title']}')
    print(f'Type -----------> {pf['type']}')
    print(f'Year -----------> {pf['year']}')
    print(f'Season # -------> {pf['season']}')
    print(f'Episode # ------> {pf['episode']}')
    print(f'File Type ------> {pf['file_extension']}')
    print(f'IMDb ID --------> {pf['imdb_id']}')


def process_filename(filename: str) -> dict:
    """Return a processed dictionary of the filename.

    Dictionary Keys
        title (str)
        title_sequence (list)
        type (str) - Either "Movie" or "TV Show"
        year (int)
        season (int)
        episode (int)
        file_extension (int)
        imdb_id (str)
    """
    # Processed Filename
    pf = {
        "title" : '',
        "title_sequence": [],
        "type" : '',
        "year" : 0,
        "season" : 0,
        "episode" : 0,
        "file_extension" : '',
        "imdb_id" : ''
    }

    ignore_case = re.IGNORECASE

    # Extract Year
    year_pattern = r'19\d\d|20\d\d'
    year = re.search(year_pattern, filename)

    if year:
        year = year.group(0)
        pf['year'] = int(year)

    number_pattern = r'\d+'

    # Extract Season Number
    season_pattern = r'SEASON[\s.]?\d+|S\d+'
    season = re.search(season_pattern, filename, ignore_case)
    if season:
        season = season.group(0)
        number = re.search(number_pattern, season)
        pf['season'] = int(number.group(0))

    # Extract Episode Number
    episode_pattern = r'EPISODE[\s.]?\d+|EP?\d+'
    episode = re.search(episode_pattern, filename, ignore_case)

    if episode:
        episode = episode.group(0)
        number = re.search(number_pattern, episode)
        pf['episode'] = int(number.group(0))

    # Extract File Extension
    for extension in VE:
        if extension in filename:
            pf['file_extension'] = extension

    # Determine File Type
    if pf['season'] and pf['episode']:
        pf['type'] = 'TV Show'
    elif pf['year']:
        pf['type'] = 'Movie'

    # Special Case/s

    # Remove anything enclosed in () or [], But if it
    # contains the Year, then replace it with it.
    pattern = r'[\s.]?\([^\)]+\)|[\s.]?\[[^\]]+\]'
    parenthesized_words = re.findall(pattern, filename)

    for matched_word in parenthesized_words:
        year = re.search(year_pattern, matched_word)

        if year:
            s_char = matched_word[0]  # Starting Character
            starting_char = s_char if s_char != '(' else ''
            year_final = starting_char + year.group(0)
            filename = filename.replace(matched_word, year_final)
        else:
            filename = filename.replace(matched_word, '')

    # Process Title

    # Pull Word Sequence
    word_pattern = r'[^. \s]+'
    word_sequence = re.findall(word_pattern, filename)

    # Cut List
    indexes = []
    for word in word_sequence:
        store_index = False

        # File Extension
        if word in VE:
            store_index = True

        # Year
        if re.search(year_pattern, word):
            store_index = True

        # Video Quality
        if word in VQ:
            store_index = True

        # Season/Episode #
        s_check = re.search(season_pattern, word)
        e_check = re.search(episode_pattern, word)

        if s_check and e_check:
            store_index = True

        # Store Index
        if store_index:
            indexes.append(word_sequence.index(word))

    final_index = min(indexes)
    word_sequence = word_sequence[:final_index]

    # Save the rough title & return the processed filename
    pf['rough_title'] = word_sequence
    return pf
