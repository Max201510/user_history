import os

# open a file
path = 'C:/Users/e18300/Google Drive/part1/2016/'
path = 'I:/VLDBJ_data/2015/'
# path = 'I:/VLDBJ_data/test/'

dirs = os.listdir(path)


# input a line, split by '\t',
def process_line(line):
    if 'Comment:' in line:
        author = ''
        author_id = ''
        author = line.split('\tAuthorChannelId:')[0].split(':')[1]
        x = line.split('\t')
        for y in x:
            if y.startswith('AuthorChannelId:'):
                author_id = y.split(':')[1]
                if author_id.startswith('{value='):
                    author_id = author_id.split('{value=')[1].split('}')[0]
        return author, author_id

dele = set()

# This would print all the files and directories
user_idc = set()
author = ''
author_id = ''

for file in dirs:
    print(file)
    try:
        f = open(path+file, 'r', encoding="utf8")
        line = f.readline() # filter out the first line
        while True:
            line = f.readline()
            if line:
                if 'Comment:' in line:
                    temp = process_line(line)
                    author = temp[0]
                    author_id = temp[1]
                    # print(author, author_id)
                    user_idc.add((author, author_id))
            if not line:
                break
        f.close()
    except ValueError:
        print(path+file)
        dele.add(file)
        print(dele)

# for i in user_idc:
#     print(i)
# print(user_idc)
print(dele)
