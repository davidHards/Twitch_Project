'''
id set
Date: 01/03/2019
Author: David Hards

'''

import glob
import os
import csv

streamData=[]

def getFileNames():
    global streamData

    # the folders to be scanned
    #os.chdir("D://UG_Project_Data")
    os.chdir("E://UG_Project_Data")
    # obtains stream data file names
    for file in glob.glob("*streamD*"):
        streamData.append(file)
    return

def idList():
    global streamData
    id = set()
    index = len(streamData)
    theFile = streamData[0]
    num = 0
    for x in range(index):
        try:
            theFile = streamData[x]
            with open (theFile, encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    if (row != []):
                        col1 = row[0]
                        id.add(col1)
                num +=1
                if (num == 300):
                    print("still working!")
                    num = 0
        except:
            print("Problem file:")
            print(theFile)
    index = len(id)
    id = list(id)
    id.sort()
    idList = []
    for x in range(index):
        number = "1"
        temp = id[x], +","+number
        idList.append(temp)


    with open('idSet2.csv', 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output)
        for row in idList:
            writer.writerow(row)

    return

if __name__== '__main__':
    getFileNames()
    idList()
