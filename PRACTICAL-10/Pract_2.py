"""
Design a database application to search the specified record from the database.
"""

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database="bscit"
	)
mycursor = mydb.cursor()

mycursor.execute("select * from students where age > '22'")
result = mycursor.fetchall()

for x in result:
	print(x)
