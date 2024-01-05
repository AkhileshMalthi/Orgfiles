# Orgfiles CLI Application

Orgfiles is a versatile command-line tool for organizing, managing, and tidying up your files effortlessly.

## Features

- **Smart Organization:** Arrange files by extension or keywords for efficient file management.
- **Selective Deletion:** Delete files based on specific keywords or file extensions with precision.
- **Bulk File Renaming:** Rename multiple files in a directory according to a provided pattern.
- **Undo Capability:** Reverse previous file movements, providing a safety net for accidental actions.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your_username/orgfiles.git
    cd orgfiles
    ```

2. **Install Dependencies:**

    - typer

    ```bash
    pip install typer
    ```

## Usage

### Commands

- `organize`: Sort files within a directory by extension or keyword.

    ```bash
    python orgfiles.py organize /path/to/directory --by extension
    python orgfiles.py organize /path/to/directory --by keyword
    ```

- `delete`: Remove files within a directory based on keywords or extensions.

    ```bash
    python orgfiles.py delete /path/to/directory --by extension
    python orgfiles.py delete /path/to/directory --by key
    ```

- `undo`: Undo the last file movement action (organization or deletion).

    ```bash
    python orgfiles.py undo
    ```

- `bulk_rename`: Rename files within a directory using a specified pattern.

    ```bash
    python orgfiles.py bulk_rename /path/to/directory pattern
    ```

## Contributions

Contributions and feedback are appreciated! Feel free to open issues for suggestions or bug reports. Pull requests for enhancements or new features are welcome.

## License

This project is licensed under the [MIT License](LICENSE).
