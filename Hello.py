from flask import Flask, redirect, url_for, request, render_template, make_response, session, abort, flash
from werkzeug import secure_filename
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'a3u&UV(*9uv49UGIriuge8879b9*NRE_jkFEOH'
#@app.route('/')
#def hello_world():
#	return 'Hello World'

#@app.route('/hello/<name>/')
#def hello_name(name):
#	return 'Hello %s!' % name

@app.route('/blog/<int:postID>/')
def show_blog(postID):
	return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>/')
def revision(revNo):
	return 'Revision Number %f' %revNo

@app.route('/admin')
def hello_admin():
	return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))

	else:
		return redirect(url_for('hello_guest', guest = name))

# @app.route('/success/<name>')
# def success(name):
# 	return 'welcome %s' % name

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
# 	if request.method == 'POST':
# 		user = request.form['nm']
# 		return redirect(url_for('success',name = user))
# 	else:
# 		user = request.args.get('nm')
# 		return redirect(url_for('success', name = user))

@app.route('/hello/<user>')
def hello_name(user):
	return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
	return render_template('hello_score.html', marks=score)

#@app.route('/result/')
#def result():
#   dict = {'phy':50,'che':60,'maths':70}
#   return render_template('result.html', result = dict)

#@app.route('/')
#def index():
#	return render_template('index.html')

#@app.route('/')
#def student():
#   return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# @app.route('/')
# def index():
# 	return render_template('index2.html')

# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
# 	if request.method == 'POST':
# 	   user = request.form['nm']
	   
# 	   resp = make_response(render_template('readcookie.html'))
# 	   resp.set_cookie('userID', user)
# 	   return resp

# @app.route('/getcookie')
# def getcookie():
#    name = request.cookies.get('userID')
#    return '<h1>welcome '+name+'</h1>'

# @app.route('/')
# def index():
#    if 'username' in session:
#       username = session['username']
#       return 'Logged in as ' + username + '<br>' + \
#          "<b><a href = '/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>"

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    if request.method == 'POST':
#       session['username'] = request.form['username']
#       return redirect(url_for('index'))
#    return '''
#    <form action = "" method= "post">
#    <p><input type = text name = 'username'/></p>
#    <p><input type = submit value = 'Login'/></p>
#    </form>
#    '''

# @app.route('/')
# def index():
#    return render_template('log_in.html')

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
# 	if request.method == 'POST' and request.form['username'] == 'admin' :
# 		return redirect(url_for('success'))
# 	return abort(401)

# @app.route('/success')
# def success():
#    return 'logged in successfully'

# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))

# @app.route('/')
# def index():
# 	return render_template('index3.html')

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    error = None
   
#    if request.method == 'POST':
#       if request.form['username'] != 'admin' or \
#          request.form['password'] != 'admin':
#          error = 'Invalid username or password. Please try again!'
#       else:
#          flash('You were successfully logged in')
#          return redirect(url_for('index'))
#    return render_template('login.html', error = error)


# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploader():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student2.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            
            cur.execute('INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)',(nm,addr,city,pin))
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result2.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)


if __name__=='__main__':
	app.run(debug = True)
	