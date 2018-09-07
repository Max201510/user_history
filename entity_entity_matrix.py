import sqlite3
import os
import sys
import time

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

def distance(location_1, entity_len_1, location_2, entity_len_2, text_len):
    if location_1>location_2:
        # dis = location_1 - location_2 - entity_len_1
        dis = location_1 - location_2
    else:
        # dis = location_2 - location_1 - entity_len_2
        dis = location_2 - location_1
    return dis/text_len
    return dis


def dis_entities(id_1, id_2):
    r_1 = cur.execute('select video_id from entity_video where entity_id=?',(id_1,)).fetchall()
    r_2 = cur.execute('select video_id from entity_video where entity_id=?',(id_2,)).fetchall()
    r_1 = set(r_1)
    r_2 = set(r_2)
    common = r_1 & r_2
    if len(common)>0:
        dis_final = 0
        for video in common:
            video=video[0]
            r_1 = cur.execute('select * from entity_video where entity_id=? and video_id=?', (id_1,video)).fetchall()
            r_2 = cur.execute('select * from entity_video where entity_id=? and video_id=?', (id_2,video)).fetchall()
            dis_ = 0
            for i in r_1:
                for j in r_2:
                    dis_ = dis_ + distance(i[2],i[4],j[2],j[4],j[3])
            dis_ = dis_/(len(r_1)*len(r_2))
            dis_final = dis_final + dis_
        dis_final = dis_final/len(common)
        return dis_final
    else:
        return 1

for x in range(10588,54328):
    for y in range(x+1,54328):
        d = dis_entities(x, y)
        if y%200==0:
            print(x, y, d)
        if d < 1:
            try:
                cur.execute('insert into entity_entity (id_1, id_2, distance) VALUES(?,?,?)',(x, y, d))
            except:
                print('insert faild,',x,y,d)
            conn.commit()

