import datetime

from flask import render_template

from config import app

@app.route('/team')
def team_page():
    now = datetime.datetime.now()
    return render_template('team.html', current_time=now.ctime())