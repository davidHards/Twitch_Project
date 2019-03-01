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
        streamsToList(file)
    return

# List to store stream data from csv files
# Function to read all streamData csv files and store data in a list
def streamsToList(self):
    try:
        theFile = self
        timestamp = theFile[0:15]
        dateTime = timestamp[4:8]+"-"+timestamp[2:4]+"-"+timestamp[0:2]+"T"+timestamp[9:11]+":"+timestamp[11:13]+":"+timestamp[13:15]+"Z"
        with open (theFile, encoding="utf8") as f:
            with open('viewCount.csv', 'a', newline='', encoding='utf-8-sig') as output:
                reader = csv.reader(f)
                next(reader) # skip header
                writer = csv.writer(output)
                for row in reader:
                    if (row != []):
                        col1 = row[0]
                        col8 = row[7]
                        col13 = dateTime
                        temp = col1, col8, col13
                        writer.writerow(temp)
    except:
        print("Problem file:")
        print(theFile)

    return

if __name__== '__main__':
    getFileNames()
