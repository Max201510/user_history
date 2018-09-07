import tagme
import sqlite3
import sys

def ann_insert(tex):
    textual = tex
    lunch_annotations = tagme.annotate(textual)
    # Print annotations with a score higher than 0.0
    for ann in lunch_annotations.get_annotations(0):
        temp = ann.entity_title
        cur.execute("select count(*) from entity where name=?", (temp,))
        if temp in textual and cur.fetchone()[0]==0: # if it is in description and not in entity table
            cur.execute('insert into entity (name) VALUES(?)', (ann.entity_title,))
            conn.commit()

tagme.GCUBE_TOKEN = "c76d64d6-b032-46f0-b3ff-cccc5e75e24b-843339462"

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists entity')
# cur.execute('create table entity (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

all_tex = cur.execute('select id, title, description from item').fetchall()

i = 0

for single_tex in all_tex:
    print(i)
    print(single_tex)
    i = i+1
    id = single_tex[0]
    print(id)
    text = single_tex[1]+' '+single_tex[2]
    print(text)
    ann_insert(text)
    print('ok')

print('here')
# with open('sample.txt', 'r') as f:
#     textual = f.read()
# f.close()


# cur.execute('select * from entity')
# for row in cur:
#     print(row)
# conn.close()