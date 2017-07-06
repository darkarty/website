from flask import Flask, render_template, request, redirect, url_for
from flask.ext.login import (LoginManager, current_user, login_required, login_user, logout_user, UserMixin, confirm_login, fresh_login_required)

from models import User
import sqlite3 as sql
import createDB

app = Flask(__name__)
app.secret_key = 'a3u&UV(*9uv49UGIriuge8879b9*NRE_jkFEOH'

#flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "reauth"

users = {'foo@bar.tld': {'pw': 'secret'}}

@login_manager.user_loader
def user_loader(user_id):
	con = sql.connect('database.db')
	cur = con.cursor()
	cur.execute("select id from users where id='%s'" % user_id)
	rows = cur.fetchall()
	con.close
	return User(rows[0][0])

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return '''
		<form action='login' method='POST'>
		<input type='text' name='email' id='email' placeholder='email'></input>
		<input type='password' name='pw' id='pw' placeholder='password'></input>
		<input type='submit' name='submit'></input>
		</form>
		'''

	email = request.form['email']
	con = sql.connect('database.db')
	cur = con.cursor()
	cur.execute("select id, password from users where id='%s'" % email)
	rows= cur.fetchall()
	con.close
	#return render_template('test.html', rows=rows)

	if request.form['pw'] == rows[0][1]:
		user = User(rows[0][0])
		user.id = email
		login_user(user)
		return redirect(url_for('index'))

	return 'Bad login'

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

# routes
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
	con = sql.connect('database.db')
	#con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select rowid, * from contacts where rowid='%d'" % userID)
	rows = cur.fetchall()
	con.close
	return render_template('user_info.html',userID = userID, rows = rows)

@app.route('/<int:userID>/edit', methods = ['POST', 'GET'])
def edit_user(userID):
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		phone = request.form['phone']
		notes = request.form['notes']
		con = sql.connect('database.db')
		cur = con.cursor()
		cur.execute("UPDATE contacts SET firstname = '%s', lastname = '%s', email = '%s', phone = '%s', notes = '%s' WHERE rowid='%d'" % (firstname, lastname, email, phone, notes, userID))
		con.commit()
		con.close
		return redirect(url_for('index'))
	else:
		return render_template('user_edit.html', userID=userID)

@app.route('/<int:userID>/delete')
def delete_user(userID):
	con = sql.connect('database.db')
	cur = con.cursor()
	cur.execute("DELETE FROM contacts WHERE rowid='%d'" % userID)
	con.commit()
	con.close
	return redirect(url_for('index'))


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
		return redirect(url_for('index'))	
	else:
		return render_template('new.html')

if __name__ == '__main__':
  app.run(debug = True)
