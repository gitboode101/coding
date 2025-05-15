# search_utils.py

from typing import List, Dict

def search_by_keyword(diffs: List[Dict], keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    return [
        d for d in diffs
        if keyword in str(d['path']).lower()
        or keyword in str(d['old_value']).lower()
        or keyword in str(d['new_value']).lower()
    ]

def search_by_type_change(diffs: List[Dict]) -> List[Dict]:
    return [d for d in diffs if d.get('type_diff')]

def search_by_date_change(diffs: List[Dict]) -> List[Dict]:
    return [d for d in diffs if d.get('is_date')]
