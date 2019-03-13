from flask import Flask, flash, redirect, request, session, url_for, escape, make_response
from flask import json
import os
from datetime import datetime
from flask import render_template
import urllib.request

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return render_template('logged.html',username=username)
    return render_template("index.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['admin']
        return redirect(url_for('index'))
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

"""

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['admin']
   
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
   
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()
