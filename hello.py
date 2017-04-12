#!/usr/bin/python

from flask import Flask, url_for, render_template, request, session, flash, redirect
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def valid_login(username,password):

    if username != app.config['USERNAME']:
        outcome = False
    elif password != app.config['PASSWORD']:
        outcome = False
    else:
        outcome = True
    return outcome

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('hello.html')
    return render_template('login.html', error=error)

with app.test_request_context():
    print url_for('static', filename='style.css')
    print url_for('index')
