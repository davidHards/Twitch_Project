'''
Count number of rows in csv files
Date: 24/01/2019
Author: David Hards
This is a helper program that serves no purpose for project. This program
gets number of rows for each csv file, and displays count for how many have
99, 100 or other number of rows.

'''

import glob
import os
import csv

topGames=[]

os.chdir("E://UG Project Data")
for file in glob.glob("*top*"):
    topGames.append(file)

index = len(topGames)
#print(index)
num = 0
theFile = topGames[0]
#print(theFile)
data = []
a = 0
b = 0
c = 0
#for x in range(index):
for x in range(index):
    try:
        theFile = topGames[x]
        with open(theFile) as f:
            reader = csv.reader(f)
            #print(reader)
            next(reader) # skip header
            n = 0
            for row in reader:
                if (num % 2) == 0:
                    pass
                else:
                    data.append(row)
                    #print("yes")
                    n += 1
                num += 1
            if (n == 100):
                a += 1
            elif (n == 99):
                b += 1
            else:
                c += 1
    except:
        print("Problem file:")
        print(theFile)
print(x)
print(len(data))
print(n)
print(a)
print(b)
print(c)
