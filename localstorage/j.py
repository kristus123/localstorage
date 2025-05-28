import json
import os


def get(file_path, default=None):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path + ".json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path + ".json", 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
