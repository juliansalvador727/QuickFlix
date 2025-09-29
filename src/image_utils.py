from PIL import Image
from datetime import datetime

DATE_ID = 36867

def get_date_taken(img_path):
    """Return the formatted date string (e.g., 01Jan2023) or None if missing."""
    with Image.open(img_path) as image:
        exif_data = image._getexif()
        if not exif_data:
            return None
        value = exif_data.get(DATE_ID)
        if value:
            dt = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
            return dt.strftime("%d%b%Y")
    return None