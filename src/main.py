from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
# from datetime import date
# from flask_sessions import Sessions
import hashlib
from DB import db, query as q
import datetime
# from flask_wtf import FlaskForm, RecaptchaField
# from wtforms import SelectField, TextField


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dodpdo6do6dpd_5#y2L"F'
app.secret_key = 'Lydoydodpdo6do6dpd_5#y2L"F4Q8z\n\xec]/'

#connection to database
conn = db.fypDB_Connect()

# Home Page
@app.route('/')
def hello():
    return render_template("index.html")


# signup
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    """
    This is signup page for students
    """
    if request.method == "POST":
        usn = request.form['USN']
        password = request.form['Password']
        name = request.form['Name']
        email = request.form['Email']
        section = request.form['Section']
        branch = request.form['Branch']
        c_password = request.form['Confirm Password']

        # password hash
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


#teacher signup
@app.route("/TSignup", methods=["POST", "GET"])
def tsignup():
    """
    Teachers signup
    """

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
  

# logins
@app.route("/teacherlogin", methods=['GET', 'POST'])
def teacherlogin():
    """
    This is the login for teachers.
    """
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
    """
    This is the login for students.
    """

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





# student homepage
@app.route("/student")
def student():
    """
    Student homepage
    """
    if session['username']:
        now = datetime.datetime.now()
        day = now.strftime("%A")
        #print(day)
        classes = db.fetch(conn, q.get_classes.format(session['username'], day))
        grades = db.fetch(conn, q.get_grades.format(session['username']))
        return render_template('student.html', classes=classes, class_len= len(classes), grades = grades, grade_len = len(grades))
    else:
        return redirect('/studentlogin')


# teacher homepage
@app.route("/teacher")
def teacher():
    """
    Teacher Homepage
    """
    if session['username']:
        # getting the day
        now = datetime.datetime.now()
        day = now.strftime("%A")
        classes = db.fetch(conn, q.get_teacher_cls.format(session['username'], day))
        return render_template('teacher.html',classes = classes, name=session['username'], class_len = len(classes) )
    else:
        return redirect('/teacherlogin')


@app.route("/schedule", methods=["POST", "GET"])
def schedule():
    """
    Page for scheduling classes
    """
    # getting `courses` list 
    getcourses = db.fetch(conn, q.get_all_courses)
    courses = []
    for i in range(len(getcourses)): 
        if getcourses != None : courses.append(getcourses[i][0])

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



@app.route("/grades", methods=['GET', 'POST'])
def grades():
    """
    Page for adding grades , there is another page which consists of that.
    """
    get_section_subject = db.fetch(conn, q.get_section_from_grades)

    if session['username']:
        if request.method == "POST":
            session["section"] = int(request.form["section_course"])

            session["exam"] = request.form['exam']
        
            return redirect("/grades1")
            
            # if request.method == "POST":
            #     for i in range(len(get_usn)):
            #         print(request.form[str(i)])
            # else:
            #     return render_template("grades1.html", usn = get_usn, usn_len =len(get_usn))
                
            
        else:
            return render_template("grades.html", list = get_section_subject, list_len = len(get_section_subject), )
    else:
        return redirect('/teacherlogin')

@app.route("/grades1", methods=["GET", "POST"])
def grades1():
    section = session["section"]
    exam = session["exam"]
     
    get_section_subject = db.fetch(conn, q.get_section_from_grades)
    get_usn = db.fetch(conn, q.get_section_usn.format(get_section_subject[section][0]))
    print(get_usn)


    if session['username']:
        if request.method == "POST":
            for i in range(len(get_usn)):
                marks = int(request.form[str(i)])
                db.execute(conn, q.update_grades.format(exam, marks, get_usn[i][0]))

            return redirect('/grades')
        else:
            return render_template("grades1.html", usn = get_usn, usn_len =len(get_usn))

    else:
        return redirect('/teacherlogin')







@app.route("/update", methods=["GET", "POST"])
def update():
    # getting the list of courses
    courses_and_ids = db.fetch(conn, q.get_courses)
    courses= []
    course_id= []

    for i in range(len(courses_and_ids)): courses.append(courses_and_ids[i][1])
    for i in range(len(courses_and_ids)): course_id.append(courses_and_ids[i][0])

    # getting the list of sections
    sections_and_ids = db.fetch(conn, q.get_sections)
    section_id = []
    sections = []

    for i in range(len(sections_and_ids)): section_id.append(sections_and_ids[i][0])
    for i in range(len(sections_and_ids)): sections.append(sections_and_ids[i][1])

    if session['username']:
        if request.method == "POST":
            section_id = int(request.form['section'])
            course_id = int(request.form['course'])
            semester = int(request.form['semester'])
            # print(section_id)
            # print(course_id)
            # print(semester)

            student_id = db.fetch(conn, q.get_section.format(section_id))

            for i in range(len(student_id)):
                db.execute(conn, q.add_student_to_grades.format(student_id[i][0], course_id, semester, section_id))
                print("student added to grades")

            for i in range(len(student_id)):
                db.execute(conn, q.add_student_to_attendance.format(student_id[i][0], course_id, section_id))
                print("student added to attendance")


            return redirect('/teacher')
        else:
            return render_template("updates.html", section_id= section_id, sections= sections, sect_len= len(sections), course_id = course_id, course = courses, course_len =len(courses) )
           







@app.route("/attendence", methods=['GET', 'POST'])
def attendance():
    get_section_subject = db.fetch(conn, q.get_section_from_attendance)

    if session['username']:
        if request.method == "POST":
            session["section_att"] = int(request.form["section_course"])
            
        
            return redirect("/attendance1")
            
            # if request.method == "POST":
            #     for i in range(len(get_usn)):
            #         print(request.form[str(i)])
            # else:
            #     return render_template("grades1.html", usn = get_usn, usn_len =len(get_usn) )
                
            
        else:
            return render_template("attendance.html", list = get_section_subject, list_len = len(get_section_subject) )
    else:
        return redirect('/teacherlogin')



@app.route('/attendance1', methods=["GET", "POST"])
def attendance1():
    section = session["section_att"]
    get_section_subject = db.fetch(conn, q.get_section_from_attendance)
    get_usn = db.fetch(conn, q.get_section_name.format(get_section_subject[section][0], get_section_subject[section][1]))
    print(get_usn)

    if get_usn[0][4] == None:
        total = 1
    else:
        total = get_usn[0][4] + 1
    print(total)
    if session['username']:
        if request.method == "POST":

            absentee = request.form.getlist('absentee')
            absentee = [int(i) for i in absentee]
            
            print(absentee)
            for i in range(len(get_usn)):
                db.execute(conn, q.add_total.format(total, get_usn[i][0], get_section_subject[section][1], get_section_subject[section][0] ))


            for i in range(len(absentee)):
                missed = db.fetch(conn, q.get_missed.format(get_usn[absentee[i]][0], get_section_subject[section][1], get_section_subject[section][0]))
                missed_int = missed[0][0]  
                if missed_int == None:
                    missed_int = 1
                else:
                    missed_int += 1
                db.execute(conn, q.add_missed.format(missed_int, get_usn[absentee[i]][0], get_section_subject[section][1], get_section_subject[section][0]))

            return redirect('/grades')
        else:
            return render_template("attendance1.html", usn_list = get_usn, usn_len =len(get_usn))

    else:
        return redirect('/teacherlogin')









@app.route("/pwch<string>", methods=["GET", "POST"])
def pwch(string):
    return render_template("pwch.html")

@app.route("/controllogin", methods=["GET", "POST"])
def controlpanel():
    if request.method == "POST":
        password = request.form['password']
        if password == "admin":
            return render_template("control.html")
        else:
            return render_template("admin_auth.html")
    else:
        return render_template("admin_auth.html")


@app.route("/create_sections", methods = ["GET", "POST"])
def sections():
    if request.method == "POST":
        name = request.form["section"]
        sem = int(request.form["semester"])
        db.execute(conn, q.add_sections.format(sem, name))
        return render_template("control.html")
    else:
        return render_template("create_sections.html")



@app.route("/create_courses", methods = ["GET", "POST"])
def courses():
    if request.method == "POST":
        course = request.form["course"]
        department = request.form["department"]
        db.execute(conn, q.add_courses.format(department, course))
        return render_template("control.html")
    else:
        return render_template("create_courses.html")



@app.route("/logout")
def logout():
    if session['username']:
        session.clear()
    return redirect("/")

# Create a class form 

if __name__ == '__main__':
    app.run(debug = True)
    db.close(conn)