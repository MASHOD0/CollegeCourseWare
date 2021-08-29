import query as q
import db
 


conn = db.fypDB_Connect()
answer = db.fetch(conn, """select class_id,classes.course_id, "link", "time", courses.course_code, department from classes join courses ON classes.course_id = courses.course_id where section_id = (select section_id from student where "USN" = '1DS20CS171' limit 1) AND day = 'Sunday';""")

for i in range(len(answer)):

    answer[i][3] = answer[i][3].strftime("%H:%M")
       

# lst = list(map(lambda i : answer[i][0], answer))
print(lst)
db.close(conn)

