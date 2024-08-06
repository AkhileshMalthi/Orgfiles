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
    git clone https://github.com/AkhileshMalthi/Orgfiles.git
    cd Orgfiles
    ```

2. **Build the package and Get the Distribution**

    ```bash
    pip setup.py sdist bdist_wheel
    ```
3. **Install the Application**

    ```bash
    pip install .
    ```

## Usage

### Commands

- `organize`: Sort files within a directory by extension or keyword.

    ```bash
    orgfiles organize /path/to/directory --by extension
    orgfiles organize /path/to/directory --by keyword
    ```

- `delete`: Remove files within a directory based on keywords or extensions.

    ```bash
    orgfiles delete /path/to/directory --by extension
    orgfiles delete /path/to/directory --by key
    ```

- `undo`: Undo the last file movement action (organization or deletion).

    ```bash
    orgfiles undo
    ```

- `bulk_rename`: Rename files within a directory using a specified pattern.

    ```bash
    orgfiles bulk_rename /path/to/directory pattern
    ```

## Contributions

Contributions and feedback are appreciated! Feel free to open issues for suggestions or bug reports. Pull requests for enhancements or new features are welcome.

## License

This project is licensed under the [MIT License](LICENSE).
