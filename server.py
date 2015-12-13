import datetime
import os
import json
import re

from classes.user import User
from classes.operations.user_operations import user_operations
from classes.operations.database_init import database_initialization
from flask import render_template, request, session, redirect, url_for, flash
from config import app, login_required
import team_views
import player_views
import statistics_views
import countries_views
import transfers_views

app.secret_key = 'my preciousssss'


@app.route('/')
@login_required
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/rules')
@login_required
def rules_page():
    now = datetime.datetime.now()
    return render_template('rules.html', current_time=now.ctime())


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('admin', None)
    session.pop('username', None)
    flash('You were logged out')
    return redirect (url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    now = datetime.datetime.now()
    error = None
    if request.method == 'POST':
        store = user_operations()
        if request.form['submit']=='login':
            result=store.get_user(request.form['username'], request.form['password'])
            if result.role is '':
                error = 'Invalid Credentials. Please try again.'
            else:
                session['logged_in'] = True
                session['username'] = request.form['username'];
                if result.role == 'admin':
                    session['admin'] = True
                return redirect(url_for('home_page'))
        else:
            result=store.add_user(User(0,request.form['username_r'], request.form['password_r'],1,'',request.form['name'],request.form['surname'],request.form['birthdate']))
            if result=='success':
                session['logged_in'] = True
                session['username'] = request.form['username_r'];
                return redirect(url_for('home_page'))
    return render_template('login.html', error=error, current_time=now.ctime())

@app.route('/init')
def init_db():
    store = database_initialization()
    store.init_db()
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)