#!/usr/bin/python

from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/projects/')
def projects():
    return "The project page"

@app.route('/about')
def about():
    return "The about page"

with app.test_request_context():
    print url_for('static', filename='style.css')
    print url_for('index')
