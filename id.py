'''
id set
Date: 01/03/2019
Author: David Hards

'''

import glob
import os
import csv
import os.path

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

idList=[]

def idLists():
    global idList
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

    for x in range(index):
        number = 1
        temp = id[x], number
        print(temp)
        idList.append(temp)

    return

counter = 0
index = len(idList)
def writeFile(self):
    global idList
    global counter
    num = 0
    completeName = self
    with open(completeName, 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output)
        for x in range(index):
            if (num == 100):
                nun = 0
                newFile()
                index = index - counter
            writer.writerow(idList[counter])
            num += 1
            counter += 1

    return

x = 0
def newFile():
    global x
    x += 1
    path = 'E:/UG_Project_Data/ID/'
    file = 'ids' + x
    completeName = os.path.join(path, file + ".csv")
    return writeFile(completeName)

if __name__== '__main__':
    getFileNames()
    idLists()
    newFile()
