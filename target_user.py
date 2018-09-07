import sqlite3
import os
import sys
import time
timestr = time.strftime("%Y%m%d_%H%M%S")

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

# cur.execute('drop table if exists user_history_number')
# cur.execute('create table user_history_number (user_id TEXT, number INT, PRIMARY KEY (user_id))')
print('user history.')

# user_ids = cur.execute('select user_id from user group by user_id').fetchall()
solider = 0


with open('target_user_2016.txt') as target_user:
    line = target_user.readlines()
    for item in line:
        user_id = item.split('"')[1]
        number = item.split('"')[3]
        print(user_id)
        print(number)
        user_name = cur.execute('select user_name from user where user_id ="' + user_id +'"').fetchone()[0]
        print(user_name)
        cur.execute('insert into target_user (user_id, user_name, number) VALUES(?,?,?)', (user_id, user_name, number))
        conn.commit()

