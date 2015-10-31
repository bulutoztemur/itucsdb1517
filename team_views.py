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
        #team1 = Team('Teamli 1', color='red')
        #team2 = Team('Teamli 2', color='blue')
        #teams = [(1, team1), (2, team2)]
        teams = team_operations.get_teams()
        now = datetime.datetime.now()
        return render_template('team.html', teams=teams, current_time=now.ctime())
    else:
        name = request.form['name']
        color = request.form['color']
        team = Team(name, color)
        teams = [(1,team)]
        #return redirect(url_for('team_page', teams=team, current_time=now.ctime())
        now = datetime.datetime.now()
        return render_template('team.html', teams=teams, current_time=now.ctime())

@app.route('/team/add')
def team_edit_page():
    now = datetime.datetime.now()
    return render_template('admin/team_edit.html', current_time=now.ctime())