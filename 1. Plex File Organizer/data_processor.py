from file_manager import process_filename, check_video
from utils.templates import GenerateTemplate as GT


def process_directory_data(media_directory: str,
                           directory_name: list,
                           gt: GT=GT()) -> dict:
    """Return a dict of processed information given media information.

    Parameters
    ----------
    media_directory : str
        Directory of the media to work on.
    directory_name : list
        Name of the directory of the media to work on.
    gt : GenerateTemplate
        For generating the templates needed to construct the dict.

    Returns
    -------
    directory_data : dict
        Contains the processed information of the given media.
    """
    # Process Directory Data
    directory_data = gt.media_data()
    dir_metadata = gt.metadata()
    dir_info = gt.file_info()

    title_sequence = process_filename(directory_name, dir_metadata, dir_info)
    dir_info['path'] = media_directory

    # Store Directory Data
    directory_data['title_sequence'] = title_sequence
    directory_data['metadata'] = dir_metadata
    directory_data['file_information'] = dir_info

    return directory_data


def process_filenames_data(media_directory: str,
                           filenames: str,
                           gt: GT=GT()) -> list:
    """Return a dict of processed information given a list of filenames.

    Parameters
    ----------
    media_directory : str
        Directory of the media working on.
    filenames : list
        The list of directories to work on.
    gt : GenerateTemplate
        For generating the templates needed to construct the dict.

    Returns
    -------
    directory_data : dict
        Contains the processed information of the given media.
    """
    files_data = []

    # Process Files Data
    for file in filenames:
        # Allow only video files.
        if not check_video(file):
            continue

        file_metadata = gt.metadata()
        file_info = gt.file_info()

        title_sequence = process_filename(file, file_metadata, file_info)
        file_info['path'] = media_directory

        # Store & Append Information
        file_data = gt.media_data()
        file_data['title_sequence'] = title_sequence
        file_data['metadata'] = file_metadata
        file_data['file_information'] = file_info
        files_data.append(file_data)

    return files_data


def unify_title_sequences(directory_data: dict, files_data: dict) -> list:
    """Return the list of titles sequence given both directory and file data.

    Parameters
    ----------
    directory_data : dict
        The directory data of the media being worked on.
    files_data : dict
        The files data of the media being worked on.

    Returns
    -------
    titles_sequence : list
        A list of title sequences.
    """
    titles_sequence = []
    titles_sequence.append(directory_data['title_sequence'])

    for file_data in files_data:
        ts = file_data['title_sequence']
        if ts not in titles_sequence:
            titles_sequence.append(ts)

    return titles_sequence
