import sqlite3
import sys
import math
conn = sqlite3.connect('../test.sqlite')
cur = conn.cursor()

def get_user_id(int_n):
    with open("user_bt5.txt") as f:
        c = f.readlines()
        return c[int_n].split(":")[0]

def user_to_veiwedvideos(user_id):
    """given a user, return his viewed videos as a list, ordered by viewed date"""
    rel = list()
    videos = cur.execute('select * from user where user_id = "' + user_id + '" order by comment_date').fetchall()
    for i in range(0, len(videos)):
        rel.append(videos[i][1])
    return rel

def video_to_entity_list(video_id):
    """given an video_id, return its entity set"""
    rel = []
    entities = cur.execute('select entity.name as name from entity_video left join entity on  (entity_video.entity_id = entity.id) where video_id = "'+video_id+'" group by name').fetchall()
    for i in range(0, len(entities)):
        rel.append(entities[i][0])
    return rel

# calculate the recommendation score between stre_video_id and a specific user say 105
stre_video_id = "xWfTXN0SH7E"
stre_video_cat = 17
hmm_score = 0
official_score = 0
entity_score = 0
rec_score = 0

# third-0, calculate the probability of official_of_stream_video in official_of_video_in_cat
official_of_strem = "UClPfLhtAqK5sJmqAJGxsf3Q"
official_of_video_in_cat = []
with open("./example/official_account.txt") as f:
    fre = 0
    content = f.readlines()
    for i in content:
        if official_of_strem == i.strip():
            fre = fre + 1
    official_score = fre/len(content)
    official_score = math.log10(official_score)

# third-1, calculate the probability of hmm
hmm_score = math.log10(0.78)

# first get the stream item entity list: entitiy_of_stream_video
entitiy_of_stream_video = list(set(video_to_entity_list(stre_video_id)))
print(entitiy_of_stream_video)

# second, get the entitiy list of videos in user's history which category is 17: entities_of_video_in_cat
user_id = get_user_id(105)
history = user_to_veiwedvideos(user_id)
video_in_cat = []
for i in history:
    tmp = cur.execute('select * from item where id = "'+ i + '" and category = 17').fetchall()
    if len(tmp)==1:
        video_in_cat.append(tmp[0][0])
entities_of_video_in_cat = []
for v in video_in_cat:
    all_entity = video_to_entity_list(v)
    entities_of_video_in_cat.extend(all_entity)
print(entities_of_video_in_cat)

# third-2, calculate the probability of entitiy_of_stream_video in entities_of_video_in_cat
def entity_in_list_pro(v, l):
    lens = len(l)
    frequency = 0
    for i in l:
        if v==i:
            frequency = frequency+1
    return frequency/lens
for v in entitiy_of_stream_video:
    entity_score = entity_score + entity_in_list_pro(v, entities_of_video_in_cat)
entity_score = math.log10(entity_score)

rec_score = hmm_score + official_score + rec_score
print(rec_score)


