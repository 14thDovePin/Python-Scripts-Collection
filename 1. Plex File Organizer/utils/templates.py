class GenerateTemplate():
    """A class for generating templates."""

    def metadata_old(self) -> dict:
        """Generate a metadata dictionary.

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

        return metadata

    def metadata(self) -> dict:
        """Generate a metadata dictionary.

        Returns
        -------
        metadata : dict
            Dictionary Keys:
            - **title** : str
            - **type** : str
                Set to either "movie" or "series".
            - **year** : str
            - **season** : str
            - **episode** : str
            - **imdb_id** : str
        """

        return {
            "title" : "",
            "type" : "",
            "year" : "",
            "season" : "",
            "episode" : "",
            "imdb_id" : ""
        }

    def file_info(self) -> dict:
        """Generate a file information dictionary.

        Returns
        -------
        file_info : dict
            Dictionary Keys:
            - **filename** : str
            - **new_filename** : str
            - **extension** : str
            - **path** : str
        """

        return {
            "filename" : "",
            "new_filename" : "",
            "extension" : "",
            "path" : "",
        }
