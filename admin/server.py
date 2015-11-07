
from flask import render_template
from flask import Blueprint
admin = Blueprint('admin', __name__,template_folder='templates/')


import datetime

from flask import url_for
from flask import redirect
from flask import request

from classes.team import Team
from classes.operations.team_operations import team_operations

from classes.court import Court
from classes.operations.court_operations import court_operations

from classes.transfer import Transfer
from classes.operations.transfer_operations import transfer_operations

@admin.route('/')
def admin_page():
    return render_template('admin.html')


@admin.route('/teams', methods=['GET','POST'])
def team_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = team_operations()
            result=store.delete_team(request.args.get('key'))
            return redirect(url_for('admin.team_page'))
        else:
            store = team_operations()
            teams=store.get_teams()
            now = datetime.datetime.now()
            return render_template('admin_teams.html', teams=teams, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.team_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                color = request.form['color']
                date = request.form['date']
                countryid = request.form['countryid']
                courtid = request.form['courtid']
                team = Team(None,name, color, date, countryid, courtid, None, 0)
                store = team_operations()
                result=store.add_team(team)
                return redirect(url_for('admin.team_page'))
            else:
                name = request.form['name']
                color = request.form['color']
                key = request.form['key_value']
                date = request.form['date']
                countryid = request.form['countryid']
                courtid = request.form['courtid']
                store = team_operations()
                result=store.update_team(key,name,color,date,countryid,courtid)
                return redirect(url_for('admin.team_page'))

@admin.route('/teams/add')
@admin.route('/teams/<int:key>')
def team_edit_page(key=None):
    store = team_operations()
    team = store.get_team(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('team_edit.html', team=team, current_time=now.ctime())

@admin.route('/courts', methods=['GET','POST'])
def court_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = court_operations()
            result=store.delete_court(request.args.get('key'))
            return redirect(url_for('admin.court_page'))
        else:
            store = court_operations()
            courts=store.get_courts()
            now = datetime.datetime.now()
            return render_template('admin_courts.html', courts=courts, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.court_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                address = request.form['address']
                capacity = request.form['capacity']
                court = Court(name, address,capacity,0)
                store = court_operations()
                result=store.add_court(court)
                return redirect(url_for('admin.court_page'))
            else:
                name = request.form['name']
                address = request.form['address']
                capacity = request.form['capacity']
                key = request.form['key_value']
                court = Court(name, address,capacity,0)
                store = court_operations()
                result=store.update_court(key, name, address, capacity)
                return redirect(url_for('admin.court_page'))

@admin.route('/courts/add')
@admin.route('/courts/<int:key>')
def court_edit_page(key=None):
    store = court_operations()
    court = store.get_court(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('court_edit.html', court=court, current_time=now.ctime())

@admin.route('/transfers', methods=['GET','POST'])
def transfer_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = transfer_operations()
            result=store.delete_transfer(request.args.get('key'))
            return redirect(url_for('admin.transfer_page'))
        else:
            store = transfer_operations()
            transfers=store.get_transfers()
            now = datetime.datetime.now()
            return render_template('admin_transfers.html', transfers=transfers, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.transfer_page'))

        else:
            if request.form['key_value']=='':
                playerid = request.form['playerid']
                oldteamid = request.form['oldteamid']
                newteamid = request.form['newteamid']
                seasonid = request.form['seasonid']
                transfer = Transfer(playerid, oldteamid,newteamid,seasonid,0)
                store = transfer_operations()
                result=store.add_transfer(transfer)
                return redirect(url_for('admin.transfer_page'))
            else:
                playerid = request.form['playerid']
                oldteamid = request.form['oldteamid']
                newteamid = request.form['newteamid']
                seasonid = request.form['seasonid']
                key = request.form['key_value']
                transfer = Transfer(playerid, oldteamid,newteamid,seasonid,0)
                store = transfer_operations()
                result=store.update_transfer(key, playerid, oldteamid,newteamid,seasonid)
                return redirect(url_for('admin.transfer_page'))

@admin.route('/transfers/add')
@admin.route('/transfers/<int:key>')
def transfer_edit_page(key=None):
    store = transfer_operations()
    transfer = store.get_transfer(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('transfer_edit.html', transfer=transfer, current_time=now.ctime())
