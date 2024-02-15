# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, url_for,send_from_directory,request

import sqlite3

db = sqlite3.connect("sum.db")
cursor = db.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS `adding` (    
        `operation_id` INTEGER AUTO_INCREMENT PRIMARY KEY ,
        `a_number` INTEGER NOT NULL,
        `b_number` INTEGER NOT NULL,
        `result`  INTEGER NULL,
        `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS `users` (    
        `user_id` INTEGER AUTO_INCREMENT PRIMARY KEY ,
        `fname` VARCHAR(30) NOT NULL,
        `lname` VARCHAR(30) NOT NULL,
        `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
)

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_url_path='/static')

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return send_from_directory('static', 'index.html')


@app.route('/add-two-numbers/<a_number>/<b_number>')
def add_two_numbers(a_number,b_number):
    db = sqlite3.connect("sum.db")
    cursor = db.cursor()
    result = int(a_number) + int(b_number)
    cursor.execute(f"""
        INSERT INTO `adding` (`a_number`, `b_number`, `result`)
            VALUES ({a_number},{b_number},{result})
    """)
    db.commit()
    return str(result)

@app.route('/submit_data')
def submit_data():
    fname = request.args.get("fname",default="???")
    lname = request.args.get("lname",default="???")
    db = sqlite3.connect("sum.db")
    cursor = db.cursor()
    cursor.execute(f"""
        INSERT INTO `users` (`fname`, `lname`)
            VALUES ("{fname}","{lname}")
    """)
    db.commit()

    return f"Welcome {fname} {lname}"

@app.route('/show')
def show():
    db = sqlite3.connect("sum.db")
    cursor = db.cursor()
    cursor.execute("""SELECT `operation_id`, `a_number`, `b_number`, `result`, `timestamp`
                   FROM `adding` 
                   """)
    rows = cursor.fetchall()
    html_result = """
    <html>
    <body>
    <table style="border-width: 1px; border-style: dotted;">
    """

    for row in rows:
        print(row)
        html_result += f"""<tr style="border-width: 1px; border-style: dotted;"><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>\n"""

    html_result += "</table></body></html>"
    return html_result
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
