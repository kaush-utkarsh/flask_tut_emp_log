from flask import Flask, render_template, url_for, session, redirect, escape, request
from operations import *
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
	return render_template('landingpage.html')


@app.route("/home")
def home():
	if "username" not in session:
		return redirect(url_for('login'))
	di = {	'title':'Home',
			'LogInUserName':session['username']
		}
	return render_template('home.html', data=di)

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method == 'POST':
		if login_check(request.form['username'].strip(" "),request.form['password'].strip(" ")):
			session['username'] = request.form['username'].strip(" ")
			return redirect(url_for('home'))
		else:
			return render_template('login.html',errormsg = True)
	if "username" in session:
		return redirect(url_for('home'))

	return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
	# note that we set the 404 status explicitly
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
