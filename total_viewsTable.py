import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="David",
    passwd='Sword',
    database="twitch"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE total_views (id BIGINT PRIMARY KEY, total_view_count INT)")
