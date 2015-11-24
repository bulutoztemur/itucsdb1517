
from flask import render_template
from flask import Blueprint
admin = Blueprint('admin', __name__,template_folder='templates/')


import datetime

import psycopg2 as dbapi2

from flask import url_for
from flask import redirect
from flask import request
from flask.helpers import url_for

from classes.country import Country
from classes.operations.country_operations import country_operations

from classes.gender import Gender
from classes.operations.gender_operations import gender_operations

from classes.hand import Hand
from classes.operations.hand_operations import hand_operations

from classes.team import Team
from classes.operations.team_operations import team_operations

from classes.court import Court
from classes.operations.court_operations import court_operations

from classes.transfer import Transfer
from classes.operations.transfer_operations import transfer_operations

from classes.position import Position
from classes.operations.position_operations import position_operations

from classes.season import Season
from classes.operations.season_operations import season_operations

from classes.coach import Coach
from classes.operations.coach_operations import coach_operations



@admin.route('/')
def admin_page():
    return render_template('admin.html')

@admin.route('/country', methods=['GET','POST'])
def country_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = country_operations()
            result=store.delete_country(request.args.get('key'))
            return redirect(url_for('admin.country_page'))
        else:
            store = country_operations()
            countries=store.get_countries()
            now = datetime.datetime.now()
            return render_template('admin_countries.html', countries=countries, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.country_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                country = Country(None,name, 0)
                store = country_operations()
                result=store.add_country(country)
                return redirect(url_for('admin.country_page'))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = country_operations()
                result=store.update_country(key, name)
                return redirect(url_for('admin.country_page'))


@admin.route('/country/add')
@admin.route('/country/<int:key>')
def country_edit_page(key=None):
    store = country_operations()
    country = store.get_country(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('country_edit.html', country=country, current_time=now.ctime())


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
                team = Team(None,name, color, date, countryid, None, courtid, None, 0)
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
    storeCourt = court_operations()
    storeCountry = country_operations()
    team = store.get_team(key) if key is not None else None
    courts = storeCourt.get_courts()
    countries = storeCountry.get_countries()
    now = datetime.datetime.now()
    return render_template('team_edit.html', team=team, courts=courts, countries=countries, current_time=now.ctime())

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
                court = Court(None ,name, address,capacity,0)
                store = court_operations()
                result=store.add_court(court)
                return redirect(url_for('admin.court_page'))
            else:
                name = request.form['name']
                address = request.form['address']
                capacity = request.form['capacity']
                key = request.form['key_value']
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
                transfer = Transfer(None,playerid, oldteamid, None, newteamid, None, seasonid,None, 0)
                store = transfer_operations()
                result=store.add_transfer(transfer)
                return redirect(url_for('admin.transfer_page'))
            else:
                key = request.form['key_value']
                playerid = request.form['playerid']
                oldteamid = request.form['oldteamid']
                newteamid = request.form['newteamid']
                seasonid = request.form['seasonid']
                store = transfer_operations()
                result=store.update_transfer(key,playerid,oldteamid,newteamid,seasonid)
                return redirect(url_for('admin.transfer_page'))

@admin.route('/transfers/add')
@admin.route('/transfers/<int:key>')
def transfer_edit_page(key=None):
    store = transfer_operations()
    storeTeam = team_operations()
    storeSeason = season_operations()
    transfer = store.get_transfer(key) if key is not None else None
    teams = storeTeam.get_teams()
    seasons = storeSeason.get_seasons()
    now = datetime.datetime.now()
    return render_template('transfer_edit.html', transfer=transfer, teams=teams,seasons=seasons, current_time=now.ctime())



@admin.route('/hand', methods=['GET','POST'])
def hand_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = hand_operations()
            result=store.delete_hand(request.args.get('key'))
            return redirect(url_for('admin.hand_page'))
        else:
            store = hand_operations()
            hands=store.get_hands()
            now = datetime.datetime.now()
            return render_template('admin_hands.html', hands=hands, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.hand_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                hand = Hand(None,name, 0)
                store = hand_operations()
                result=store.add_hand(hand)
                return redirect(url_for('admin.hand_page'))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = hand_operations()
                result=store.update_hand(key, name)
                return redirect(url_for('admin.hand_page'))


@admin.route('/hand/add')
@admin.route('/hand/<int:key>')
def hand_edit_page(key=None):
    store = hand_operations()
    hand = store.get_hand(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('hand_edit.html', hand=hand, current_time=now.ctime())


@admin.route('/position', methods=['GET','POST'])
def position_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = position_operations()
            result=store.delete_position(request.args.get('key'))
            return redirect(url_for('admin.position_page'))
        else:
            store = position_operations()
            positions=store.get_positions()
            now = datetime.datetime.now()
            return render_template('admin_positions.html', positions=positions, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.position_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                position = Position(None,name, 0)
                store = position_operations()
                result=store.add_position(position)
                return redirect(url_for('admin.position_page'))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = position_operations()
                result=store.update_position(key, name)
                return redirect(url_for('admin.position_page'))


@admin.route('/position/add')
@admin.route('/position/<int:key>')
def position_edit_page(key=None):
    store = position_operations()
    position = store.get_position(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('position_edit.html', position=position, current_time=now.ctime())



@admin.route('/season', methods=['GET','POST'])
def season_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = season_operations()
            result=store.delete_season(request.args.get('key'))
            return redirect(url_for('admin.season_page'))
        else:
            store = season_operations()
            seasons=store.get_seasons()
            now = datetime.datetime.now()
            return render_template('admin_seasons.html', seasons=seasons, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.season_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                season = Season(None,name, 0)
                store = season_operations()
                result=store.add_season(season)
                return redirect(url_for('admin.season_page'))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = season_operations()
                result=store.update_season(key, name)
                return redirect(url_for('admin.season_page'))


@admin.route('/season/add')
@admin.route('/season/<int:key>')
def season_edit_page(key=None):
    store = season_operations()
    season = store.get_season(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('season_edit.html', season=season, current_time=now.ctime())


@admin.route('/gender', methods=['GET','POST'])
def gender_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = gender_operations()
            result=store.delete_gender(request.args.get('key'))
            return redirect(url_for('admin.gender_page'))
        else:
            store = gender_operations()
            genders=store.get_genders()
            now = datetime.datetime.now()
            return render_template('admin_genders.html', genders=genders, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.gender_page'))

        else:
            if request.form['key_value']=='':
                type = request.form['name']
                gender = Gender(None,type, 0)
                store = gender_operations()
                result=store.add_gender(gender)
                return redirect(url_for('admin.gender_page'))
            else:
                type = request.form['name']
                key = request.form['key_value']
                store = gender_operations()
                result=store.update_gender(key, type)
                return redirect(url_for('admin.gender_page'))


@admin.route('/gender/add')
@admin.route('/gender/<int:key>')
def gender_edit_page(key=None):
    store = gender_operations()
    gender = store.get_gender(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('gender_edit.html', gender=gender, current_time=now.ctime())


@admin.route('/coaches', methods=['GET','POST'])
def coach_page(key=None,operation=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = coach_operations()
            result=store.delete_coach(request.args.get('key'))
            return redirect(url_for('admin.coach_page'))
        else:
            store = coach_operations()
            coaches=store.get_coaches()
            now = datetime.datetime.now()
            return render_template('admin_coaches.html', coaches=coaches, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.coach_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                surname = request.form['surname']
                countryid = request.form['countryid']
                teamid = request.form['teamid']
                coach = Coach(None,name, surname, countryid, teamid, None, 0)
                store = coach_operations()
                result=store.add_coach(coach)
                return redirect(url_for('admin.coach_page'))
            else:
                name = request.form['name']
                surname = request.form['surname']
                key = request.form['key_value']
                countryid = request.form['countryid']
                teamid = request.form['teamid']
                store = coach_operations()
                result=store.update_coach(key,name,surname,countryid,teamid)
                return redirect(url_for('admin.coach_page'))

@admin.route('/coaches/add')
@admin.route('/coaches/<int:key>')
def coach_edit_page(key=None):
    store = coach_operations()
    storeTeam = team_operations()
    storeCountry = country_operations()
    coach = store.get_coach(key) if key is not None else None
    teams = storeTeam.get_teams()
    countries = storeCountry.get_countries()
    now = datetime.datetime.now()
    return render_template('coach_edit.html', coach=coach, teams=teams, countries=countries, current_time=now.ctime())