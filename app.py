from flask import Flask, render_template, request

print(__file__)

import os

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
print(project_dir)

from flask_sqlalchemy import SQLAlchemy
    # Column, String, Integer
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydatabase.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Teacher(db.Model):
    full_name = db.Column(db.String(), primary_key=True, unique=True)
    password = db.Column(db.String())
    dob = db.Column(db.String())
    gender = db.Column(db.String())
    email = db.Column(db.String())
    phone_number = db.Column(db.Integer(), unique=False)
    subject = db.Column(db.String())
    
# def __init__(self, full_name, password, dob, gender, email, phone_number,subject):
#    self.full_name = full_name
#    self.password = password
#    self.dob = dob
#    self.gender = gender
#    self.email = email
#    self.phone_number = phone_number
#    self.subject = subject
#db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if (request.method == 'POST'):
        return render_template('teacher.html')
        full_name = request.form.get('full_name')
        password = request.form.get('password')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        subject = request.form.get('subject')

        entry = Teacher(full_name=full_name, password=password, dob=dob, gender=gender, email=email, phone_number=phone_number, subject=subject)
        return entry

        db.session.add(entry)
        db.session.commit()






@app.route('/student', methods=['GET', 'POST'])
def student():
        return render_template('student.html')



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
