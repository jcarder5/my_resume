import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)



class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    number = db.Column(db.Integer)
    description = db.Column(db.Text)



@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/professors')
def show_all_professors():
    professors = Professor.query.all()
    return render_template('professor-all.html', professors=professors)


@app.route('/professor/add', methods=['GET', 'POST'])
def add_professor():
    if request.method == 'GET':
        return render_template('professor-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['department']

        # insert the data into the database
        professor = Professor(name=name, department=department)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('show_all_professors'))



@app.route('/professor/edit/<int:id>', methods=['GET', 'POST'])
def edit_professor(id):
    professor = Professor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('professor-edit.html', professor=professor)
    if request.method == 'POST':
        # update data based on the form data
        professor.name = request.form['name']
        professor.about = request.form['department']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_professor'))


# song-all.html adds song id to the edit button using a hidden input
@app.route('/courses')
def show_all_courses():
    courses = Course.query.all()
    return render_template('course-all.html', courses=courses)


@app.route('/course/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'GET':
        professors = Professor.query.all()
        return render_template('course-add.html', professors=professors)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        lyrics = request.form['lyrics']
        course = Course(name=name, number=number, description=description)

        # insert the data into the database
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('show_all_courses'))


@app.route('/course/edit/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    course = Course.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('course-edit.html', course=course)
    if request.method == 'POST':
        # update data based on the form data
        course.name = request.form['name']
        course.year = request.form['number']
        course.lyrics = request.form['description']

        # update the database
        db.session.commit()
        return redirect(url_for('show_all_courses'))









# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
