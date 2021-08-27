import query as q
import db

conn = db.fypDB_Connect()
answer = db.fetch(conn, q.get_classes.format('1DS20CS121', 'Sunday'))

for i in range(len(answer)):
    print(answer[0][i])

db.close(conn)
