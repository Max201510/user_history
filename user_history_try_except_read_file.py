import sqlite3
import os
import sys
import time
timestr = time.strftime("%Y%m%d_%H%M%S")

conn = sqlite3.connect('stream_data_5.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists user_history_number')
# cur.execute('create table user_history_number (user_id TEXT, number INT, PRIMARY KEY (user_id))')
print('user history.')

# user_ids = cur.execute('select user_id from user group by user_id').fetchall()
solider = 0

with open('user_history'+'_'+timestr+'.txt','w') as f:
    with open('us.txt') as all_user:
        line = all_user.readlines()
        for user_id in line:
            user_id = user_id[0:-1]
            print(user_id)

            # for user_id in user_ids:
            if solider > 0:
                f.write('\n')
            solider = solider + 1
            # user = str(user_id[0])
            f.write(user_id)
            video_ids = cur.execute('select video_id from user where user_id="'+user_id+'" group by video_id').fetchall()
            f.write(":")
            f.write(str(len(video_ids)))

            f.write(':')
            for video_id in video_ids:
                f.write(video_id[0])
                f.write(':')
            try:
                cur.execute('insert into user_history_number (user_id, number) VALUES(?,?)', (user_id, len(video_ids)))
            except:
                print('exist')
        conn.commit()
