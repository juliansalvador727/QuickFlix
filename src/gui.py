from tkinter import *
from tkinter import filedialog, messagebox
from pathlib import Path

from image_utils import get_date_taken
from name_utils import make_unique_names


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
        file.rename(new_path)
    return len(image_paths)

def run_gui():
    root = Tk()
    root.title("Image Renamer")

    label = Label(root, text="Select a folder to rename")
    label.pack(pady=10)

    images = []

    def choose_folder():
        folder_selected = filedialog.askdirectory()
        if not folder_selected:
            return
        folder_path = Path(folder_selected)

        images = collect_image_paths(folder_path)
        if not images:
            messagebox.showinfo("No Images", "No JPG images found in that folder.")
            return

        

    def change_filename():
        new_names = generate_new_names(images)
        count = rename_files(images, new_names)
        messagebox.showinfo("Success", f"Renamed {count} images.")


    btn_choose_folder = Button(root, text="Choose Folder", command=choose_folder)
    btn_change_filename = Button(root, text="Rename Files", command=change_filename)
    btn_choose_folder.pack(pady=20)
    btn_change_filename.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
