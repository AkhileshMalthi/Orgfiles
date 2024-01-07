from rich import print as rprint
import typer
import os
import shutil
import json

app = typer.Typer()
MOVEMENTS_FILE = "file_movements.json"

def save_movements(movements):
    with open(MOVEMENTS_FILE, "w") as file:
        json.dump(movements, file, indent=4)

def load_movements():
    movements = {}
    if os.path.exists(MOVEMENTS_FILE):
        with open(MOVEMENTS_FILE, "r") as file:
            movements = json.load(file)
    return movements

@app.command()
def organize(directory: str = typer.Argument(..., help="The directory path where the operation will take place."),
    by: str = typer.Option(..., help="Choose how to organize the files: 'extension' or 'keyword'.")):
    """
    Organize files in a directory based on provided option (extension or keyword).
    """
    movements = load_movements()
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

                    movements[filename] = {
                        "from": directory,
                        "to": extension_folder
                    }
            save_movements(movements)
            rprint(f"Files [green]organized[/green] by extension in [blue]{directory}[/blue].")
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
                            movements[filename] = {
                                "from": directory,
                                "to": keyword_folder
                            }
                            break

            save_movements(movements)
            rprint(f"Files [green]organized[/green] by keywords in [blue]{directory}[/blue] using [blue]{keywords}[/blue].")
        else:
            raise typer.BadParameter("Invalid option. Use 'extension' or 'keyword'.")

    except Exception as e:
        rprint(f"[bold red]Error organizing files:[/bold red] {e}")

@app.command()
def delete(directory: str, by: str = typer.Option(..., help="Delete by 'key' or 'extension'")):
    """
    Delete files in a directory based on provided option (key or extension).
    """
    movements = load_movements()
    try:
        if by == 'extension':
            extension = typer.prompt("Enter extension:")
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    if filename.lower().endswith(extension.lower()):
                        os.remove(os.path.join(directory, filename))
                        movements[filename] = {
                            "from": directory,
                            "to": "deleted"
                        }

            save_movements(movements)
            rprint(f"Files [green]deleted[/green] in [blue]{directory}[/blue] with extension(s): [blue]{extension}[/blue].")
        elif by == 'key':
            keys = typer.prompt("Enter keys (comma-separated):")
            key_list = keys.split(',')

            # Display files to be deleted
            files_to_delete = []
            for filename in os.listdir(directory):
                if os.path.isfile(os.path.join(directory, filename)):
                    for key in key_list:
                        if key.lower() in filename.lower():
                            files_to_delete.append(filename)
                            movements[filename] = {
                                "from": directory,
                                "to": "deleted"
                            }
                            break

            if not files_to_delete:
                rprint("[bold yellow]No files found to delete.[/bold yellow]")
                return

            # Confirmation prompt
            confirm = typer.confirm(
                f"[bold yellow]Are you sure you want to delete these files? {files_to_delete}[/bold yellow]"
            )
            if confirm:
                # Perform deletion
                for filename in files_to_delete:
                    os.remove(os.path.join(directory, filename))

                save_movements(movements)
                rprint(f"Files [green]deleted[/green] in [blue]{directory}[/blue] using keys: [blue]{keys}[/blue].")
            else:
                rprint("[yellow]Deletion operation cancelled.[/yellow]")
        else:
            raise typer.BadParameter("Invalid option. Use 'key' or 'extension'.")

    except Exception as e:
        rprint(f"[bold red]Error deleting files:[/bold red] {e}")

@app.command()
def undo():
    """
    Undo the last file movement action.
    """
    movements = load_movements()
    if not movements:
        rprint("[yellow]No movements to undo.[/yellow]")
        return

    last_movement = list(movements.keys())[-1]
    movement_details = movements.pop(last_movement)
    save_movements(movements)

    if movement_details["to"] == "deleted":
        rprint(f"[bold yellow]Undo Operation cannot be performed for [red]Deleted File[red][/bold yellow]")
    else:
        os.replace(
            os.path.join(movement_details["to"], last_movement),
            os.path.join(movement_details["from"], last_movement),
        )
        rprint(f"[bold yellow]Undo:[/bold yellow] [bold green]Reverted[/bold green] [bold blue]{last_movement}[/bold blue] back to [bold blue]{movement_details['from']}[/bold blue].")

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

        rprint(f"Files in [blue]{directory}[/blue] renamed with pattern: [blue]{pattern}[/blue].")
    except Exception as e:
        rprint(f"[bold red]Error renaming files:[/bold red] {e}")

if __name__ == "__main__":
    app()
