import os 
import pandas as pd 
from pathlib import Path
from deepdiff import DeepDiff
import json 

def file_path(file) :
    folder = Path(file)
    if not folder.exists() or not folder.is_dir():
        print('false path dir ')
        return exit(1)
    json_file =list(folder.glob("*.json"))
    if len(json_file) < 2 :
        print('min must 2 json files in folder')
        return exit(1)    
    json_file.sort(key=lambda f:f.stat().st_mtime,reverse = True)
    return json_file


def get_file(json_file):
    return    json_file[0],json_file[1]
folder_input = input('enter folder path : ').strip()
def read_json(file_path) :
    with open(file_path , 'r' ,encoding = 'utf-8') as f :
        return json.load(f)
def compare_json(data1,data2) :
    return DeepDiff(data1,data2,verbose_level=2)   
def diff_to_filtered_rows(diff_result, keyword):
    rows = []

    for diff_type, changes in diff_result.items():
        if isinstance(changes, dict):
            for path, change in changes.items():
                if keyword.lower() in path.lower():
                    old = change.get('old_value', None)
                    new = change.get('new_value', None)
                    rows.append({
                        'type': diff_type,
                        'dir_path': path,
                        'old_itm': old,
                        'new_itm': new
                    })

    return rows


json_file = file_path(folder_input)
file1,file2 = get_file(json_file)
print(f'{file1}\n {file2}')
data1 = read_json(file1)
data2 = read_json(file2)

diff = compare_json(data1, data2)
print(json.dumps(diff ,indent =2 ,ensure_ascii =False))


def diff_to_rows(diff_result):
    rows = []

    for diff_type, changes in diff_result.items():
        if isinstance(changes, dict):
            for path, change in changes.items():
                old = change.get('old_value', None)
                new = change.get('new_value', None)
                rows.append({
                    'type': diff_type,
                    'dir_path': path,
                    'old_itm': old,
                    'new_itm': new
                })
        elif isinstance(changes, set):
            for item in changes:
                rows.append({
                    'type': diff_type,
                    'dir_path': item,
                    'old_itm': None,
                    'new_itm': None
                })

    return rows
rows = diff_to_rows(diff)
df = pd.DataFrame(rows)
print(df.head(200))



        