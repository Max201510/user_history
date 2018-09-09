# step 1: for each user, get his viewed category history as a 19-d vector. We only maintain the user who has more than 5 videos in his history
# 1   2   10  15  17  19  20  22  23  24  25  26  27  28  29  30  34  43  44
# the result is writtin in the file: user_cat_list5.txt
# user_bt5.txt is the user id and whole frequency
import sqlite3

conn = sqlite3.connect('../test.sqlite')
cur = conn.cursor()

def map(category_frequency):
    a = [1,2,10,15,17,19,20,22,23,24,25,26,27,28,29,30,34,43,44]
    b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0, len(a)):
        for j in range(0, len(category_frequency)):
            if a[i]==category_frequency[j][0]:
                b[i]=category_frequency[j][1]
                break
    return b


all_user = cur.execute('select * from user_history_number where number > 5 order by number DESC').fetchall()

with open('user_cat_list.txt','w') as f:
    with open('user.txt','w') as u:
        for i in range(0, len(all_user)):
            user = all_user[i][0]
            video_number = all_user[i][1]
            print(user, video_number)

            category_frequency = cur.execute('select item.category as category, count(*) from user left join item on (user.video_id=item.id) where user.user_id="'+user+'" group by category').fetchall()
            user_cat_list = map(category_frequency)
            f.write(str(user_cat_list))
            f.write('\n')
            u.write(user+':'+str(video_number))
            u.write('\n')
    f.close()
