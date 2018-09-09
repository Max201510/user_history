from sklearn.cluster import KMeans
import numpy as np
import sys
from sklearn import metrics

def list_convert(line):
    list_1 = line.strip()[1:-1].split(', ')
    list_2 = [int(i) for i in list_1]
    return list_2


with open('user_cat_list_bt5.txt') as f:
    content = f.readlines()

print(len(content))
n = 19290
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

for i in range(2, n):
    # print(i)
    kmeans = KMeans(n_clusters=i, random_state=0).fit(kmeans_array)
    silhouette_avg = metrics.silhouette_score(kmeans_array, kmeans.labels_, metric='euclidean')
    # silhouette_avg = silhouette_score(kmeans_array, kmeans.labels_)
    # silhouette_avg =  metrics.silhouette_score(kmeans_array, kmeans.labels_)
    print(i, silhouette_avg)


with open('group_result.txt','w') as result:
    result.write(str(list(kmeans.labels_)))
