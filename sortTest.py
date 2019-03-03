'''
id set
Date: 01/03/2019
Author: David Hards

'''

import glob
import os
import csv

def getFileNames():

    # the folders to be scanned
    #os.chdir("D://UG_Project_Data")
    os.chdir("E://UG_Project_Data")
    # obtains stream data file names
    #for file in glob.glob("*streamD*"):
        #streamData.append(file)
    return

def idList():
    id = []
    num = 0
    with open ('idSet.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            if (row != []):
                col1 = row[0]
                id.append(col1)
                #print(col1)
        num +=1
        if (num == 300):
            print("still working!")
            num = 0
    index = len(id)
    #id = list(id)
    idList = []
    for x in range(index):
        number = "1"
        temp = id[x], number
        idList.append(temp)
    idList.sort()
    id.clear()
    for d in idList:
        number = 1
        test = str(d)
        test1 = test[2:13]
        temp = test1, number
        id.append(temp)
        print(test1)

    with open('sortedIds.csv', 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output)
        for row in id:
            writer.writerow(row)

    return

if __name__== '__main__':
    getFileNames()
    idList()
