from datetime import datetime

def normalize(value):
    """تحويل القيم إلى صيغة قابلة للمقارنة"""
    try:
        return float(value)
    except:
        pass

    try:
        return datetime.fromisoformat(value)
    except:
        pass

    try:
        return datetime.strptime(value, "%d/%m/%Y")
    except:
        pass

    try:
        return datetime.strptime(value, "%d.%m.%Y")
    except:
        pass

    return str(value).lower().strip()

def smart_search_json(data, keyword, path="root"):
    results = []
    keyword_norm = normalize(keyword)

    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}['{key}']"
            if keyword_norm == normalize(key) or keyword_norm == normalize(value):
                results.append((current_path, value))
            results.extend(smart_search_json(value, keyword, current_path))

    elif isinstance(data, list):
        for index, item in enumerate(data):
            current_path = f"{path}[{index}]"
            if keyword_norm == normalize(item):
                results.append((current_path, item))
            results.extend(smart_search_json(item, keyword, current_path))

    return results


# data = read_json(file1)  # أو file2

# keyword = input("🔍 أدخل الكلمة / الرقم / التاريخ للبحث الذكي: ").strip()
# matches = smart_search_json(data, keyword)

# if matches:
#     for path, value in matches:
#         print(f"📍 المسار: {path}\n🔸 القيمة: {value}\n")
# else:
#     print("❌ لم يتم العثور على تطابق.")
