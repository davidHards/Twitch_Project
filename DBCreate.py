'''
Database creation program
Date: 24/01/2019
Author: David Hards
This program creates a database called twitch, to store tables for project.

'''

# creates twitch DB
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="David",
    passwd="Sword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE twitch")
