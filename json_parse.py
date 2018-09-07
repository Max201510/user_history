import sys
import os
import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

key_words = os.listdir('I:/RMITLinux/workspace/CrawlData/Search_Result/2012/')
key = []
for i in key_words:
    key.append(i.split('.')[0])
time = ['2012','2013','2014','2015','2016']
time = ['2016']

with open('uploader_2016.txt','w',encoding="utf8") as file:

    for k in key_words:
        for t in time:
            path = 'I:/RMITLinux/workspace/CrawlData/Search_Result/'+t+'/'+k+''

            with open(path, encoding="utf8") as f:
                all_line = f.readlines()
                f.close()

            for video in all_line:
                id = video.split('"id":')[1].split('"')[1]
                uploader_title = video.split('"channelTitle":')[1].split('"')[1]
                uploader_id = video.split('"channelId":')[1].split('"')[1]
                try:
                    cur.execute('INSERT INTO uploader (uploader_id, uploader_name, video_id) VALUES(?,?,?)', (uploader_id, uploader_title, id))
                except:
                    file.write(id + '...' + uploader_id + '...' + uploader_title + '\n')
                conn.commit()
                #

