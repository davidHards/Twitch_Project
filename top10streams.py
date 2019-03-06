import mysql.connector
import csv
import os

os.chdir("E://Users/David/Dropbox/qmul/UG Project query results")

# MYSQL logon
mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="twitch"
)
mycursor = mydb.cursor()


'''
 "SELECT \
    total_views.total_view_count as totalViews, \
    streams.id as ID, \
    streams.game_id as gameID, \
    streams.started_at as startTime, \
    streams.time_stamp as timeStamp \
    FROM total_views \
    JOIN streams ON total_views.id = streams.id \
    JOIN ORDER BY total_view_count DESC LIMIT 10"
'''
# Need to select top 50 results ordered by total_views.total_view_count
# ordered by highest to lowest

sql = "SELECT \
    total_views.total_view_count as totalViews, \
    streams.id as ID, \
    top_games.name as game, \
    streams.started_at as startTime, \
    streams.time_stamp as timeStamp \
    FROM streams \
    JOIN total_views ON total_views.id = streams.id \
    JOIN top_games ON top_games.id = streams.game_id \
    ORDER BY total_view_count DESC LIMIT 10"

mycursor.execute(sql)

myresult = mycursor.fetchall()

index = len(myresult)

with open('top10StreamsGame.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, myresult)
    w.writerow(['totalViews', 'ID', 'gameID', 'startTime', 'timeStamp'])
    for x in myresult:
        w.writerow(x)
