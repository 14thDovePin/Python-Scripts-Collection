def generate_metadata() -> dict:
    """Return a template dict of a title"s metadata.

    Returns
    -------
    metadata : dict
        Dictionary Keys:
        - **title** : str
        - **title_sequence** : list
          An ordered list of string composed from the title.
        - **type** : str
          Set to either "movie" or "series".
        - **year** : str
        - **season** : str
        - **episode** : str
        - **file_extension** : str
        - **imdb_id** : str
    """
    metadata = {
        "title" : "",
        "title_sequence": [],
        "type" : "",
        "year" : "",
        "season" : "",
        "episode" : "",
        "file_extension" : "",
        "imdb_id" : ""
    }

    file_information = {
        "filename" : "",
        "new_filename" : "",
        "extension" : "",
        "path" : "",
        "new_path" : "",
    }

    return metadata
