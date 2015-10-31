import datetime

from flask import render_template

from config import app

@app.route('/player')
def player_page():
    now = datetime.datetime.now()
    return render_template('player.html', current_time=now.ctime())