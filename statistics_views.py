import datetime

from flask import render_template

from config import app


@app.route('/statistics')
def statistics_page():
    now = datetime.datetime.now()
    return render_template('statistics.html', current_time=now.ctime())