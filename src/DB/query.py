get_section_id = """
                SELECT section_id
                FROM sections
                WHERE sections = '{}';
                """
get_student_pw="""select distinct password
                from student
                where "USN" = '{}' 
                limit  1;
                """
add_new_student = """
                INSERT INTO student(student_id, section_id, "USN", "Name", password, email, branch)
                VALUES (DEFAULT, {}, '{}', '{}', '{}', '{}', '{}');
                """
add_new_teacher = """
                INSERT INTO teachers (teacher_id, name, password, email, department) 
                VALUES (DEFAULT, '{}', '{}', '{}', '{}');
                 """