import os
from datetime import datetime


def upload_image_to(instance, filename):
    # Get the file extension
    name, ext = os.path.splitext(filename)
    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Create the filename with the timestamp
    new_filename = f"{name}_{timestamp}_{ext}"
    # Return the path relative to MEDIA_ROOT
    return os.path.join("images", new_filename)


def extract_timestamp(url: str):
    return url.split("_")[-2]
