import re

from data_sets import video_extensions, video_qualities


VE = video_extensions()
VQ = video_qualities()


def print_pf(processed_filename: dict) -> None:
    # Verbosely print on terminal the processed filename.
    pf = processed_filename

    print(f'\nTitle -----> {pf['title']}')
    print(f'Type ------> {pf['type']}')
    print(f'Year ------> {pf['year']}')
    print(f'Season # --> {pf['season']}')
    print(f'Episode # -> {pf['episode']}')
    print(f'File Type -> {pf['file_extension']}')
    print(f'IMDb ID ---> {pf['imdb_id']}')


def process_filename(filename: str) -> dict:
    """Return a processed dictionary of the filename.

    Dictionary Keys
        title (str)
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
        "type" : '',
        "year" : None,
        "season" : None,
        "episode" : None,
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
    if not pf['season'] and not pf['episode']:
        pf['type'] = 'TV Show'
    else:
        pf['type'] = 'Movie'



    # Pull all word sequences.
    word_pattern = r'[^. \s]+'
    results = re.findall(word_pattern, filename)

    # Preserve file extension.
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
