'''
Read CSV files and input data into streams table
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

# List to store stream data from csv files
sData = []
# Function to read all streamData csv files and store data in a list
def streamsToList():
    global streamData
    global sData

    # Same as gamesToList
    index = len(streamData)
    num = 0
    theFile = streamData[0]
    for x in range(index):
        if (num == 301):
            filterStreams(sData)
            num = 0
            sData.clear()
        try:
            theFile = streamData[x]
            timestamp = theFile[0:15]
            dateTime = timestamp[4:8]+"-"+timestamp[2:4]+"-"+timestamp[0:2]+"T"+timestamp[9:11]+":"+timestamp[11:13]+":"+timestamp[13:15]+"Z"
            with open (theFile, encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    if (row != []):
                        col1 = row[0]
                        col2 = row[1]
                        col3 = row[2]
                        col4 = row[3]
                        col5 = row[4]
                        col6 = row[5]
                        col7 = row[6]
                        col8 = row[7]
                        col9 = row[8]
                        col10 = row[9]
                        col11 = row[10]
                        col12 = row[11]
                        col13 = dateTime
                        temp = col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13
                        sData.append(temp)
        except:
            print("Problem file:")
            print(theFile)
        print(num)
        num +=1
    return

def filterStreams(self):
    sData = self
    dataSet = set(tuple(x) for x in sData)
    sData = [ list (x) for x in dataSet ]
    return createStreamDB(sData)

# Function to create a table of stream data
def createStreamDB(self):
    global mydb
    global mycursor
    sData = self
    tupleList = ()
    for x in sData:
        tupleList = tuple(x)
        sql = "INSERT INTO streams (id, user_id, user_name, game_id, community_ids, type, title, viewer_count, started_at, language, thumbnail_url, tag_ids, time_stamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = tupleList
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            test = 1
    return

if __name__== '__main__':
    getFileNames()
    streamsToList()
    filterStreams(sData)
