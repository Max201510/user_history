import sqlite3
import os

conn = sqlite3.connect('streamRec.sqlite')
cur = conn.cursor()
# cur.execute('drop table if exists item')
# cur.execute('create table item ('
#             'id TEXT PRIMARY KEY, '
#             'title TEXT, '
#             'category integer, '
#             'publishedAt date, '
#             'description TEXT)')

all_file = os.listdir('I:/VLDBJ_data_v1/2012/')
all_file.sort(reverse=True)
for file in all_file:
    print(file)
    with open('I:/VLDBJ_data_v1/2012/'+file, encoding="utf8") as f:
        id = f.readline().split('title:')[1][:-1]
        title = f.readline().split(':')[1][:-1]
        category = f.readline().split(':')[1]
        publishedAt = f.readline().split(':')[1]
        f.readline()
        description = f.readline().split('description:')[1][:-1]
    f.close()

    try:
        cur.execute('insert into item (id, title, category, publishedAt, description) VALUES(?,?,?,?,?)', (id, title, category, publishedAt, description))
        conn.commit()
    except:
        print('exist')

cur.execute('select * from item')
for row in cur:
    print(row)

conn.close()

