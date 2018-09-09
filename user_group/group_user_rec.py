# given a group and an incoming item, calculate the rec score.

import sqlite3
conn = sqlite3.connect('../test.sqlite')
cur = conn.cursor()

def get_user_id(int_n):
    with open("user_bt5.txt") as f:
        c = f.readlines()
        return c[int_n].split(":")[0]

def video_to_entity_set(video_id):
    """given an video_id, return its entity set"""
    rel = set()
    entities = cur.execute('select entity.name as name from entity_video left join entity on  (entity_video.entity_id = entity.id) where video_id = "'+video_id+'" group by name').fetchall()
    for i in range(0, len(entities)):
        rel.add(entities[i][0])
    return rel

def user_to_veiwedvideos(user_id):
    """given a user, return his viewed videos as a list, ordered by viewed date"""
    rel = list()
    videos = cur.execute('select * from user where user_id = "'+user_id+'" order by comment_date').fetchall()
    for i in range(0, len(videos)):
        rel.append(videos[i][1])
    return rel


group = [105, 109, 149, 163, 236, 254, 261]

group_entities = set()

# get group entities and write it into group_entities.txt
for i in group:
    user_id = get_user_id(i)
    video_list = user_to_veiwedvideos(user_id)
    print(video_list)
    for v in video_list:
        group_entities = group_entities.union(video_to_entity_set(v))
with open("./example/group_entities.txt","w") as f:
    for i in group_entities:
        f.write(i)
        f.write('\n')

