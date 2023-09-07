from flask import Flask, render_template, request
import re
from collections import defaultdict

app = Flask(__name__)

GRADE_MAP = {
    'ＡＡ': 4.0,
    'Ａ': 3.0,
    'Ｂ': 2.0,
    'Ｃ': 1.0,
    'Ｄ': 0.0
}

def semester_number(year, term, start_year):
    return (year - start_year) * 2 + (1 if term in ["前期", "前期集中", "前期前半", "前期後半", "通年集中"] else 2)

@app.route('/')
def index():
    return render_template("index.html", gpa="N/A", semester_data={})

@app.route('/calculate_gpa', methods=["POST"])
def calculate_gpa():
    input_text = request.form['input_text']
    lines = input_text.split("\n")
    start_year = int(request.form['start_year']) # 入学年度の入力を想定

    semester_data = defaultdict(lambda: {"total_units": 0, "total_score": 0.0})

    for line in lines:
        semester_match = re.search(r'(\d{4})\s+(前期|前期前半|前期後半|前期集中|後期|後期前半|後期後半|後期集中|通年集中)', line)
        grade_match = re.search(r'(\d)\s+(ＡＡ|Ａ|Ｂ|Ｃ|Ｄ)', line)

        if semester_match and grade_match:
            year = int(semester_match.group(1))
            term = semester_match.group(2)
            current_semester = semester_number(year, term, start_year)

            units = int(grade_match.group(1))
            grade = grade_match.group(2)

            semester_data[current_semester]["total_units"] += units
            semester_data[current_semester]["total_score"] += GRADE_MAP.get(grade, 0) * units

    overall_units = sum(data["total_units"] for data in semester_data.values())
    overall_score = sum(data["total_score"] for data in semester_data.values())
    overall_gpa = overall_score / overall_units if overall_units != 0 else 0.0

    for semester_num, data in semester_data.items():
        data["gpa"] = data["total_score"] / data["total_units"] if data["total_units"] != 0 else 0

    # セメスター番号を名前に変換して、ソート
    sorted_semester_data = {f"{(semester_num-1)//2 + start_year} {(semester_num % 2) or 2}セメ": v for semester_num, v in sorted(semester_data.items())}

    return render_template("index.html", gpa=round(overall_gpa, 2), semester_data=sorted_semester_data)

if __name__ == "__main__":
    app.run(debug=True)
