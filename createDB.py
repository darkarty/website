import sqlite3

conn = sqlite3.connect('database.db')

#Create database if it doesn't exist

try:
	conn.execute('CREATE TABLE contacts (firstname TEXT, lastname TEXT, email TEXT, phone TEXT, notes TEXT)')
	conn.commit()
	print("Database successfully created")
#Database exists already
except:
	print("Database already exists")
#close database
conn.close()
