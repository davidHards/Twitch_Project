'''
Create top_games table
Date: 24/01/2019
Author: David Hards
This program creates a table called top_games in the twitch database, the table
will store a list of games that are streamed on twitch.

'''

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="David",
    passwd='Sword',
    database="twitch"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE top_games (id INT PRIMARY KEY, name VARCHAR(255), box_art_url VARCHAR(255))")
