import sqlite3

conn = sqlite3.connect('streamRec.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists entity')
# cur.execute('create table entity (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(15))')

cur.execute('insert into entity (name) VALUES(?)',('au',))
conn.commit()
cur.execute('select * from entity')
for row in cur:
    print(row)

conn.close()

#
# connection=sqlite3.connect(':memory:')
# cursor=connection.cursor()
# cursor.execute('''CREATE TABLE foo (id integer primary key autoincrement ,
#                                     username varchar(50),
#                                     password varchar(50))''')
# cursor.execute('INSERT INTO foo (username,password) VALUES (?,?)',
#                ('test','test'))
# print(cursor.lastrowid)
# #该代码片段来自于: http://www.sharejs.com/codes/go/2328
