import mysql.connector

#Connecting python to TestDataBase database of 'root' user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Game"
)

#Creating a cursor
my_cursor=mydb.cursor()

#Creating a database
'''
my_cursor.execute("CREATE DATABASE Game;")
'''

#Creating a table
"""my_cursor.execute("CREATE TABLE IF NOT EXISTS modules(highscore INTEGER(10),"
                     "user_id INTEGER AUTO_INCREMENT Primary KEY);")"""


mydb.commit()
#Closing the cursor
my_cursor.close()

#Closing database after creation
mydb.close()

