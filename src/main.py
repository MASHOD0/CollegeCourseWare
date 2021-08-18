from flask import Flask, render_template, request, session
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

# Home Page
@app.route('/')
def hello():
    return render_template("index.html")

# logins and signups

@app.route("/teacherlogin", methods=['GET', 'POST'])
def teacherlogin():
    if request.method == "POST":
        name = request.form['Name']
        password = request.form['Password']
        return redirect(f'/teacher-{name}')
    else:
        return render_template("teacherlogin.html")


@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    if request.method == "POST":
        usn = request.form['USN']
        password = request.form['Password']
        return redirect(f'/student-{usn}')
    else:
        return render_template("studentlogin.html")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        usn = request.form['USN']
        section = request.form['section']
        password = request.form['Password']
        c_password = request.form["Confirm Password"]
        if password != c_password:
            return render_template("signup.html")
        else:
            return redirect("/studentlogin")
    else:
        return render_template("signup.html")


@app.route("/TSignup")
def tsignup():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['Password']
        c_password = request.form["Confirm Password"]
        if password != c_password:
            return render_template("TSignup.html")
        else:
            return redirect("/teacherlogin")
    else:
        return render_template("TSignup.html")


@app.route("/student")
def student(usn):
    return render_template('student.html', name=usn)

@app.route("/teacher")
def teacher(name):
    return render_template('teacher.html', name=name)

@app.route("/classes")
def classes():
    return render_template("class.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/grades")
def grades():
    return render_template("grades.html")

@app.route("/upload")
def upload():
    return render_template("updates.html")

@app.route("/pwch<string>")
def pwch():
    return render_template("pwch.html")

@app.route("/controlpanel", methods=["GET", "POST"])
def controlpanel():
    if method == "POST":
        password = request.form['password']
        if password == "admin":
            return render_template("control.html")
        else:
            return render_template("admin_auth.html")
    else:
        return render_template("admin_auth.html")

@app.route("/create_sections")
def sections():
    return render_template("create_sections.html")
@app.route("/create_courses")
def courses():
    return render_template("create_courses.html")



@app.route("/logout")
def logout():
    if session['username']:
        session.clear()
    

    return redirect("/")



if __name__ == '__main__':
    app.run(debug = True)