#from flask import Flask, render_template, redirect, url_for, request, session
from flask import *
app = Flask(__name__)
#from app import app
app.secret_key='6264'
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/welcome")
def welcome(): 
    return render_template('welcome.html')
@app.route("/main")
def home():
    return render_template('index.html')
@app.route('/showSignUp')
def showSignUp():
    return render_template('index.html')
@app.route('/showSignIn', methods=['GET', 'POST'])
def showSignIn():
     return render_template('signin.html')
@app.route("/archean")
def archean():
     return render_template('archean1.html')
@app.route('/login',methods=['GET','POST'])
def login():
     error = None
     if request.method == 'POST':
	if request.form['username'] != 'admin' or request.form['password'] != 'admin':
		error = 'Invalid Credentials. Try Again.'
	else:
		session['logged_in']= True
		return redirect(url_for('archean'))
     return render_template('login.html', error = error) 
@app.route('/logout')
def logout():
     session.pop('logged_in', None)
     return redirect(url_for('home'))
@app.route('/mostwatched')
def mostwatched():
     return render_template('mostwatched.html')
@app.route('/highestratings')
def highestratings():
     return render_template('/highestratings.html')
@app.route('/recommended')
def recommended():
     return render_template('/recommended.html')
@app.route('/superhero')
def superhero():
     return render_template('/superhero.html')
@app.route('/sim1')
def sim1():
     return render_template('sim1.html')
if __name__ == "__main__":
    app.run(debug=True)
