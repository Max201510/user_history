import sqlite3
import os
import sys

conn = sqlite3.connect('streamRec.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists user_history_number')
# cur.execute('create table user_history_number (user_id TEXT, number INT, PRIMARY KEY (user_id))')
print('start....hhhh.')


user_ids = cur.execute('select user_id from user group by user_id').fetchall()
solider = 0
with open('user_history.txt','w') as f:
    for user_id in user_ids:
        if solider > 0:
            f.write('\n')
        solider = solider + 1
        user = str(user_id[0])
        f.write(user)
        video_ids = cur.execute('select video_id from user where user_id="'+user+'" group by video_id').fetchall()
        f.write(":")
        f.write(str(len(video_ids)))

        f.write(':')
        for video_id in video_ids:
            f.write(video_id[0])
            f.write(':')
        try:
            cur.execute('insert into user_history_number (user_id, number) VALUES(?,?)', (user, len(video_ids)))
        except:
            print('exist')
        conn.commit()
