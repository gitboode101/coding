from flask import Blueprint, render_template, request, jsonify
from json_diff import JsonDiffer
from app.data_loader import select_json_folder, get_latest_json_files, read_json
from search_utils import search_by_keyword, search_by_type_change, search_by_date_change
import pandas as pd
import easygui

routes = Blueprint('routes', __name__)
current_diffs = []  # will store current diff globally

@routes.route('/', methods=['GET', 'POST'])
def index():
    global current_diffs
    keyword = request.form.get('keyword')
    filter_type = request.form.get('filter')
    filtered = current_diffs

    if keyword:
        filtered = search_by_keyword(filtered, keyword)

    if filter_type == 'type_diff':
        filtered = search_by_type_change(filtered)
    elif filter_type == 'is_date':
        filtered = search_by_date_change(filtered)

    return render_template('index.html', diffs=filtered)

@routes.route('/load-folder', methods=['POST'])
def load_folder():
    global current_diffs
    try:
        folder = select_json_folder()
        print("📂 Selected folder:", folder)

        if not folder:
            print("❌ No folder selected.")
            return jsonify({"status": "cancelled", "message": "No folder selected."})

        file1, file2 = get_latest_json_files(folder)
        print("🟢 File 1:", file1)
        print("🟢 File 2:", file2)

        data1 = read_json(file1)
        data2 = read_json(file2)
        print("📖 Loaded both JSON files.")

        differ = JsonDiffer(data1, data2)
        current_diffs = differ.compare()

        print("✅ Differences found:", len(current_diffs))

        return jsonify({
            "status": "success",
            "file1": str(file1.name),
            "file2": str(file2.name)
        })

    except Exception as e:
        print("❌ ERROR:", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        })


@routes.route('/save', methods=['POST'])
def save():
    data = request.json.get('data')
    df = pd.DataFrame(data)
    file_path = easygui.filesavebox(
        title="Choose location to save results",
        default="results.csv",
        filetypes=["*.csv", "*.xlsx"]
    )
    if file_path:
        if file_path.endswith(".xlsx"):
            df.to_excel(file_path, index=False)
        else:
            df.to_csv(file_path, index=False)
    return jsonify({'status': 'success'})
