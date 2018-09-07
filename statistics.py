import sqlite3
import sys
from itertools import groupby
from numpy import dot
from numpy.linalg import norm

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

def entity_distribution():
    for i in range(1,54328):
        print(i)
        rel = cur.execute('SELECT entity_video.entity_id AS EID, item.category AS CAT,'
                    'count(*) as number FROM entity_video '
                    'INNER JOIN item ON (entity_video.video_id = item.id)'
                    'where entity_video.entity_id =? group by CAT',(i,)).fetchall()

        for j in rel:
            try:
                cur.execute('insert into entity_distribution (EID,CAT,number) VALUES (?,?,?)',(j[0],j[1],j[2]))
            except:
                print(j[0],j[1],j[2])

        conn.commit()

def write_entity_distribution():
    cat = [1,2,10,15,17,19,20,22,23,24,25,26,27,28,29,30,34,43,44]
    with open('entity_distribution.txt','w') as file:
        file.write('entity:\t')
        for c in cat:
            file.write(str(c)+'\t')
        file.write('\n')

        for i in range(1, 54328):
            file.write(str(i)+':\t')
            for j in cat:
                print(i)
                rel = cur.execute('select * from entity_distribution where EID = ? AND CAT = ?',(i,j)).fetchall()
                if rel:
                    file.write(str(rel[0][2])+'\t')
                else:
                    file.write(str(0)+'\t')
            file.write('\n')

def result():
    rel = cur.execute('select EID, count(*) as nn from entity_distribution group by EID order by nn').fetchall()
    lists=[]
    for i in rel:
        lists.append(i[1])

    rel = [len(list(group)) for key, group in groupby(lists)]

    for i in range(1,20):
        print(str(i)+': '+str(rel[i-1]))

def uploader_entity():
    with open('uploader_entity.txt', 'w') as file:
        file.write('uid\tall_number\teid:number')
        rels = cur.execute('select *, count(*) as co from uploader group by uploader_id order by co desc').fetchall()
        for uploader in rels:
            print(uploader[3])
            uid = uploader[0]
            file.write(uid+'\t')
            rel = cur.execute('SELECT	count(*) as co, uploader.uploader_id AS UID,	uploader.video_id AS VID, entity_video.entity_id AS EID '
                        'FROM uploader '
                        'INNER JOIN entity_video ON (entity_video.video_id = uploader.video_id) '
                        'where uploader.uploader_id= ? group by EID order by count(*) desc',(uid,)).fetchall()
            all_number = str(len(rel))
            file.write(all_number+'\t')
            for i in rel:
                eid = str(i[3])
                number = str(i[0])
                file.write(eid+':'+number+'\t')
                print(eid+':'+number+'\t')
            file.write('\n')

# uploader_entity()

def user_cat_vect(uid):
    rel = cur.execute('select count(*) as co, user.user_id, user.video_id, entity_video.entity_id, item.category from user, entity_video, item where user.video_id = entity_video.video_id and item.id = entity_video.video_id and user.user_id=? group by category',(uid,)).fetchall()
    dic={
        "1": 0,"2": 0,"10": 0,
        "15": 0,"17": 0,"19": 0,
        "20": 0,"22": 0,"23": 0,
        "24": 0,"25": 0,"26": 0,
        "27": 0,"28": 0,"29": 0,
        "30": 0,"34": 0,"43": 0,
        "44": 0
    }
    for i in rel:
        cat_fre = i[0]
        category = str(i[4])
        dic[category]=cat_fre
    # print(dic)
    return dic

def user_user(uid_1,uid_2):
    dic_1 = user_cat_vect(uid_1)
    dic_2 = user_cat_vect(uid_2)
    cat = ['1','2','10','15','17','19','20','22','23','24','25','26','27','28','29','30','34','43','44']
    vect_1 = []
    vect_2 = []
    for i in cat:
        vect_1.append(dic_1[i])
        vect_2.append(dic_2[i])
    cos_sim = dot(vect_1, vect_2) / (norm(vect_1) * norm(vect_2))
    print(vect_1)
    print(vect_2)
    print(cos_sim)
    return str(cos_sim)

users = cur.execute('select DISTINCT user_id from target_user').fetchall()
with open('user_vect.txt','w') as file:
    for i in range(69, len(users)):
        uid_1 = users[i][0]
        dic_1 = user_cat_vect(uid_1)
        dic_1 = user_cat_vect(uid_1)
        cat = ['1', '2', '10', '15', '17', '19', '20', '22', '23', '24', '25', '26', '27', '28', '29', '30', '34', '43', '44']
        vect_1 = []
        for i in cat:
            vect_1.append(dic_1[i])
        print(uid_1)
        print(vect_1)

# file.write(uid_1+'\t'+str(vect_1)+'\n')
