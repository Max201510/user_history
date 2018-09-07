with open('C:/bitbucket_folder/ccig_demo/user_view_history.txt') as recfile:
    all_rec = recfile.readlines()
x = [1,2,3,4,5]
import random
def ccig_rec(di, rec_result, dj,beixuan):
    len_rec_result = len(rec_result)
    len_beixuan_result = len(beixuan)
    rec_1 = random.sample(range(0, len_rec_result), di)
    rec_2 = random.sample(range(0, len_beixuan_result), dj)
    for i in rec_1:
        print(str(rec_result[i])+',',end='')
    for i in rec_2:
        print(str(beixuan[i])+',',end='')
    # print()

for xx in x:
    # print(all_rec[0].split('\n')[0].split(','))
    rec = all_rec[xx - 1].split('\n')[0].split(',')[15:30]
    rec_result = [int(i) for i in rec]

    all_video = []
    for i in range(0, 150):
        all_video.append(i)

    beixuan = [item for item in all_video if item not in rec_result]
    # rec_result是15:30的， beixuan是用户没有看过的， 在rec_result里选x%k个，其他里选k-x%k个


    k = [3, 5, 10, 20]



    print(xx, end='\t')
    for j in k:
        di = int(j * 0.25)
        dj = j - di
        ccig_rec(di, rec_result, dj, beixuan)
    print()
