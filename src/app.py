import pyodbc
from flask import Flask, render_template, request

app = Flask(__name__)

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\prath\OneDrive\Documents\TSATryoutDatabase.accdb;')
cursor = conn.cursor()


# cursor.execute("CREATE TABLE AdoptFormData ("
#               "FirstName varchar(255),"
#               "LastName varchar(255),"
#               "Email varchar(255),"
#               "Address varchar(255)"
#               ");")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submitadopt', methods=['GET', 'POST'])
def record_adopt_info():
    global cursor
    fname = request.form.get('fname1')
    lname = request.form.get('lname1')
    email = request.form.get('email1')
    address = request.form.get('address')

    query = 'INSERT INTO AdoptFormData (FirstName, LastName, Email, Address) VALUES (?, ?, ?, ?)'
    cursor.execute(query, fname, lname, email, address)

    return render_template('index.html')


@app.route('/submitdonate', methods=['GET', 'POST'])
def record_donate_info():
    global cursor
    fname = request.form.get('fname2')
    lname = request.form.get('lname2')
    email = request.form.get('email2')
    amount = request.form.get('amount')

    query = 'INSERT INTO DonateFormData (FirstName, LastName, Email, Amount) VALUES (?, ?, ?, ?)'
    cursor.execute(query, fname, lname, email, amount)

    return render_template('index.html')


@app.route('/submitvolunteer', methods=['GET', 'POST'])
def record_volunteer_info():
    global cursor
    fname = request.form.get('fname3')
    lname = request.form.get('lname3')
    email = request.form.get('email3')
    experience = request.form.get('experience')

    query = 'INSERT INTO DonateFormData (FirstName, LastName, Email, Experience) VALUES (?, ?, ?, ?)'
    cursor.execute(query, fname, lname, email, experience)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
