import sqlite3
import sys

def substring_indexes(substring, string):
    """
    Generate indices of where substring begins in string

    >>> list(find_substring('me', "The cat says meow, meow"))
    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:
            break  # All occurrences have been found
        yield last_found

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()

year = ['2016']

for y in year:
    # read all the file name one by one
    with open('file_name_item_'+y+'.txt') as f:
        all_file = f.readlines()

    print('entity_video start..')

    with open('entity_video_'+y+'.txt','w') as logs:
        logs.write(y)
        logs.write('\n')

        for file in all_file:
            logs.write(file)
            video_id = file.split('.txt')[0]
            rel = cur.execute('select title, description from item where id="'+video_id+'"').fetchone()
            textual = rel[0]+rel[1]
            print(video_id)
            text_len = len(textual)
            # next for all entities to check
            for entity_id in range(1,54328):
                entity_name = cur.execute('select name from entity where id=?',(entity_id,)).fetchone()[0]
                entity_len = len(entity_name)
                location = substring_indexes(entity_name, textual)
                for i in location:
                    try:
                        cur.execute('insert into entity_video (entity_id, video_id, location, text_len, entity_len) VALUES(?,?,?,?,?)',(entity_id,video_id,i,text_len,entity_len))
                    except:
                        print('insert into entity_video (entity_id, video_id, location, text_len, entity_len)',
                              entity_id, video_id, i, text_len, entity_len)
                        print('something is wrong')
            conn.commit()
conn.close()

