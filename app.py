import typer
import os
import shutil

app = typer.Typer()

@app.command()
def organize(directory: str, by: str = typer.Option(..., help="Organize by 'extension' or 'keyword'")):
    """
    Organize files in a directory based on provided option (extension or keyword).
    """
    try:
        if by == 'extension':
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
        elif by == 'keyword':
            keywords = typer.prompt("Enter keywords (comma-separated):")
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
        else:
            raise typer.BadParameter("Invalid option. Use 'extension' or 'keyword'.")

    except Exception as e:
        typer.echo(f"Error organizing files: {e}", err=True)

@app.command()
def delete(directory: str, by: str = typer.Option(..., help="Delete by 'key' or 'extension'")):
    """
    Delete files in a directory based on provided option (key or extension).
    """
    try:
        if by == 'extension':
            extension = typer.prompt("Enter extension:")
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    if filename.lower().endswith(extension.lower()):
                        os.remove(os.path.join(directory, filename))

            typer.echo(f"Files deleted in {directory} with extension: {extension}.")
        elif by == 'key':
            keys = typer.prompt("Enter keys (comma-separated):")
            key_list = keys.split(',')
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    for key in key_list:
                        if key.lower() in filename.lower():
                            os.remove(os.path.join(directory, filename))
                            break

            typer.echo(f"Files deleted in {directory} using keys: {keys}.")
        else:
            raise typer.BadParameter("Invalid option. Use 'key' or 'extension'.")

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
