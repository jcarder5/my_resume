from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home-page.html')



@app.route('/course')
def get_course():
    courses = [
        'MISY350',
        'ACCT315',
        'ACCT208'

        ]

    return render_template('courses.html', courses = courses)


@app.route('/about')
def get_about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run()
