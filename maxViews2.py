import os
import csv
import re

#os.chdir("D://UG_Project_Data")
os.chdir("E://UG_Project_Data")
id = 0
views = 0

def scan():
    global id
    global views
    id2 = 31448318432
    maxViews = 0
    with open ('viewCount2.csv', encoding='utf-8-sig') as views:
        with open ('maxViews4.csv', 'a', newline='', encoding='utf-8-sig') as output:
            reader = csv.reader(views)
            writer = csv.writer(output, delimiter=',')
            for row in reader:
                id = str(row[0:1])
                id = re.sub('[^0-9]', '', id)
                id = int(id)
                if (id == id2):
                    views = row[1:2]
                    views = str(views)
                    views = re.sub('[^0-9]', '', views)
                    views = int(views)
                    if (views >= maxViews):
                        maxViews = views
                        temp = id, maxViews
                elif (id != id2):
                    writer.writerow(temp)
                    maxViews = 0
                    views = row[1:2]
                    views = str(views)
                    views = re.sub('[^0-9]', '', views)
                    views = int(views)
                    if (views >= maxViews):
                        maxViews = views
                        temp = id, maxViews
                id2 = id
    return

def last():

    with open ('maxViews4.csv', 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output, delimiter=',')
        temp = id, views
        writer.writerow(temp)
    return

if __name__== '__main__':
    scan()
    last()
