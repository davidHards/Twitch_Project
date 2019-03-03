import os
import csv
import re

os.chdir("E://UG_Project_Data")

with open ('sortedIds.csv', encoding='utf-8-sig') as ids:
    with open ('viewCount.csv', encoding='utf-8-sig') as views:
        with open ('maxViews.csv', 'a', newline='', encoding='utf-8-sig') as output:
            reader1 = csv.reader(ids)
            reader2 = csv.reader(views)
            next(reader2)
            writer = csv.writer(output)
            for row1 in reader1:
                id1 = int(row1[0])
                maxViews = 0
                for row2 in reader2:
                    id2 = str(row2[0:1])
                    id2 = re.sub('[^0-9]', '', id2)
                    id2 = int(id2)
                    print(id1, id2)
                    if (id1 == id2):
                        print("success")
                        views = row2[1:2]
                        views = str(views)
                        views = re.sub('[^0-9]', '', views)
                        views = int(views)
                        if (views > maxViews):
                            maxViews = views
                            temp = id1, maxViews
                writer.writerow(temp)
