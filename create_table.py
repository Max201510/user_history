import sqlite3
import os

conn = sqlite3.connect('paper_revision.sqlite')
cur = conn.cursor()

# cur.execute('create table entity_entity (id_1 integer, id_2 integer, distance float, PRIMARY KEY (id_1, id_2))')

# cur.execute('create table entity_video (entity_id integer, video_id TEXT, location integer, text_len integer, PRIMARY KEY (entity_id, video_id, location))')

# cur.execute('CREATE TABLE entity (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
#
# cur.execute('create table target_user ('
#             'user_id TEXT PRIMARY KEY, '
#             'user_name TEXT, '
#             'number integer)')
#
# cur.execute('create table user_history_number (user_id TEXT, number Integer)')
#
# # cur.execute('drop table if exists user')
# cur.execute('create table user (user_id TEXT, video_id TEXT, user_name TEXT, comment_date date, comment_content TEXT, PRIMARY KEY (user_id, video_id, user_name, comment_date, comment_content))')
#
# # cur.execute('drop table if exists item')
# cur.execute('create table item ('
#             'id TEXT PRIMARY KEY, '
#             'title TEXT, '
#             'category integer, '
#             'publishedAt date, '
#             'description TEXT)')

# cur.execute('create table paper_coauthor ('
#             'id INTEGER, '
#             'title TEXT, '
#             'sub_time date, '
#             'back_time date, '
#             'score TEXT, '
#             'details TEXT, '
#             'others TEXT)')
