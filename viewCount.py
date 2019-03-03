'''
Read CSV files and input data into streams and top_games tables
Date: 24/01/2019
Author: David Hards
This program reads all csv files, stores all the information in a list, the
lists are filtered to remove duplicates and empty rows etc. The lists are then
convered to tuples and the data is inputted into two databases, one for games
and the other for stream data.

'''

import glob
import os
import csv
import mysql.connector

# MYSQL logon
mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="twitch"
)
mycursor = mydb.cursor()

# list for strean data file names
streamData=[]
# list for game data file names
topGames=[]

# This function obtains file name list from a folder, this is to open files in other functions
def getFileNames():
    global streamData
    global topGames

    # the folders to be scanned
    #os.chdir("D://UG_Project_Data")
    os.chdir("E://UG_Project_Data")
    # obtains stream data file names
    for file in glob.glob("*streamD*"):
        streamData.append(file)
    return

sData = []
# List to store stream data from csv files
# Function to read all streamData csv files and store data in a list
def streamsToList():
    global sData
    global streamData
    index = len(streamData)
    num = 0
    theFile = streamData[0]
    print(index)
    for x in range(index):
        if (num == 1000):
            sortList(sData)
            num = 0
            sData.clear()
        try:
            theFile = streamData[x]
            with open (theFile, encoding="utf8") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    if (row != []):
                        col1 = row[0]
                        col8 = row[7]
                        temp = col1, col8
                        sData.append(temp)
        except:
            print("Problem file:")
            print(theFile)
        print(num)
        num += 1
    return

def sortList(self):
    sData = self
    print("A")
    sData = set(sData)
    print("B")
    sData = list(sData)
    print("C")
    sData.sort()
    print("D")
    with open('viewCount2.csv', 'a', newline='', encoding='utf-8-sig') as output:
        writer = csv.writer(output)
        for d in sData:
            writer.writerow(d)

if __name__== '__main__':
    getFileNames()
    streamsToList()
    sortList(sData)
