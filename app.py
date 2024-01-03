import typer
import os
import shutil

app = typer.Typer()

@app.command()
def organize_by_extension(directory: str):
    """
    Organize files in a directory based on their extensions.
    """
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                extension = filename.split(".")[-1]
                extension_folder = os.path.join(directory, extension)

                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(extension_folder, filename),
                )

        typer.echo(f"Files organized by extension in {directory}.")
    except Exception as e:
        typer.echo(f"Error organizing files: {e}", err=True)

@app.command()
def organize_by_keywords(directory: str, keywords: str):
    """
    Organize files in a directory based on provided keywords.
    """
    try:
        keyword_list = keywords.split(',')
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                for keyword in keyword_list:
                    if keyword.lower() in filename.lower():
                        keyword_folder = os.path.join(directory, keyword)

                        if not os.path.exists(keyword_folder):
                            os.makedirs(keyword_folder)

                        shutil.move(
                            os.path.join(directory, filename),
                            os.path.join(keyword_folder, filename),
                        )
                        break

        typer.echo(f"Files organized by keywords in {directory} using {keywords}.")
    except Exception as e:
        typer.echo(f"Error organizing files: {e}", err=True)

@app.command()
def delete_by_keys(directory: str, keys: str):
    """
    Delete files in a directory based on provided keys.
    """
    try:
        key_list = keys.split(',')
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                for key in key_list:
                    if key.lower() in filename.lower():
                        os.remove(os.path.join(directory, filename))
                        break

        typer.echo(f"Files deleted in {directory} using keys: {keys}.")
    except Exception as e:
        typer.echo(f"Error deleting files: {e}", err=True)

@app.command()
def delete_by_extension(directory: str, extension: str):
    """
    Delete files in a directory with a specified extension.
    """
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                if filename.lower().endswith(extension.lower()):
                    os.remove(os.path.join(directory, filename))

        typer.echo(f"Files deleted in {directory} with extension: {extension}.")
    except Exception as e:
        typer.echo(f"Error deleting files: {e}", err=True)

@app.command()
def bulk_rename(directory: str, pattern: str):
    """
    Bulk rename files in a directory based on a provided pattern.
    """
    try:
        for index, filename in enumerate(os.listdir(directory)):
            if os.path.isfile(os.path.join(directory, filename)):
                extension = filename.split(".")[-1]
                new_filename = f"{pattern}{index}.{extension}"
                os.rename(
                    os.path.join(directory, filename),
                    os.path.join(directory, new_filename),
                )

        typer.echo(f"Files in {directory} renamed with pattern: {pattern}.")
    except Exception as e:
        typer.echo(f"Error renaming files: {e}", err=True)

def main():
    app()

if __name__ == "__main__":
    typer.run(main)
