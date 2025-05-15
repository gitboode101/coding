# json_diff.py

import datetime
from typing import Any, Dict, List, Union


class JsonDiffer:
    def __init__(self, old_data: Union[Dict, List], new_data: Union[Dict, List]):
        self.old_data = old_data
        self.new_data = new_data
        self.differences = []

    def compare(self):
        self.differences = [] 
    
        self._compare_recursive(self.old_data, self.new_data)
        return self.differences

    def _compare_recursive(self, old: Any, new: Any, path: str = ''):
        if type(old) != type(new):
            self._add_diff(path, old, new, type_diff=True)
            return

        if isinstance(old, dict):
            all_keys = set(old.keys()).union(new.keys())
            for key in all_keys:
                old_val = old.get(key)
                new_val = new.get(key)
                new_path = f"{path}.{key}" if path else key
                self._compare_recursive(old_val, new_val, new_path)

        elif isinstance(old, list):
            for i in range(max(len(old), len(new))):
                old_val = old[i] if i < len(old) else None
                new_val = new[i] if i < len(new) else None
                new_path = f"{path}[{i}]"
                self._compare_recursive(old_val, new_val, new_path)

        else:
            if old != new:
                self._add_diff(path, old, new, type_diff=False)

    def _add_diff(self, path: str, old_val: Any, new_val: Any, type_diff: bool):
        self.differences.append({
            "path": path,
            "old_value": old_val,
            "new_value": new_val,
            "type_diff": type_diff,
            "is_date": self._is_date(old_val) or self._is_date(new_val)
        })

    def _is_date(self, value: Any) -> bool:
        if isinstance(value, (datetime.date, datetime.datetime)):
            return True
        if isinstance(value, str):
            try:
                # يدعم التاريخ والوقت
                datetime.datetime.fromisoformat(value)
                return True
            except ValueError:
                return False
        return False


