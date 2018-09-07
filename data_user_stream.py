import sqlite3
import os
import sys

conn = sqlite3.connect('stream_data_pluto.sqlite')
cur = conn.cursor()
cur.execute('drop table if exists user')
cur.execute('create table user (user_id TEXT, video_id TEXT, user_name TEXT, comment_date date, comment_content TEXT, PRIMARY KEY (user_id, video_id))')
# year = ['2012','2013','2014','2015','2016']
# year = ['2013']
# for y in year:
#     # write all the file name
#     all_file = os.listdir('I:/VLDBJ_data_v1/' + y + '/')
#     all_file = os.listdir(y + '/')
#     all_file.sort(key=lambda y: y.lower(), reverse=False)
#     with open('file_name_1.txt', 'w') as f:
#         for i in all_file:
#             dong = 1
#             f.write(i)
#             f.write('\n')
#     f.close()
#
#     # read all the file name one by one
#     with open('file_name_1.txt') as f:
#         all_file = f.readlines()
#
#     print('start..')
#     with open('log_1'+y+'.txt','w') as log:
#         log.write(y)
#         log.write('\n')
#         for file in all_file:
#             log.write(file[:-1]+'\n')
#             # with open('I:/VLDBJ_data_v1/'+y+'/'+file[:-1], encoding="utf8") as f:
#             with open( y + '/' + file[:-1], encoding="utf8") as f:
#                 video_id = f.readline().split(':')[1][:-1]
#                 f.readline()
#                 f.readline()
#                 f.readline()
#                 f.readline()
#                 f.readline()
#                 all_comments = f.readlines()
#                 for comment in all_comments:
#                     if len(comment)>10 and ('AuthorChannelId:' in comment.split('\t')[1]) and('Comment:' in comment.split('\t')[2]) and ('PublishAt:' in comment.split('\t')[3]):
#                         user_name = comment.split('\t')[0].split(':')[1]
#                         user_id = comment.split('\t')[1].split(':')[1]
#                         if '{value=' in user_id:
#                             user_id = user_id.split('{value=')[1][:-1]
#                         comment_content = comment.split('\t')[2].split('Comment:')[1]
#                         comment_date = comment.split('\t')[3].split(':')[1]
#                         try:
#                             cur.execute('insert into user (user_id, video_id, user_name, comment_date, comment_content) VALUES(?,?,?,?,?)',(user_id, video_id, user_name, comment_date, comment_content))
#                         except:
#                             a = 1
#                             # log.write('exist\n')
#                 conn.commit()
#             f.close()
#         log.close()

conn.close()

