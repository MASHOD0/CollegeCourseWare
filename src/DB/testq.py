import query as q
import db
 
query = """" """

conn = db.fypDB_Connect()
stud_tuple = db.fetch(conn, )
usn_list = []

for i in range(len(stud_tuple)): usn_list.append(stud_tuple[i][2])

student_id = stud_tuple[5][0]

# for i in range(len(answer)):

#     answer[i][3] = answer[i][3].strftime("%H:%M")
       

# lst = list(map(lambda i : answer[i][0], answer))
#print(lst)
print(student_id)
db.close(conn)

