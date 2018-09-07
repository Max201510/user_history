import sqlite3

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

year = ['2016']

for y in year:
    # read all the file name one by one
    with open('file_name_item_'+y+'.txt') as f:
        all_file = f.readlines()

    print('item start..')

    with open('logs_item_'+y+'.txt','w') as logs:
        logs.write(y)
        logs.write('\n')

        for file in all_file:
            logs.write(file)
            with open('I:/VLDBJ_data_v1/'+y+'/'+file[:-1], encoding="utf8") as f:
                id = f.readline().split(':')[1][:-1]
                title = f.readline().split('title:')[1][:-1]
                category = f.readline().split(':')[1]
                publishedAt = f.readline().split('publishedAt:')[1]
                f.readline()
                description = f.readline().split('description:')[1][:-1]
            f.close()

            try:
                cur.execute('insert into item (id, title, category, publishedAt, description) VALUES(?,?,?,?,?)', (id, title, category, publishedAt, description))
                conn.commit()
            except:
                print('exist')

conn.close()

