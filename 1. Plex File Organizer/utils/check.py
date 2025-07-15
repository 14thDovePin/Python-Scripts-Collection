from utils.data_sets import video_extensions, video_qualities


VE = video_extensions()
VQ = video_qualities()


def check_video(filename: str) -> bool:
    """Check if filename is a video by its extension."""
    for ext in VE:
        if ext in filename:
            return True

    return False
