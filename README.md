# Orgfiles - File Organizer CLI Tool

Orgfiles is a command-line tool designed to help organize files within a directory based on their extensions, keywords, perform deletions, and bulk renaming.

## Features

- **Organize by Extension:** Sorts files into folders based on their file extensions.
- **Organize by Keywords:** Moves files containing specified keywords into respective folders.
- **Delete by Keys/Extensions:** Removes files containing specific keys or with a specified extension.
- **Bulk Renaming:** Renames files in a directory using a provided pattern.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/orgfiles.git
    cd orgfiles
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Commands:

- **Organize by Extension:**
    ```bash
    python orgfiles.py organize_by_extension /path/to/directory
    ```

- **Organize by Keywords:**
    ```bash
    python orgfiles.py organize_by_keywords /path/to/directory keyword1,keyword2,keyword3
    ```

- **Delete by Keys:**
    ```bash
    python orgfiles.py delete_by_keys /path/to/directory key1,key2,key3
    ```

- **Delete by Extension:**
    ```bash
    python orgfiles.py delete_by_extension /path/to/directory .ext
    ```

- **Bulk Rename:**
    ```bash
    python orgfiles.py bulk_rename /path/to/directory pattern
    ```

Replace `/path/to/directory` with the target directory and adjust the parameters accordingly.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes or open an issue for any new features or bug fixes.
