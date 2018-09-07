import sqlite3
import os
import sys
import time

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

for id in range(1,54328):
    print(id)
    entity_name = cur.execute('select name from entity where id=?',(id,)).fetchone()[0]
    name_len = len(entity_name)

    cur.execute('update entity_video set entity_len=? where entity_id=?',(name_len,id))
    conn.commit()
