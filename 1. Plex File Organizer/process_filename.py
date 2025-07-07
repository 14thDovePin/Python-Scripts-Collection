import re

from data_sets import video_extensions, video_qualities


VE = video_extensions()
VQ = video_qualities()


def clean_filename(filename: str) -> str:
    """Return a clean filename."""
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
