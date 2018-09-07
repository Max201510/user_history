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
            print(temp+' is inserted')

tagme.GCUBE_TOKEN = "c76d64d6-b032-46f0-b3ff-cccc5e75e24b-843339462"

conn = sqlite3.connect('stream_data_5.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists entity')
# cur.execute('create table entity (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

with open('file_name_item_2014.txt') as f:
    all_id = f.readlines()
i = 0


for single_id in all_id:
    print(i)
    i = i + 1
    # single_id = single_id[1:-2]
    single_id = single_id[0:11]
    print(single_id)
    single_tex = cur.execute('select id, title, description from item where id=?',(single_id,)).fetchone()
    text = single_tex[1]+' '+single_tex[2]
    ann_insert(text)
print('here')
