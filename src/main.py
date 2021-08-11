from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/teacherlogin")
def teacherlogin():
    if request.method == "POST":
        name = request.form['Name']
        password = request.form['Password']
        return render_template(f'/teacher-{name}')
    else:
        return render_template("teacherlogin.html")


@app.route("/studentlogin")
def studentlogin():
    return render_template("studentlogin.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")
    

@app.route("/student-<usn>")
def home(name):
    return render_template('student.html', content=usn)

@app.route("/teacher-<name>")
def home(name):
    return render_template('teacher.html', content=name)

@app.route("/logout")
def logout():
    if session['username']:
        session.clear()
    

    return redirect("/")



if __name__ == '__main__':
    app.run(debug = True)