import os
import csv
import re

os.chdir("E://UG_Project_Data")
header = ['id', 'views']
with open ('sortedIds.csv', encoding='utf-8-sig') as ids:
    with open ('maxViews.csv', 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerow(header)
        reader1 = csv.reader(ids)
        for row1 in reader1:
            id1 = int(row1[0])
            maxViews = 0
            print(id1)
            with open ('viewCount2.csv', encoding='utf-8-sig') as views:
                reader2 = csv.reader(views)
                num = 0
                for row2 in reader2:
                    if (num == 10000000):
                        num = 0
                        print("Still working!")
                    id2 = str(row2[0:1])
                    id2 = re.sub('[^0-9]', '', id2)
                    id2 = int(id2)
                    num += 1
                    if (id1 == id2):
                        views = row2[1:2]
                        views = str(views)
                        views = re.sub('[^0-9]', '', views)
                        views = int(views)
                        if (views > maxViews):
                            maxViews = views
                            temp = id1, maxViews
            writer.writerow(temp)
