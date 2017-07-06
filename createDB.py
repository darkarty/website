import sqlite3

conn = sqlite3.connect('database.db')

#Create database if it doesn't exist

try:
	conn.execute('CREATE TABLE contacts (firstname TEXT, lastname TEXT, email TEXT, phone TEXT, notes TEXT)')
	conn.commit()
	print("Database successfully created")

except:
	print("Database already exists")
	pass
try:
	conn.execute('CREATE TABLE users(id TEXT PRIMARY KEY, password TEXT)')
	conn.commit()
	print("user table created")

except:
	print("Database already exists")
	pass

try:
	conn.execute("INSERT into users (id, password) VALUES(?,?)",('123@123.com', 'Password1'))
	conn.commit()
	print("Successful insert into users table")

except:
	print("cant insert into users table")
	


#close database
conn.close()
