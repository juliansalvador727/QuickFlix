# main.py
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

FOLDER = Path("images")
IMAGE_PATHS = list({file for ext in ('*.jpg', '*.JPG') for file in FOLDER.glob(ext)})

new_file_names = []
for img_path in IMAGE_PATHS:
    with Image.open(img_path) as image:
        exif_data = image._getexif()
        date_taken = None
        
        if exif_data:
            for tag_id, value in exif_data.items():
                if tag_id == 36867:  # DateTimeOriginal tag
                    dt = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                    date_taken = dt.strftime("%d%b%Y")
                    break
        
        if date_taken:
            new_file_names.append(date_taken)
        else:
            new_file_names.append("unknown_date")

name_counts = {}
final_names = []
for date_str in new_file_names:
    count = name_counts.get(date_str, 0)
    if count == 0:
        final_name = date_str
    else:
        final_name = f"{date_str}_{count}"
    name_counts[date_str] = count + 1
    final_names.append(final_name)

for file, base_name in zip(IMAGE_PATHS, final_names):
    new_name = f"{base_name}{file.suffix}"
    new_path = file.parent / new_name
    print(f"Renaming {file.name} to {new_name}")
    file.rename(new_path)