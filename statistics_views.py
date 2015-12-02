import datetime

from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

from config import app
from classes.statistic import Statistic
from classes.operations.statistic_operations import statistic_operations

@app.route('/statistics', methods=['GET','POST'])
def statistics_page():
    if request.method == 'GET':
        store = statistic_operations()
        statistics=store.get_statistics()
        now = datetime.datetime.now()
        return render_template('statistics.html', statistics=statistics, current_time=now.ctime())
