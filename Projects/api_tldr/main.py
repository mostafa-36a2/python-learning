from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Hello world"









# # simple calculator
# @app.route("/calculator/<a>/<b>", methods=["POST","GET"])
# def calculator(a, b):
#     return {"a":a, "b":b}

# app.run()

# exit()







# # API to get single value
# @app.route("/get-students-count", methods=["GET"])
# def get_students_count():
#     import os
#     import sqlite3

#     db_dir = os.path.dirname(__file__)
#     db_path = os.path.join(db_dir, "db.sqlite3")
#     db_connection = sqlite3.connect(db_path)
#     cr = db_connection.cursor()
#     cr.execute("SELECT COUNT(*) FROM `students`")
#     row = cr.fetchone()
#     print(row)
#     print(f"count of students is {row[0]}")
#     return str(row[0])

# # API to get json
# @app.route("/get-students1", methods=["GET"])
# def get_students1():
#     import os
#     import sqlite3

#     db_dir = os.path.dirname(__file__)
#     db_path = os.path.join(db_dir, "db.sqlite3")
#     db = sqlite3.connect(db_path, check_same_thread=False)
#     cr = db.cursor()
#     cr.execute("SELECT * FROM `students`")
#     rows = cr.fetchall()
#     print(rows)
#     # [(1, 'rami', 'rami.jpg', 'the king', '2023-02-01'),
#     #  (2, 'sami', 'sami.png', 'sasomi', '2023-03-01'),
#     #  (3, 'iyad', 'iiii.jpg', 'manager', '2023-01-01'),
#     #  (4, 'khaled', 'khkh.jpeg', 'flash', '2023-01-02')]
#     return rows


# @app.route("/get-students2", methods=["GET"])
# def get_students2():
#     import os
#     import sqlite3

#     db_dir = os.path.dirname(__file__)
#     db_path = os.path.join(db_dir, "db.sqlite3")
#     db = sqlite3.connect(db_path, check_same_thread=False)
#     cr = db.cursor()
#     cr.execute("SELECT * FROM `students`")
#     rows = cr.fetchall()
#     print(rows)
#     # [(1, 'rami', 'rami.jpg', 'the king', '2023-02-01'),
#     #  (2, 'sami', 'sami.png', 'sasomi', '2023-03-01'),
#     #  (3, 'iyad', 'iiii.jpg', 'manager', '2023-01-01'),
#     #  (4, 'khaled', 'khkh.jpeg', 'flash', '2023-01-02')]
#     res = []
#     for row in rows:
#         res.append(
#             {
#                 "id": row[0],
#                 "name": row[1],
#                 "image": row[2],
#                 "nickname": row[3],
#                 "registration": row[4],
#             }
#         )
#     return res


# @app.route("/download-image/<image_name>", methods=["GET"])
# def download_image(image_name):
#     # https://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response
#     import os

#     from flask import send_file

#     return send_file(os.path.join("static", "images", image_name), mimetype="image/*")
#     #return send_file("static/files/file.txt",as_attachment=True)

# @app.route("/get-image/<image_name>", methods=["GET"])
# def get_image_url(image_name):
#     return f"<img src='/static/images/{image_name}'>"







@app.route("/get-student-data/<student_id>", methods=["GET"])
def get_student_data(student_id):
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT * FROM `students` WHERE `id` = '{student_id}'")
    rows = cr.fetchall()
    print(rows)
    return list(rows)


@app.route("/get-student-card/<student_id>", methods=["GET"])
def get_student_card(student_id):
    # https://www.w3schools.com/howto/howto_css_cards.asp
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT * FROM `students` WHERE `id` = '{student_id}'")
    row = cr.fetchone()
    print(row)
    return f"""
     <div class="card" style="border: solid black 1px; width: 20%;padding-left:10%">
        <img src="/static/images/{row[2]}" alt="{row[1]} image">
        <div class="container">
            <h4><b>{row[0]}. {row[1]}</b></h4>
            <p>{row[3]}</p>
            <p>{row[4]}</p>
        </div>
    </div> 
    """


@app.route("/get-student-card2/<student_id>", methods=["GET"])
def get_student_card2(student_id):
    # https://www.w3schools.com/howto/howto_css_cards.asp
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT * FROM `students` WHERE `id` = '{student_id}'")
    row = cr.fetchone()
    print(row)
    return render_template(
        "card.html",
        image_src=f"/static/images/{row[2]}",
        image_alt=row[1],
        title=f"{row[0]}. {row[1]}",
        details1=row[3],
        details2=row[4],
    )


@app.route("/students/")
def students1():
    print(render_template("students.html", title="Students", home=True))
    return render_template("students.html", title="Students", home=True)




@app.route("/students/<name>")
def students2(name):
    return render_template("students.html", title="Students", home=False, username=name)






# https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters
@app.route("/students_with_jinja_for_loop/", defaults={"name": None})
@app.route("/students_with_jinja_for_loop/<name>")
def students_with_jinja_for_loop(name):
    return render_template(
        "students_with_loop.html", title="Students", home=not name, username=name
    )


@app.route("/students_with_jinja_for_loop2/", defaults={"name": None})
@app.route("/students_with_jinja_for_loop2/<name>")
def students_with_jinja_for_loop2(name):
    return render_template(
        "students_with_loop_and_pass_paras.html",
        title="Students",
        home=not name,
        username=name,
        abcde=["1 ahmad", "2 samir", "3 sameer"],
    )


@app.route("/students_with_jinja_for_loop3/", defaults={"name": None})
@app.route("/students_with_jinja_for_loop3/<name>")
def students_with_jinja_for_loop3(name):
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT `student-name` FROM `students`")
    rows = cr.fetchall()
    print(rows)
    rows = [row[0] for row in rows]
    return render_template(
        "students_with_loop_and_pass_paras_from_db.html",
        title="Students",
        home=not name,
        username=name,
        items_from_python=rows,
    )


@app.route(
    "/students_with_jinja_for_loop4/", defaults={"name": None, "student_id": None}
)
@app.route("/students_with_jinja_for_loop4/<name>/<student_id>/")
def students_with_jinja_for_loop4(name, student_id):
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT `student-name`,`id` FROM `students`")
    students_rows = cr.fetchall()
    print(f"students_rows: {students_rows}")

    cr.execute(f"SELECT * FROM `students` WHERE `id` = '{student_id}'")
    row = cr.fetchone()
    print(row)
    card_html = None
    if row:
        card_html = render_template(
            "card.html",
            image_src=f"/static/images/{row[2]}",
            image_alr=row[1],
            title=f"{row[0]}. {row[1]}",
            details1=row[3],
            details2=row[4],
        )

    return render_template(
        "students_with_loop_and_pass_paras_from_db_and_card.html",
        title="Students",
        home=not name,
        username=name,
        student_id=student_id,
        students=students_rows,
        # https://stackoverflow.com/questions/3206344/passing-html-to-template-using-flask-jinja2
        card_html=card_html,
    )


@app.route(
    "/students_with_jinja_for_loop5/", defaults={"name": None, "student_id": None}
)
@app.route("/students_with_jinja_for_loop5/<name>/<student_id>/")
def students_with_jinja_for_loop5(name, student_id):
    import os
    import sqlite3

    db_dir = os.path.dirname(__file__)
    db_path = os.path.join(db_dir, "db.sqlite3")
    db = sqlite3.connect(db_path, check_same_thread=False)
    cr = db.cursor()
    cr.execute(f"SELECT `student-name`,`id` FROM `students`")
    students_rows = cr.fetchall()
    print(f"students_rows: {students_rows}")

    cr.execute(f"SELECT * FROM `students` WHERE `id` = '{student_id}'")
    row = cr.fetchone()
    print(row)

    return render_template(
        "students_with_loop_and_pass_paras_from_db_and_card_but_js.html",
        title="Students",
        home=not name,
        username=name,
        student_id=student_id,
        students=students_rows,
    )


app.run()
