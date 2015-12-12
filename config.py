from flask import Flask
from flask import render_template, request, session, redirect, url_for, flash
import admin.server as admin
from functools import wraps
app = Flask(__name__)
app.register_blueprint(admin.admin, url_prefix='/admin')


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login_page'))
    return wrap