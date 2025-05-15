# test_diff.py

import json
from json_diff import JsonDiffer

# ملف JSON القديم
old_data = {
    "students": [
        {"name": "Ali", "birthdate": "2002-05-01", "grades": {"math": 90}},
        {"name": "Sara", "birthdate": "2003-04-10"},
        {"name": "Mona", "active": True}
    ]
}

# ملف JSON الجديد
new_data = {
    "students": [
        {"name": "Ali", "birthdate": "2002-06-15", "grades": {"math": 92}},
        {"name": "Sara", "birthdate": "2003-04-10"},
        {"name": "Mona", "active": "yes"},
        {"name": "New Student", "birthdate": "2005-01-01"}
    ]
}

differ = JsonDiffer(old_data, new_data)
diffs = differ.compare()

# طباعة النتائج
for diff in diffs:
    print(json.dumps(diff, indent=2, ensure_ascii=False))
    from search_utils import (
    search_by_keyword,
    search_by_type_change,
    search_by_date_change
)

# البحث عن الفروقات التي تحتوي على "birthdate"
birthdate_diffs = search_by_keyword(diffs, "birthdate")
print("\n🔍 الفروقات في birthdate:")
for d in birthdate_diffs:
    print(d)

# البحث عن الفروقات التي تغير فيها نوع البيانات
type_diffs = search_by_type_change(diffs)
print("\n🧠 الفروقات في الأنواع:")
for d in type_diffs:
    print(d)

# البحث عن الفروقات التي تتضمن تواريخ
date_diffs = search_by_date_change(diffs)
print("\n📆 الفروقات التي تشمل تواريخ:")
for d in date_diffs:
    print(d)

