import os
from pathlib import Path

existing_file_names = [
    "DSCN0003.JPG",
    "DSCN0019.JPG",
    "DSCN0237.JPG"
]


# use path class, select the appropriate folder
folder = Path("images")

# .glob method to find pathnames matching specified pattern (.jpg)
files = list(folder.glob("*.jpg"))

# print(files)
# files becomes a list of files with [WindowsPath('images/YOUR_IMAGE_HERE.jpg'), WindowsPath('images/YOUR_IMAGE_HERE2.jpg'), etc...]

file_count = len(files)

print(f"there are {file_count} pictures in this folder.")

# rename files
for i, file in enumerate(files, start=1):
    new_name = f"foo{i}{file.suffix}"
    new_path = file.parent / new_name
    print(f"Renaming {file.name} to {new_name}")
    file.rename(new_path)