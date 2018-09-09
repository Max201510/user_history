# import os

# open a file
# path = 'I:/VLDBJ_data/2014/'
# delet = {'jmJjEWH9VO8.txt'}
# for i in delet:
#     os.remove(path+i)
# x = 0.045 * 75.89 + 0.621 * 4 + 88.923
# print(x)

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-100, 1, 100)
# print(x)
# y = 1/(1+np.exp(x))
# y = np.exp(x)
# plt.plot(x,y)
# plt.xlabel('$x$')
# plt.ylabel('$exp(x)$')
# plt.show()

# x=[0.228 , 0.389 , 0.401  , 0.452]
# y=[0.248 , 0.396 , 0.411  , 0.460]
# m = 0
# for i in range(0,4):
#     m=m+(y[i]-x[i])/x[i]
# print(m/4)
#
# s = 'Author:Tanisha Crutch	AuthorChannelId:UClaGA6Q4gcH5w6LGwApYA4g	Comment:I still love this song to this day	PublishAt:2015-04-11T16:39:01.000Z'
# print(len(s))
# print(s)
# user_id = s.split('Author:')[0]
# print(user_id)

# y='2012'
# all_file = os.listdir('I:/VLDBJ_data_v1/'+y+'/')
# all_file.sort(key=lambda y: y.lower(),reverse=False)
# with open('file_name.txt','w') as f:
#     for i in all_file:
#         f.write(i)
#         f.write('\n')



# import sqlite3
# import os
# import sys

# conn = sqlite3.connect('streamRec.sqlite')
# cur = conn.cursor()
# with open('I:/VLDBJ_data_v1/category.txt') as f:
#     all_file = f.readlines()

# for category in all_file:
#     id = category.split('\t')[0]
#     print(id)
#     name = category.split('\t')[1][:-1]
#     print(name)
#     cur.execute('insert into category (id, name) VALUES(?,?)',(id, name))
#     conn.commit()
# conn.close()
#
# with open('c:/pycharmPro/user_history/2014.txt') as f:
#     all_file_1 = f.readlines()
# with open('c:/pycharmPro/user_history/file_name_item_2014.txt') as f:
#     all_file_2 = f.readlines()

# for i in all_file_1:
    # s2016 = i[1:12]
    # s2016 = s2016+'.txt\n'
    # if s2016 not in all_file_2:
    #     print(s2016)

# print(all_file_1)
# for i in all_file_2:
#     s2016 = "\""+i[0:11]+"\"\\n"
#     if s2016 not in all_file_1:
#         print(s2016)
# a=[]
# for file in all_file_1:
#     a.append(file[1:12])
# print(len(a))
# a.sort()
#
# b=[]
# for file in all_file_2:
#     b.append(file[0:11])
# b.sort()
# print(len(b))

# for file in a:
#     if file not in b:
#         print(file)

# with open('testtest.txt','w') as f:
#     for i in range(0,157838):
#         f.write(a[i]+'\t'+b[i])
#         f.write('\n')

#
# for i in range(0,157838):
#     if a[i]!=b[i]:
#         print(i)
#         print(a[i])

# import sqlite3
#
# conn = sqlite3.connect('stream_data_5.sqlite')
# cur = conn.cursor()
# print('st...')
# res = cur.execute('select count(*) from user')
# print(res)

# import time
# timestr = time.strftime("%Y%m%d_%H%M%S")
# with open('test_'+timestr+'.txt','w') as f:
#     f.write('x')
# print(timestr)

# import sqlite3
#
# conn = sqlite3.connect('stream_data_5.sqlite')
# cur = conn.cursor()
# result = cur.execute('select * from user_history_number order by number').fetchall()
# for i in result:
#     print(i)
# with open('user_name.txt','w') as file:
#
#     with open('user_history.txt') as f:
#         while(True):
#             file.write(f.readline().split(':')[0])

# conn = sqlite3.connect('stream_data_5.sqlite')
# cur = conn.cursor()
# # cur.execute("select count(*) from entity where name=?", (temp,))
# result = cur.execute('select user_id from user group by user_id').fetchall()
# with open('user_name_all.txt','w') as f:
#     for i in result:
#         f.write(str(i[0]))
# all=8,700,746
# with open('us.txt','w') as file:
#     with open('user_name_all.txt') as f:
#         line = f.readline()
#         # lens = 27,287,918
#         print(len(line)/24)
#         for i in range(all, 27287919):
#             file.write(line[24*i:24*(i+1)])
#             file.write('\n')
#             print(i)

# import sqlite3
# import os
# import sys
# import time
# timestr = time.strftime("%Y%m%d_%H%M%S")
#
# conn = sqlite3.connect('stream_data_5.sqlite')
# cur = conn.cursor()
#
# # cur.execute('drop table if exists user_history_number')
# # cur.execute('create table user_history_number (user_id TEXT, number INT, PRIMARY KEY (user_id))')
# print('user history.')
#
# # user_ids = cur.execute('select user_id from user group by user_id').fetchall()
# solider = 0
#
#
# with open('entity_2016.txt', encoding="utf8") as target_user:
#     line = target_user.readlines()
#     for item in line:
#         user_id = item.split('"')[1]
#         number = item.split('"')[3]
#         print(user_id)
#         print(number)
#         cur.execute('insert into entity (id, name) VALUES(?,?)', (user_id, number))
#         conn.commit()

# for i in range(1,4):
#     print(i)

import sqlite3
import os
import sys
import time

# conn = sqlite3.connect('test.sqlite')
# cur = conn.cursor()
#
# def distance(location_1, entity_len_1, location_2, entity_len_2, text_len):
#     if location_1>location_2:
#         # dis = location_1 - location_2 - entity_len_1
#         dis = location_1 - location_2
#     else:
#         # dis = location_2 - location_1 - entity_len_2
#         dis = location_2 - location_1
#     return dis/text_len
#     return dis
#
#
# def dis_entities(id_1, id_2):
#     r_1 = cur.execute('select video_id from entity_video where entity_id=?',(id_1,)).fetchall()
#     r_2 = cur.execute('select video_id from entity_video where entity_id=?',(id_2,)).fetchall()
#     r_1 = set(r_1)
#     r_2 = set(r_2)
#     common = r_1 & r_2
#     if len(common)>0:
#         dis_final = 0
#         for video in common:
#             video=video[0]
#             r_1 = cur.execute('select * from entity_video where entity_id=? and video_id=?', (id_1,video)).fetchall()
#             r_2 = cur.execute('select * from entity_video where entity_id=? and video_id=?', (id_2,video)).fetchall()
#             dis_ = 0
#             for i in r_1:
#                 for j in r_2:
#                     dis_ = dis_ + distance(i[2],i[4],j[2],j[4],j[3])
#             dis_ = dis_/(len(r_1)*len(r_2))
#             dis_final = dis_final + dis_
#         dis_final = dis_final/len(common)
#         return dis_final
#     else:
#         return 1

# for x in range(1,54328):
#     for y in range(x+1,54328):
#         d = dis_entities(x, y)
#         print(x, y, d)
        # cur.execute('insert into entity_entity (id_1, id_2, distance) VALUES(?,?,?)',(x, y, d))
        # conn.commit()

# a = [1,2,3,4]
# a = set(a)
# b = [2,3,4,5]
# b = set(b)
# print(a & b)
# from numpy.linalg import norm
# from itertools import groupby
# from numpy import dot
#
# vect_1 = [1,2,3]
# print(norm(vect_1)*norm(vect_1))
#
# with open('vector.txt') as file:
#     with open('u_u_sim.txt','w') as f:
#         rel = file.readlines()
#         for index in range(0,len(rel)):
#             for index_y in range(index+1, len(rel)):
#
#                 f.write(rel[index].split('\t')[0] + '\t')
#                 f.write(rel[index_y].split('\t')[0] + '\t')
#                 print(rel[index].split('\t')[0] + '\t')
#                 print(rel[index_y].split('\t')[0] + '\t')
#
#                 v = rel[index].split('\t')[1][1:-2].split(', ')
#                 vec = []
#                 for i in range(0,len(v)):
#                     vec.append(int(v[i]))
#
#                 v_y = rel[index_y].split('\t')[1][1:-2].split(', ')
#                 vec_y = []
#                 for i in range(0, len(v_y)):
#                     vec_y.append(int(v_y[i]))
#
#                 f.write(str(dot(vec, vec_y) / (norm(vec) * norm(vec_y)))+'\n')
#                 print(dot(vec, vec_y) / (norm(vec) * norm(vec_y)))
#
# i=0
# for a in range(0,11):
#     for b in range(0, 11):
#         for c in range(0, 11):
#             for d in range(0, 11):
#                 for e in range(0, 11):
#                     for f in range(0, 11):
#                         if a+b+c+d+e+f == 10:
#                             i=i+1
#                             print(str(i)+": "+str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f)+" ")
#
# from scipy.special import comb, perm
# print(comb(11,5) +comb(11,4)+comb(11,3)+ comb(11,2) + comb(11,1))
#
# import tensorflow as tf
# from collections import defaultdict
# top_n = defaultdict(list)
# top_n[1].append((1,3))
# top_n[1].append((1,2))
# top_n[2].append((1,3))
# top_n[2].append((1,2))
# print(top_n.items())
# print(top_n)
#
# food_list = 'spam spam spam spam spam spam eggs spam'.split()
# food_count = defaultdict(int) # default value of int is 0
# for food in food_list:
#     food_count[food] += 1  # increment element's value by 1
# print(food_count)

# import time
# def countdown(n):
#     while n>0:
#         print(n)
#         n = n-1
#         if n==0:
#             print('kk')
#
# countdown(50)
# from random import randint
#
# a = [
# 0.00674944,
# 0.00620624,
# 0.00590595,
# 0.00588457,
# 0.00588636
# ]
#
# b = [0.0001,0.00013,.00015]
#
# for i in a:
#     index = randint(0, 2)
#     print(i+b[index])
# total_number = 2000
# set_size = int(total_number/2)
# print(set_size)
# test = set(range(1,total_number+1))
# # print(test)
#
# distribution = [0]*(set_size+1)
#
# import random
# rounds = 100000
# for i in range(1,rounds):
#     # print(i)
#     x = set(random.sample(range(1, total_number), set_size))
#     y = set(random.sample(range(1, total_number), set_size))
#     overlap = x.intersection(y)
#     # print(x)
#     # print(y)
#     # print(overlap)
#     # print(len(overlap))
#     distribution[len(overlap)] += 1
# new_distribution = [x/(rounds-1) for x in distribution[1:]]
# # print(new_distribution)
# import matplotlib.pyplot as plt;
# import numpy as np
# plt.bar(np.arange(len(new_distribution)), new_distribution)
# plt.show()

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0],[7,0],[7,2],[7,4]])
for i in range(2, 6):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(X)
    print(kmeans.labels_)
    silhouette_avg = silhouette_score(X, kmeans.labels_)
    print(silhouette_avg)