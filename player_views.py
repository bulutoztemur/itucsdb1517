import datetime

from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

from config import app, login_required
from classes.player import Player
from classes.operations.player_operations import player_operations

@app.route('/player', methods=['GET','POST'])
@login_required
def player_page():
    if request.method == 'GET':
        store = player_operations()
        players=store.get_players()
        now = datetime.datetime.now()
        return render_template('player.html', players=players, current_time=now.ctime())
