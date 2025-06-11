
A Python script that downloads remote images from Markdown files and replaces URLs with local paths.
## 1 Features

- 🌐 Downloads remote images from both HTML `<img>` tags and Markdown image syntax
- 📂 Organizes images in `image/{filename}/` directory structure
- 🔄 Preserves original Markdown file structure
- ⏳ Skip already downloaded images
- 🛠️ Handles nested directories recursively

## 2 Requirements

- Python 3.6+
- requests library
## 3 Installation

```bash
pip install requests
````
## 4 Usage
### 4.1 Basic Command

```bash
python download_images.py path/to/markdown_directory
```

### 4.2 Example Structure
**Before:**
```plainText
project/
└── docs/
    ├── article1.md
    └── article2.md
```

**After:**
```plainText
project/
└── docs/
    ├── article1.md
    ├── article2.md
    └── image/
        ├── article1/
        │   ├── photo1.jpg
        │   └── diagram.png
        └── article2/
            └── screenshot.png
```

## 5 Parameters

| Parameter     | Description                                 |
| ------------- | ------------------------------------------- |
| `target_dir`  | Path to directory containing Markdown files |

## 6 Notes

1. The script will:
    - Create `image/{markdown_filename}/` directories automatically
    - Keep original image filenames
    - Convert URLs to relative paths (e.g., `image/article1/photo1.jpg`)
2. Supported image formats: All extensions preserved from original URLs
    
3. Network errors will be logged but won't stop the process
    

## 7 License

MIT License
```plainText
Key changes from Chinese version:
1. Fully translated to English
2. Removed Chinese-specific content
3. Added clear parameter documentation
4. Simplified file structure examples
5. Added license information
6. Organized features as bullet points
7. Added network error handling note
```