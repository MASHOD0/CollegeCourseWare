#1
get_section_id = """
                SELECT section_id
                FROM sections
                WHERE sections = '{}';
                """

#2
get_student_pw="""SELECT distinct password
                FROM student
                WHERE "USN" = '{}' 
                LIMIT  1;
                """

#3
get_teacher_pw="""
                SELECT distinct password
                FROM teachers
                WHERE name = '{}' 
                LIMIT  1;
                """

#4
add_new_student = """
                INSERT INTO student(student_id, section_id, "USN", "Name", password, email, branch)
                VALUES (DEFAULT, {}, '{}', '{}', '{}', '{}', '{}');
                """

#5
add_new_teacher = """
                INSERT INTO teachers (teacher_id, name, password, email, department) 
                VALUES (DEFAULT, '{}', '{}', '{}', '{}');
                 """

#6
get_classes = """
                SELECT class_id,classes.course_id, "link", "time", courses.course_code, department
                FROM classes
                JOIN courses
                ON classes.course_id = courses.course_id
                WHERE section_id = (select section_id from student where "USN" = '{}' limit 1)
                AND day = '{}';
                """

#7
get_teacher_cls = """
                SELECT sections.sections, courses.course_code, link, "time"
                FROM classes
                INNER JOIN courses ON classes.course_id = courses.course_id
				INNER JOIN teachers ON classes.teacher_id = teachers.teacher_id 
				LEFT JOIN sections ON classes.section_id = sections.section_id
				where teachers.name = '{}'
				AND "day" = '{}';
                """

#8
add_class = """
            INSERT INTO classes(
	        section_id, course_id, link, day, "time", class_id, teacher_id)
	        VALUES ({}, {}, '{}','{}', '{}:00', default, {});
            """

#9
get_courseId="""
            SELECT course_id 
	        FROM public.courses
	        WHERE course_code = '{}'
            LIMIT 1;
            """

#10
get_teacher_id = """
                SELECT teacher_id FROM  teachers WHERE name = 'Ananth Raju' limit 1;
                """

#11
get_all_courses = """
                    SELECT course_code
                    FROM courses;
                """

#12
get_student_list = """SELECT grades.student_id, semester, course_id, student."USN" 
                        FROM grades
                        INNER JOIN student ON  grades.student_id = student.student_id;
                    """

#13
update_grades = """UPDATE public.grades
                    SET "{}"={}
                    WHERE student_id = {};
                """

#14 
get_section = """SELECT student_id FROM student WHERE section_id = {};"""

#15
add_student_to_grades = """INSERT INTO grades(student_id, course_id, semester, section_id) VALUES ({}, {}, {}, {})"""

#16
add_courses = """INSERT INTO courses(course_id, department, course_code) VALUES (DEFAULT, '{}', '{}');"""

#17
add_sections = """INSERT INTO sections(section_id, semester, sections) VALUES (DEFAULT, {}, '{}');"""

#18
get_sections = """
                SELECT section_id, sections
                FROM sections
                """

#19
get_courses = """SELECT course_id, course_code FROM courses;"""

#20
get_section = """SELECT student_id FROM student WHERE section_id = {};"""

#21
add_student_to_attendance = """INSERT INTO "Attendance"(student_id, course_id, section_id) VALUES ({}, {}, {});""" 

#22
get_section_from_grades ="""SELECT DISTINCT grades.section_id, grades.course_id, courses.course_code, sections.sections 
                            FROM grades
                            INNER JOIN courses ON grades.course_id = courses.course_id
                            INNER JOIN sections on grades.section_id = sections.section_id;
                         """

#23
get_section_usn = """SELECT student_id, "USN" FROM student WHERE section_id = {};"""

#24
get_section_from_attendance = """SELECT DISTINCT "Attendance".section_id, "Attendance".course_id,courses.course_code , sections.sections 
                            FROM "Attendance"
                            INNER JOIN courses ON "Attendance".course_id = courses.course_id
                            INNER JOIN sections on "Attendance".section_id = sections.section_id;
                            """

#25
get_section_name = """select "Attendance".student_id, "USN", "Name", missed, total from "Attendance" 
                    INNER JOIN "student" ON "Attendance".student_id = student.student_id
                    WHERE "Attendance".section_id = {}
                    AND "Attendance".course_id = {};
                    """
#26
add_total = """UPDATE public."Attendance"
                SET total= {}
                WHERE student_id = {}
                AND course_id = {}
                AND section_id = {};
            """
#27
add_missed = """UPDATE public."Attendance"
                SET missed= {}
                WHERE student_id = {}
                AND course_id = {}
                AND section_id = {};
            """
#28
get_missed = """SELECT missed
                FROM public."Attendance"
                WHERE student_id = {}
                AND course_id = {}
                AND section_id = {};
            """
#29
get_grades=  """
            select courses.course_code, semester, "CIE_1", "CIE_2", "CIE_3", "AAT", "SEE" from grades
            inner join courses
            on grades.course_id = courses.course_id
            where student_id = (select student_id from student where "USN" = '{}');
            """
get_attendance = """
                    select courses.course_code,  missed, total from "Attendance"
                    inner join courses
                    on "Attendance".course_id = courses.course_id
                    where student_id = (select student_id from student where "USN" = '{}');
                    """