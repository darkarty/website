from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import createDB

app = Flask(__name__)
app.secret_key = 'a3u&UV(*9uv49UGIriuge8879b9*NRE_jkFEOH'

@app.route('/')
def index():
	con = sql.connect('database.db')
	#con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute('select rowid, * from contacts')
	rows = cur.fetchall()
	con.close
	return render_template('index.html', rows=rows)
	

@app.route('/<int:userID>')
def user(userID):
	return render_template('user_info.html',userID = userID)

@app.route('/new', methods=['POST', 'GET'])
def new():
	if request.method=='POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		phone = request.form['phone']
		notes = request.form['notes']

		con = sql.connect('database.db')
		cur = con.cursor()
		cur.execute('INSERT INTO contacts (firstname, lastname, email, phone, notes) VALUES(?,?,?,?,?)',(firstname, lastname, email, phone, notes))
		con.commit()
		con.close
		return redirect('/')
			
	else:
		return render_template('new.html')

if __name__ == '__main__':
  app.run(debug = True)
