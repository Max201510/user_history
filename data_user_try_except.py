import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

year = ['2013','2014','2015','2016']
year = ['2016']
import time
timestr = time.strftime("%Y%m%d_%H%M%S")
for y in year:
    # read all the file name one by one
    with open('file_name_user_'+y+'.txt') as f:
        all_file = f.readlines()

    print(y + ' user start..')

    with open('logs_user_'+y+'_'+timestr+'.txt','w') as logs:
        logs.write(y)
        logs.write('\n')

        for file in all_file:
            logs.write(file)
            # with open('I:/VLDBJ_data_v1/'+y+'/'+file, encoding="utf8") as f:
            with open('I:/VLDBJ_data_v1/' + y + '/' + file[:-1], encoding="utf8") as f:
                video_id = f.readline().split(':')[1][:-1]
                f.readline()
                f.readline()
                f.readline()
                f.readline()
                f.readline()
                all_comments = f.readlines()
                for comment in all_comments:
                    # print(comment)
                    try:
                        if len(comment)>10 and ('AuthorChannelId:' in comment.split('\t')[1]) and('Comment:' in comment.split('\t')[2]) and ('PublishAt:' in comment.split('\t')[3]):
                            user_name = comment.split('\t')[0].split(':')[1]
                            user_id = comment.split('\t')[1].split(':')[1]
                            if '{value=' in user_id:
                                user_id = user_id.split('{value=')[1][:-1]
                            comment_content = comment.split('\t')[2].split('Comment:')[1]
                            comment_date = comment.split('\t')[3].split(':')[1]
                            try:
                                cur.execute('insert into user (user_id, video_id, user_name, comment_date, comment_content) VALUES(?,?,?,?,?)',(user_id, video_id, user_name, comment_date, comment_content))
                            except:
                                a = 1
                                # log.write('exist\n')
                    except:
                        a=1
                conn.commit()
            f.close()
        logs.close()

conn.close()

