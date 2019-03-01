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

# list for strean data file names
streamData=[]
# list for game data file names


# This function obtains file name list from a folder, this is to open files in other functions
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
   for x in range(index):
      try:
        theFile = streamData[x]
        with open (theFile, encoding="utf8") as f:
          reader = csv.reader(f)
          next(reader) # skip header
            for row in reader:
              if (row != []):
                        col1 = row[0]
                        id.add(col1)
    except:
        print("Problem file:")
        print(theFile)

    with open('idSet.csv', 'a', newline='', encoding='utf-8-sig') as output:
      writer = csv.writer(output)
      for row in id:
        writer.writerow(row)
     
    return

if __name__== '__main__':
    getFileNames()
    idList()
