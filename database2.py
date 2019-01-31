'''
Database creation program
Date: 24/01/2019
Author: David Hards


'''

import glob
import os
import csv
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="twitch"
)
mycursor = mydb.cursor()

streamData=[]
topGames=[]

def getFileNames():
    global streamData
    global topGames
    os.chdir("D://UG Project Data")
    #os.chdir("E://UG Project Data")
    for file in glob.glob("*streamD*"):
        streamData.append(file)
    for file in glob.glob("*top*"):
        topGames.append(file)
    return

gData = []

def gamesToList():
    global topGames
    global gData

    index = len(topGames)
    num = 0
    theFile = topGames[0]
    for x in range(index):
        try:
            theFile = topGames[x]
            with open(theFile, encoding="utf8") as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    gData.append(row)
                    num += 1
        except:
            print("Problem file:")
            print(theFile)
    data2 = list(gData)
    data2 = [x for x in gData if x != []]
    dataSet = set(tuple(x) for x in data2)
    gData = [ list (x) for x in dataSet ]
    return

sData = []

def streamsToList():
    global streamData
    global sData

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
    sData = [x for x in sData if x != []]
    data2 = list(sData)
    dataSet = set(tuple(x) for x in data2)
    sData = [ list (x) for x in dataSet ]
    index = len(sData)
    idSet = set()
    try:
        for x in range(index):
            idSet.add(sData[x][0])
    except:
        print("duplicate entry:")
        print(sData[x][0])
    sData2 = []
    idList = list(idSet)
    idIndex = len(idList)
    for x in range(idIndex):
        id = int(idList[x])
        maxViews = 0
        for n in range(index):
            id2 = int(sData[n][0])
            if (id == id2):
                views = int(sData[n][7])
                if (views > maxViews):
                    maxViews = views
                    temp = sData[n]
        sData2.append(temp)
    sData = list(sData2)
    return

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

def createStreamDB():
    global mydb
    global mycursor
    global sData

    tupleList = ()
    for x in sData:
        tupleList = tuple(x)
        sql = "INSERT INTO streams1 (id, user_id, user_name, game_id, community_ids, type, title, viewer_count, started_at, language, thumbnail_url, tag_ids) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
