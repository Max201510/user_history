# # Pythono3 code to rename multiple
# # files in a directory or folder
#
# # importing os module
# import os
#
#
# # Function to rename multiple files
# def main():
#     i = 1
#
#     for filename in os.listdir("C:/bitbucket_folder/ccig_demo/CCIGDemo3/src/main/resources/static/images/video/"):
#         dst = "" + str(i) + ".png"
#         src = 'C:/bitbucket_folder/ccig_demo/CCIGDemo3/src/main/resources/static/images/video/' + filename
#         dst = 'C:/bitbucket_folder/ccig_demo/CCIGDemo3/src/main/resources/static/images/video/' + dst
#
#         # rename() function will
#         # rename all the files
#         os.rename(src, dst)
#         i += 1
#
#
# # Driver Code
# if __name__ == '__main__':
#     # Calling main() function
#     main()

import urllib.request
with open('C:/bitbucket_folder/ccig_demo/videoid.txt') as f:
    all_file = f.readlines()
    for i in range(0,len(all_file)):
        id_int = all_file[i].split('\t')[0]
        id_string = all_file[i].split('\t')[1][:-1]
        name = "C:/bitbucket_folder/ccig_demo/CCIGDemo3/src/main/resources/static/images/video/"+str(id_int)+".png"
        urllib.request.urlretrieve("https://img.youtube.com/vi/"+id_string+"/hqdefault.jpg", name)

