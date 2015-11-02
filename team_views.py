import datetime

from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

from config import app
from classes.team import Team
from classes.team_operations import team_operations

@app.route('/team', methods=['GET','POST'])
def team_page():
    if request.method == 'GET':
        store = team_operations()
        teams=store.get_teams()
        now = datetime.datetime.now()
        return render_template('team.html', teams=teams, current_time=now.ctime())
