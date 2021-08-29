from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
#from datetime import date
#from flask_sessions import Sessions
import hashlib
from DB import db, query as q
import datetime


app = Flask(__name__)

app.secret_key = 'Lydoydodpdo6do6dpd_5#y2L"F4Q8z\n\xec]/'

conn = db.fypDB_Connect()
# Home Page
@app.route('/')
def hello():
    return render_template("index.html")

# logins

@app.route("/teacherlogin", methods=['GET', 'POST'])
def teacherlogin():
    try:
        if request.method == "POST":
            name = request.form['Name']
            password = request.form['Password']
            dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
            
            fetch_password = db.fetch(conn, q.get_teacher_pw.format(name))

            if fetch_password[0][0] == dk.hex():
                print("login successful!!!!")
                session['username']= name
        
                return redirect('/teacher')
        else:
            return render_template("teacherlogin.html")
    except:
        return redirect('/teacherlogin')


# student login
@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    if request.method == "POST":
        usn = request.form['USN']
        password = request.form['Password']
        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
    
        fetch_password = db.fetch(conn, q.get_student_pw.format(usn))
        
        if fetch_password[0][0] == dk.hex():
            print("login successful!!!")
            session['username'] = usn
            return redirect('/student')
        else:
            return render_template('studentlogin.html')
    else:
        return render_template("studentlogin.html")

# signup
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        usn = request.form['USN']
        password = request.form['Password']
        name = request.form['Name']
        email = request.form['Email']
        section = request.form['Section']
        branch = request.form['Branch']
        c_password = request.form['Confirm Password']

        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)
        section_id = db.fetch(conn, q.get_section_id.format(section))
        sectionId = section_id[0][0]

        if password == c_password:
            db.execute(conn,q.add_new_student.format(sectionId, usn, name, dk.hex(), email, branch))
            return redirect("/studentlogin")
        else:
            return redirect("/signup")
    else:
        return render_template("signup.html")


@app.route("/TSignup", methods=["POST", "GET"])
def tsignup():
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        department = request.form['Department']
        password = request.form['Password']
        c_password = request.form['Confirm Password']
        dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 100000)

        if password == c_password:
            db.execute(conn,q.add_new_teacher.format(name, dk.hex(), email, department))
            return redirect("/teacherlogin")
        else:
            return redirect("/TSignup")
    else:
        return render_template("TSignup.html")

# student homepage
@app.route("/student")
def student():
    if session['username']:
        now = datetime.datetime.now()
        day = now.strftime("%A")
        #print(day)
        classes = db.fetch(conn, q.get_classes.format(session['username'], day))
        return render_template('student.html', classes=classes, class_len= len(classes))
    else:
        return redirect('/studentlogin')


# teacher homepage
@app.route("/teacher")
def teacher():
    if session['username']:
        now = datetime.datetime.now()
        day = now.strftime("%A")
        classes = db.fetch(conn, q.get_teacher_cls.format(session['username'], day))
        return render_template('teacher.html',classes = classes, name=session['username'], class_len = len(classes) )
    else:
        return redirect('/teacherlogin')


@app.route("/schedule", methods=["POST", "GET"])
def schedule():
    # getting `courses` list 
    getcourses = db.fetch(conn, q.get_all_courses)
    courses = []
    for i in range(len(getcourses)): courses.append(getcourses[i][0])

    if session['username']:
        if request.method == "POST":
            if session['username']:
                section = request.form['section']
                n = int(request.form['course'])
                course = courses[n]
                link = request.form['link']
                day = request.form['day']
                time = request.form['time']
                section_id = db.fetch(conn, q.get_section_id.format(section))
                teacher_id = db.fetch(conn, q.get_teacher_id.format(session['username']))
                course_id = db.fetch(conn, q.get_courseId.format(course))
                
                db.execute(conn, q.add_class.format(section_id[0][0], course_id[0][0], link, day, time, teacher_id[0][0]))
                
                return redirect('/teacher')
            else:
                return redirect('/teacherlogin')
        else:

            return render_template("schedule.html", courses= courses, course_len= len(courses))
    else:
        return redirect('/teacherlogin')


@app.route("/grades")
def grades():
    #get students_list
    stud_tuple = db.fetch(conn, q.get_student_list)
    usn_list = []
    for i in range(len(stud_tuple)): usn_list.append(stud_tuple[i][2])
    #student_id = stud_tuple[5][0]
    if session['username']:
        if request.method == "POST":
            i = request.form['student_id']
            exam = request.form['exam']
            grades = int(request.form['grades'])
            return redirect('/teacher')
        else:
            return render_template("grades.html")
    else:
        return redirect('/teacherlogin')



@app.route("/upload")
def upload():
    return render_template("updates.html")

@app.route("/pwch<string>")
def pwch():
    return render_template("pwch.html")

@app.route("/controlpanel", methods=["GET", "POST"])
def controlpanel():
    if request.method == "POST":
        password = request.form['password']
        if password == "admin":
            return render_template("control.html")
        else:
            return render_template("admin_auth.html")
    else:
        return render_template("admin_auth.html")


@app.route('/test', methods=["GET", "POST"])
def test():
    # getting `courses` list
    getcourses = db.fetch(conn, q.get_all_courses)
    courses = []
    for i in range(len(getcourses)): courses.append(getcourses[i][0])
    # print(courses)

    if request.method == "POST":
        n = int(request.form['list'])
        print(n)
        print(courses[n])
        return redirect('/test')
    else:
         
       
        return render_template("test.html", courses=courses, course_len=len(courses))



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
    db.close(conn)