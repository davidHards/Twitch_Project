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

os.chdir("E://UG_Project_Data")
data = []
with open ('maxViews4.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        col1 = row[0]
        col2 = row[1]
        temp = col1, col2
        #print(temp)
        data.append(temp)

print(data[3][0])
print(data[3][1])

tuplelist = ()
for x in data:
    tuplelist = tuple(x)
    sql = "INSERT INTO total_views (id, total_view_count) VALUES (%s, %s)"
    val = tuplelist
    try:
        mycursor.execute(sql, val)
    except:
        # do some thing
        pass
try:
    mydb.commit()
except:
    pass
