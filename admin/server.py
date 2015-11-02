
from flask import render_template
from flask import Blueprint
admin = Blueprint('admin', __name__,template_folder='templates/')


import datetime

from flask import url_for
from flask import redirect
from flask import request

from classes.team import Team
from classes.team_operations import team_operations

@admin.route('/')
def admin_page():
    return render_template('admin.html')


@admin.route('/teams', methods=['GET','POST'])
def team_page(key=None):
    if request.method == 'GET':
        store = team_operations()
        teams=store.get_teams()
        now = datetime.datetime.now()
        return render_template('admin_teams.html', teams=teams, current_time=now.ctime())
    else:
        if key==None:
            name = request.form['name']
            color = request.form['color']
            team = Team(name, color,'10-01-10',1,1,0)
            store = team_operations()
            result=store.add_team(team)
            return redirect(url_for('admin.team_page'))
        else:
            name = request.form['name']
            color = request.form['color']
            team = Team(name, color,'10-01-10',1,1,0)
            store = team_operations()
            result=store.update_team(key,team)
            return redirect(url_for('admin.team_page'))

@admin.route('/teams/add')
@admin.route('/teams/<int:key>')
def team_edit_page(key=None):
    store = team_operations()
    team = store.get_team(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('team_edit.html', team=team, current_time=now.ctime())