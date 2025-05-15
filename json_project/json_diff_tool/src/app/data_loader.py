from pathlib import Path
import json
import easygui

def select_json_folder():
    folder = easygui.diropenbox(title="Select folder with JSON files")
    return folder

def get_latest_json_files(folder_path: str):
    folder = Path(folder_path)
    json_files = list(folder.glob("*.json"))
    if len(json_files) < 2:
        raise ValueError("At least two JSON files are required.")
    json_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    
    return json_files[0], json_files[1]

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

