import os
year = ['2012','2013','2014','2015','2016']

for y in year:
    all_file = os.listdir('I:/VLDBJ_data_v1/' + y + '/')
    all_file.sort(key=lambda y: y.lower(), reverse=False)

    with open('file_name_item_'+y+'.txt', 'w') as f:
        for i in all_file:
            dong = 1
            f.write(i)
            f.write('\n')
    f.close()

    with open('file_name_user_'+y+'.txt', 'w') as f:
        for i in all_file:
            dong = 1
            f.write(i)
            f.write('\n')
    f.close()