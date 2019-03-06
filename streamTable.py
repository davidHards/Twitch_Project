'''
Create streams table
Date: 24/01/2019
Author: David Hards
This program creates a table called streams in the twitch database, the table
will store a list of streams in the twitch database.

'''

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="David",
    passwd='Sword',
    database="twitch"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE streams (id BIGINT PRIMARY KEY, user_id INT, user_name VARCHAR(255), game_id INT, community_ids VARCHAR(255), type VARCHAR(10), title VARCHAR(255), viewer_count INT, started_at DATETIME, language VARCHAR(5), thumbnail_url VARCHAR(255), tag_ids VARCHAR(255), time_stamp DATETIME)")
