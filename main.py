from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


existing_file_names = [
    "DSCN0003.JPG",
    "DSCN0019.JPG",
    "DSCN0237.JPG"
]


folder = Path("images")

image_paths = list({file for ext in ('*.jpg', '*.JPG') for file in folder.glob(ext)})

new_file_names = []

def unique_path(folder, base_name, suffix):
    new_name = f"{base_name}{suffix}"
    candidate = folder / new_name
    count = 1
    while candidate.exists():
        candidate = folder / f"{base_name}_{count}{suffix}"
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


for i, file in enumerate(image_paths, start=1):
    base_name = new_file_names[i-1]
    suffix = file.suffix
    new_path = unique_path(file.parent, base_name, suffix)
    print(f"Renaming {file.name} to {new_path.name}, {i}")
    file.rename(new_path)