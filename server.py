import datetime
import os
import json
import re

from flask import render_template
from config import app
import team_views
import player_views
import statistics_views

@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/login')
def login_page():
    now = datetime.datetime.now()
    return render_template('login.html', current_time=now.ctime())

if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    app.run(host='0.0.0.0', port=port, debug=debug)