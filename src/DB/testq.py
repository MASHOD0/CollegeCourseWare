import query as q
import db

conn = db.fypDB_Connect()
answer = db.fetch(conn, """select course_code from courses;""")
lst = []
for i in range(len(answer)): lst.append(answer[i][0])

# lst = list(map(lambda i : answer[i][0], answer))
print(lst)
db.close(conn)

