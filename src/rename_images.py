from pathlib import Path
from image_utils import get_date_taken
from name_utils import make_unique_names

FOLDER = Path("images")

def collect_image_paths(folder):
    return list({file for ext in ('*.jpg', '*.JPG') for file in folder.glob(ext)})

def generate_new_names(image_paths):
    base_names = []
    for path in image_paths:
        date_taken = get_date_taken(path)
        base_names.append(date_taken if date_taken else "unknown_date")
    return make_unique_names(base_names)

def rename_files(image_paths, final_names):
    for file, base_name in zip(image_paths, final_names):
        new_name = f"{base_name}{file.suffix}"
        new_path = file.parent / new_name
        print(f"Renaming {file.name} to {new_name}")
        file.rename(new_path)

def main():
    image_paths = collect_image_paths(FOLDER)
    new_names = generate_new_names(image_paths)
    rename_files(image_paths, new_names)

if __name__ == "__main__":
    main()
