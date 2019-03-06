import mysql.connector
import csv

# MYSQL logon
mydb = mysql.connector.connect(
  host="localhost",
  user="David",
  passwd="Sword",
  database="twitch"
)
mycursor = mydb.cursor()

# Selects all games, from top_games, selects view count from streams, joins these
# two tables via top_games id and streams game_id.
sql = "SELECT \
    top_games.name AS game, \
    streams.viewer_count AS views \
    FROM top_games \
    JOIN streams ON top_games.id = streams.game_id"

mycursor.execute(sql)
# results
myresult = mycursor.fetchall()
# index of stream data
streamIndex = len(myresult)
# the following 4 lines collect a list of all games ensuring no duplicates
games = set()
for x in range(streamIndex):
    games.add(myresult[x][0])
games = list(games)
# game index
gameIndex = len(games)
# new list to be created, a list of each unique
gameTotalViews = []
for x in range(gameIndex):
    game = str(games[x])
    totalViews = 0
    for n in range(streamIndex):
        game2 = str(myresult[n][0])
        # checks for all games of same name, adds up their view count.
        if (game in game2):
            views = myresult[n][1]
            totalViews = totalViews + views
    temp = game, totalViews
    # creates new list each unique game has it's total view count
    gameTotalViews.append(temp)

with open('streamViewCount.csv', 'w', encoding='utf-8-sig') as f:
    w = csv.writer(f, gameTotalViews)
    w.writerow(['game', 'total_views'])
    for x in gameTotalViews:
        w.writerow(x)
