# 📸 QuickFlix

A simple Python utility that renames JPEG images based on their **EXIF metadata** (date taken).  
If no EXIF date is found, the file is renamed with `unknown_date`.  
Duplicate dates are handled automatically by appending suffixes like `_1`, `_2`, etc.

---

## ✨ Features

- Extracts the **Date Taken** field (`DateTimeOriginal`) from EXIF metadata.
- Renames files into human-readable format like `12Aug2023.jpg`.
- Handles duplicates with numbered suffixes.
- Falls back to `unknown_date` if no EXIF data is available.
- Works on `.jpg` and `.JPG` files.

---

## 🚀 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/QuickFlix.git
cd photo-renamer
pip install -r requirements.txt
```

---

## 🖼️ Usage

Place your photos in the `images/` folder (or specify another directory).

Run the script:

```bash
python src/rename_images.py --input ./images
```

Example output:

```
Renaming IMG_0012.JPG to 12Aug2023.jpg
Renaming IMG_0013.JPG to 12Aug2023_1.jpg
Renaming IMG_0014.JPG to unknown_date.jpg
```

---

## 📂 Project Structure

```
photo-renamer/
├── src/
│   └── rename_images.py      # main script
├── tests/                    # optional unit tests
├── sample_images/            # small example JPGs
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Requirements

- Python 3.9+
- [Pillow](https://pypi.org/project/Pillow/)

Install with:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
