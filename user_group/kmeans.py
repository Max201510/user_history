# step 2: group the users accoridng to the 19-d vector into n_clu groups.
# we get a n_clu-d list. Each element in the list means the frequecy he watched this category.
# the result is written in group_result.txt

from sklearn.cluster import KMeans
import numpy as np
import sys
from sklearn import metrics

n = 19200
n_clu = 520

def list_convert(line):
    list_1 = line.strip()[1:-1].split(', ')
    list_2 = [int(i) for i in list_1]
    return list_2

def indices(l, val):
    """Always returns a list containing the indices of val in the_list l"""
    return [index for index, value in enumerate(l) if value == val]

def write_group_result(kmean_label):
    """print each group (user ids) in file: user_group_vector.txt. Each line is a group (with user ids)"""
    with open("user_group_vector1.txt","w") as f:
        for i in range(0, n_clu):
            f.write(str(indices(list(kmeans.labels_), i)))
            f.write('\n')


with open('user_cat_list_bt5.txt') as f:
    content = f.readlines()

print(len(content))

kmeans_vector = []
for number in range(0, n):
    kmeans_vector.append(list_convert(content[number]))
kmeans_array = np.array(kmeans_vector)
print(len(kmeans_vector))

# kmeans = KMeans(n_clusters=2, random_state=0).fit(kmeans_array)
# silhouette_avg = silhouette_score(kmeans_array, kmeans.labels_)
# silhouette_avg =  metrics.silhouette_score(kmeans_array, kmeans.labels_)
# print(2, silhouette_avg)
# sys.exit()

kmeans = KMeans(n_clusters=n_clu, random_state=0).fit(kmeans_array)
# silhouette_avg = metrics.silhouette_score(kmeans_array, kmeans.labels_, metric='euclidean')
# silhouette_avg = silhouette_score(kmeans_array, kmeans.labels_)
# silhouette_avg =  metrics.silhouette_score(kmeans_array, kmeans.labels_)
# print(525, silhouette_avg)

with open('group_result.txt','w') as result:
    result.write(str(list(kmeans.labels_)))

# print each group (user ids) in file: user_group_vector.txt
# write_group_result(kmeans.labels_)
