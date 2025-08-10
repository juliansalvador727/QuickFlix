from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


existing_file_names = [
    "DSCN0003.JPG",
    "DSCN0019.JPG",
    "DSCN0237.JPG"
]


FOLDER = Path("images")

image_paths = list({file for ext in ('*.jpg', '*.JPG') for file in FOLDER.glob(ext)})

new_file_names = []

def unique_path(FOLDER, base_name, suffix):
    new_name = f"{base_name}{suffix}"
    candidate = FOLDER / new_name
    count = 1
    while candidate.exists():
        candidate = FOLDER / f"{base_name}_{count}{suffix}"
        count += 1
    return candidate

for img_path in image_paths:
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

for file, base_name in zip(image_paths, final_names):
    new_name = f"{base_name}{file.suffix}"
    new_path = file.parent / new_name
    print(f"Renaming {file.name} to {new_name}")
    file.rename(new_path)