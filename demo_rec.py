import  sys
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
    for i in range(0,len(rec_2)-1):
        print(str(beixuan[rec_2[i]]) + ',', end='')
    print(str(beixuan[-1])+"', '2018-08-08 23:30:35', NULL);",end='')

index = 0;
# for xx in x:
#
#
#     # print(all_rec[0].split('\n')[0].split(','))
#     rec = all_rec[xx - 1].split('\n')[0].split(',')[15:30]
#     rec_result = [int(i) for i in rec]
#
#     all_video = []
#     for i in range(0, 150):
#         all_video.append(i)
#
#     beixuan = [item for item in all_video if item not in rec_result]
#     # rec_result是15:30的， beixuan是用户没有看过的， 在rec_result里选x%k个，其他里选k-x%k个
#     feature4 = ['1111']
#     feature3 = ['1110', '1101', '1011', '0111']
#     feature2 = ['1100', '1010', '1001', '0110', '0101', '0011']
#     feature1 = ['1000', '0100', '0010', '0001']
#
#     k = [20]
#
#
#     for i in feature4:
#         index = index + 1
#         print("INSERT INTO `ccig` VALUES ("+str(index)+",",end='')
#         print(str(xx)+",", end='\t')
#         print("'"+str(i)+"',",end='\t')
#         for j in k:
#             di = int(j * 0.5)
#             dj = j - di
#             print("'", end='')
#             ccig_rec(di, rec_result, dj, beixuan)
#         print()
#
#
#     for i in feature3:
#         index = index + 1
#         print("INSERT INTO `ccig` VALUES (" + str(index) + ",", end='')
#         print(str(xx) + ",", end='\t')
#         print("'" + str(i) + "',", end='\t')
#         for j in k:
#             di = int(j * 0.4)
#             dj = j - di
#             print("'", end='')
#             ccig_rec(di, rec_result, dj, beixuan)
#         print()
#
#
#     for i in feature2:
#         index = index + 1
#         print("INSERT INTO `ccig` VALUES (" + str(index) + ",", end='')
#         print(str(xx) + ",", end='\t')
#         print("'" + str(i) + "',", end='\t')
#         for j in k:
#             di = int(j * 0.3)
#             dj = j - di
#             print("'", end='')
#             ccig_rec(di, rec_result, dj, beixuan)
#         print()
#
#
#     for i in feature1:
#         index = index + 1
#         print("INSERT INTO `ccig` VALUES (" + str(index) + ",", end='')
#         print(str(xx) + ",", end='\t')
#         print("'" + str(i) + "',", end='\t')
#         for j in k:
#             di = int(j * 0.2)
#             dj = j - di
#             print("'", end='')
#             ccig_rec(di, rec_result, dj, beixuan)
#         print()

video_id = 0
for i in range(1,151):
    print("INSERT INTO `video` VALUES ("+str(i)+", 'test01v', '"+str(i)+".png', '1,2', '2018-08-08 23:30:35', NULL);")