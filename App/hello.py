from flask import (Flask, request, url_for,send_from_directory) 
app = Flask(__name__)
import os
'''
@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'


@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
	print (url_for('index'))
	print (url_for('login'))
	print (url_for('profile', username='mark'))
'''

@app.route('/login', methods=['Get', 'POST'])
def login():
	if request.method =='POST':
		do_the_login()
	else:
		show_the_login_form()

@app.route('/static/stylesheet.css')
def serve_static_css(filename):
	root_dir = os.path.dirname(os.getcwd())
	return send_from_directory(os.path.join(root_dir, 'static'), filename)




if __name__ == '__main__':
	app.run(debug = True)