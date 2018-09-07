import sqlite3
import os

conn = sqlite3.connect('test - Copy.sqlite')
cur = conn.cursor()
with open('C:/bitbucket_folder/ccig_demo/videoid.txt') as f:
    all_file = f.readlines()
    for i in range(0,len(all_file)):
        id_int = all_file[i].split('\t')[0]
        id_string = all_file[i].split('\t')[1][:-1]
        # print(str(id_int),end="\t")

        video_id = 0
        title = str(cur.execute('SELECT title FROM item WHERE id = ?', (id_string,)).fetchone()[0])
        newstr = title.replace("'", "")

        print("INSERT INTO `video` VALUES (" + str(id_int) + "," + "'"+newstr+"'" +",'"+  str(id_int) + ".png', '1,2', '2018-08-08 23:30:35', NULL);")
        # print(cur.execute('SELECT title FROM item WHERE id = ?', (id_string,)).fetchone()[0])




# with open('C:/bitbucket_folder/ccig_demo/video_id.txt') as f:
#     all_file = f.readlines()
# for i in all_file:
#     i.splitlines()
#
#
# real_video_id = list(set(all_file))
# list.sort(real_video_id)
#
#
# with open('C:/bitbucket_folder/ccig_demo/data/user5.txt') as userfile:
#     all_user = userfile.readlines()
# print(all_user)
#
# for i in all_user:
#     print(str(real_video_id.index(i))+',',end='')

# conn1 = sqlite3.connect('test - Copy.sqlite')
# cur1 = conn1.cursor()
#
# print(cur1.execute('select title from item where id=?', (test_video_id,)).fetchone())
