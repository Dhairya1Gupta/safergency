import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234dhairya@#',

)

#prepare a cursor object
cursorObject = database.cursor()

#create a database

cursorObject.execute("CREATE DATABASE company")

print("All done!")