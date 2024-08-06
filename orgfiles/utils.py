import os
import json

MOVEMENTS_FILE = "file_movements.json"

def save_movements(movements):
    with open(MOVEMENTS_FILE, "w") as file:
        json.dump(movements, file, indent=4)

def load_movements():
    movements = {}
    if os.path.exists(MOVEMENTS_FILE):
        with open(MOVEMENTS_FILE, "r") as file:
            movements = json.load(file)
    else:
        save_movements(movements)  # Create an empty file if it doesn't exist
    return movements

