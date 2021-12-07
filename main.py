from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/timetable1/<int:marks_eng>/<int:marks_sst>/<int:marks_mat>/<int:marks_sci>')
def main1(marks_eng, marks_sst, marks_mat, marks_sci):
    list_marks = [marks_eng, marks_sst, marks_mat, marks_sci]

    timetable = []
    sorted2 = sorted(list_marks)
    # print(sorted)
    for i in sorted2:
        if marks_eng == i:
            timetable.append("English")
        if marks_sci == i:
            timetable.append("Science")
        if marks_mat == i:
            timetable.append("Mathematics")
        if marks_sst == i:
            timetable.append("Social Science")

    # print(litimetable)
    timetable2 = [timetable[1], timetable[2], timetable[0], timetable[3]]
    timetable1 = {
        "1st": timetable[0],
        "2nd": timetable[1],
        "3rd": timetable[2],
        "4th": timetable[3]
    }
    timetable3 = {
        "1st": timetable2[0],
        "2nd": timetable2[1],
        "3rd": timetable2[2],
        "4th": timetable2[3]
    }

    return timetable1

@app.route('/timetable2/<int:marks_eng>/<int:marks_sst>/<int:marks_mat>/<int:marks_sci>')
def main2(marks_eng, marks_sst, marks_mat, marks_sci):
    list_marks = [marks_eng, marks_sst, marks_mat, marks_sci]

    timetable = []
    sorted2 = sorted(list_marks)
    # print(sorted)
    for i in sorted2:
        if marks_eng == i:
            timetable.append("English")
        if marks_sci == i:
            timetable.append("Science")
        if marks_mat == i:
            timetable.append("Mathematics")
        if marks_sst == i:
            timetable.append("Social Science")

    # print(litimetable)
    timetable2 = [timetable[1], timetable[2], timetable[0], timetable[3]]
    timetable1 = {
        "1st": timetable[0],
        "2nd": timetable[1],
        "3rd": timetable[2],
        "4th": timetable[3]
    }
    timetable3 = {
        "1st": timetable2[0],
        "2nd": timetable2[1],
        "3rd": timetable2[2],
        "4th": timetable2[3]
    }

    return timetable3
    

if __name__ == '__main__':
    app.run(debug=True)
