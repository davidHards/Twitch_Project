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
    os.chdir("D://UG Project Data")
    #os.chdir("E://UG Project Data")
    # obtains stream data file names
    for file in glob.glob("*streamD*"):
        streamData.append(file)
    # obtains game data file names
    for file in glob.glob("*top*"):
        topGames.append(file)
    return

# List to store topGames data from csv files
gData = []

# This function reads all topGames csv files and stores data in a list
def gamesToList():
    global topGames
    global gData

    # index to go through list of topGames
    index = len(topGames)
    # variable to keep track of number of total rows
    num = 0
    # File to open
    theFile = topGames[0]
    for x in range(index):
        try:
            # opens each file in list
            theFile = topGames[x]
            with open(theFile, encoding="utf8") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    gData.append(row)
                    num += 1
        except:
            # reports files that were unable to be read
            print("Problem file:")
            print(theFile)
    # copies gData to another list for purpose of filtering list
    gData2 = list(gData)
    # Removes all empty rows in list
    gData2 = [x for x in gData if x != []]
    # Removes all exact duplicate rows, by converting to set
    dataSet = set(tuple(x) for x in gData2)
    # Converts back to list
    gData = [ list (x) for x in dataSet ]
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
        try:
            theFile = streamData[0]
            with open (theFile, encoding="utf8") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    sData.append(row)
                    num += 1
        except:
            print("Problem file:")
            print(theFile)
    # same as gamesToList, removes empty rows and exact duplicates
    sData = [x for x in sData if x != []]
    sData2 = list(sData)
    dataSet = set(tuple(x) for x in sData2)
    sData = [ list (x) for x in dataSet ]
    # new index of filtered list for purpose of keeping highest view count row
    index = len(sData)
    # this set stores stream id's from the data, ensures no duplicates
    idSet = set()
    try:
        # stores id's of streams
        for x in range(index):
            idSet.add(sData[x][0])
    except:
        # incase of errors
        print("duplicate entry:")
        print(sData[x][0])
    # this empty list will store updated data, no duplicates, no empty rows and entry with highest view count only.
    sData3 = []
    # converts the set of id's to list, for purpose of filtering process
    idList = list(idSet)
    # index of id list
    idIndex = len(idList)
    # for each id in list check sData for all matching id's in sData
    for x in range(idIndex):
        # variable stores id to check
        id = int(idList[x])
        # maxViews resets for each new id
        maxViews = 0
        # the sData to id's to check for match with idList
        for n in range(index):
            id2 = int(sData[n][0])
            # if id's match
            if (id == id2):
                # store view count for that row in views
                views = int(sData[n][7])
                # if the view count is greater than maxViews...
                if (views > maxViews):
                    # ...update maxViews value with views value
                    maxViews = views
                    # for each unique id this variable stores the highest value view count for that id
                    temp = sData[n]
        # This list now contains only one record of each unique stream with the highest view count
        sData3.append(temp)
    # copy to sData for purpose of database creation
    sData = list(sData3)
    return

# Function to create a database of top games data
def createGamesDB():
    global mydb
    global mycursor
    global gData

    tupleList = ()
    for x in gData:
        tupleList = tuple(x)
        sql = "INSERT INTO top_games (id, name, box_art_url) VALUES (%s, %s, %s)"
        val = tupleList
        mycursor.execute(sql, val)
        mydb.commit()
    return

# Function to create a database of stream data
def createStreamDB():
    global mydb
    global mycursor
    global sData

    tupleList = ()
    for x in sData:
        tupleList = tuple(x)
        sql = "INSERT INTO streams (id, user_id, user_name, game_id, community_ids, type, title, viewer_count, started_at, language, thumbnail_url, tag_ids) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = tupleList
        try:
            mycursor.execute(sql, val)
            mydb.commit()
        except:
            print("Error updating this record:")
            print(val)
    return

if __name__== '__main__':
    getFileNames()
    gamesToList()
    streamsToList()
    createGamesDB()
    createStreamDB()
