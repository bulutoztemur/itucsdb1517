
from flask import render_template
from flask import Blueprint
admin = Blueprint('admin', __name__,template_folder='templates/')


import datetime

import psycopg2 as dbapi2

from flask import url_for
from flask import redirect
from flask import request
from flask.helpers import url_for

from classes.operations.database_init import database_initialization

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

from classes.match import Match
from classes.operations.match_operations import match_operations

from classes.player import Player
from classes.operations.player_operations import player_operations

from classes.statistic import Statistic
from classes.operations.statistic_operations import statistic_operations

from flask import render_template, request, session, redirect, url_for, flash
from functools import wraps

def admin_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'admin' in session and session['admin']==True:
            return test(*args, **kwargs)
        else:
            return redirect(url_for('home_page'))
    return wrap

@admin.route('/init')
def init_db():
    store = database_initialization()
    store.init_db()
    return render_template('admin.html')

@admin.route('/')
@admin_required
def admin_page():
    return render_template('admin.html')

@admin.route('/country', methods=['GET','POST'])
@admin_required
def country_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = country_operations()
            result=store.delete_country(request.args.get('key'))
            return redirect(url_for('admin.country_page', error=result))
        else:
            store = country_operations()
            countries=store.get_countries()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_countries.html', countries=countries, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.country_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                country = Country(None,name, 0)
                store = country_operations()
                result=store.add_country(country)
                return redirect(url_for('admin.country_page', error=result))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = country_operations()
                result=store.update_country(key, name)
                return redirect(url_for('admin.country_page', error=result))


@admin.route('/country/add')
@admin.route('/country/<int:key>')
@admin_required
def country_edit_page(key=None):
    store = country_operations()
    country = store.get_country(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('country_edit.html', country=country, current_time=now.ctime())


@admin.route('/teams', methods=['GET','POST'])
@admin_required
def team_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = team_operations()
            result=store.delete_team(request.args.get('key'))
            return redirect(url_for('admin.team_page', error=result))
        else:
            store = team_operations()
            teams=store.get_teams()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_teams.html', teams=teams, error=error, current_time=now.ctime())
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
                return redirect(url_for('admin.team_page', error=result))
            else:
                name = request.form['name']
                color = request.form['color']
                key = request.form['key_value']
                date = request.form['date']
                countryid = request.form['countryid']
                courtid = request.form['courtid']
                store = team_operations()
                result=store.update_team(key,name,color,date,countryid,courtid)
                return redirect(url_for('admin.team_page', error=result))

@admin.route('/teams/add')
@admin.route('/teams/<int:key>')
@admin_required
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
@admin_required
def court_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = court_operations()
            result=store.delete_court(request.args.get('key'))
            return redirect(url_for('admin.court_page', error=result))
        else:
            store = court_operations()
            courts=store.get_courts()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_courts.html', courts=courts, error=error, current_time=now.ctime())
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
                return redirect(url_for('admin.court_page', error=result))
            else:
                name = request.form['name']
                address = request.form['address']
                capacity = request.form['capacity']
                key = request.form['key_value']
                store = court_operations()
                result=store.update_court(key, name, address, capacity)
                return redirect(url_for('admin.court_page', error=result))

@admin.route('/courts/add')
@admin.route('/courts/<int:key>')
@admin_required
def court_edit_page(key=None):
    store = court_operations()
    court = store.get_court(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('court_edit.html', court=court, current_time=now.ctime())

@admin.route('/transfers', methods=['GET','POST'])
def transfer_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = transfer_operations()
            result=store.delete_transfer(request.args.get('key'))
            return redirect(url_for('admin.transfer_page', error=result))
        else:
            store = transfer_operations()
            transfers=store.get_transfers()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_transfers.html', transfers=transfers, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.transfer_page'))

        else:
            if request.form['key_value']=='':
                playerid = request.form['playerid']
                oldteamid = request.form['oldteamid']
                newteamid = request.form['newteamid']
                seasonid = request.form['seasonid']
                transfer = Transfer(None,playerid, None, oldteamid, None, newteamid, None, seasonid,None, 0)
                store = transfer_operations()
                result=store.add_transfer(transfer)
                return redirect(url_for('admin.transfer_page', error=result))
            else:
                key = request.form['key_value']
                playerid = request.form['playerid']
                oldteamid = request.form['oldteamid']
                newteamid = request.form['newteamid']
                seasonid = request.form['seasonid']
                store = transfer_operations()
                result=store.update_transfer(key,playerid,oldteamid,newteamid,seasonid)
                return redirect(url_for('admin.transfer_page', error=result))

@admin.route('/transfers/add')
@admin.route('/transfers/<int:key>')
@admin_required
def transfer_edit_page(key=None):
    store = transfer_operations()
    storeTeam = team_operations()
    storeSeason = season_operations()
    storePlayer = player_operations()
    transfer = store.get_transfer(key) if key is not None else None
    teams = storeTeam.get_teams()
    seasons = storeSeason.get_seasons()
    players = storePlayer.get_players()
    now = datetime.datetime.now()
    return render_template('transfer_edit.html', transfer=transfer, teams=teams,seasons=seasons,players=players, current_time=now.ctime())



@admin.route('/hand', methods=['GET','POST'])
@admin_required
def hand_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = hand_operations()
            result=store.delete_hand(request.args.get('key'))
            return redirect(url_for('admin.hand_page', error=result))
        else:
            store = hand_operations()
            hands=store.get_hands()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_hands.html', hands=hands, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.hand_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                hand = Hand(None,name, 0)
                store = hand_operations()
                result=store.add_hand(hand)
                return redirect(url_for('admin.hand_page', error=result))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = hand_operations()
                result=store.update_hand(key, name)
                return redirect(url_for('admin.hand_page', error=result))


@admin.route('/hand/add')
@admin.route('/hand/<int:key>')
@admin_required
def hand_edit_page(key=None):
    store = hand_operations()
    hand = store.get_hand(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('hand_edit.html', hand=hand, current_time=now.ctime())


@admin.route('/position', methods=['GET','POST'])
@admin_required
def position_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = position_operations()
            result=store.delete_position(request.args.get('key'))
            return redirect(url_for('admin.position_page', error=result))
        else:
            store = position_operations()
            positions=store.get_positions()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_positions.html', positions=positions, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.position_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                position = Position(None,name, 0)
                store = position_operations()
                result=store.add_position(position)
                return redirect(url_for('admin.position_page', error=result))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = position_operations()
                result=store.update_position(key, name)
                return redirect(url_for('admin.position_page', error=result))


@admin.route('/position/add')
@admin.route('/position/<int:key>')
@admin_required
def position_edit_page(key=None):
    store = position_operations()
    position = store.get_position(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('position_edit.html', position=position, current_time=now.ctime())



@admin.route('/season', methods=['GET','POST'])
@admin_required
def season_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = season_operations()
            result=store.delete_season(request.args.get('key'))
            return redirect(url_for('admin.season_page',error=result))
        else:
            store = season_operations()
            seasons=store.get_seasons()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_seasons.html', seasons=seasons, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.season_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                season = Season(None,name, 0)
                store = season_operations()
                result=store.add_season(season)
                return redirect(url_for('admin.season_page', error=result))
            else:
                name = request.form['name']
                key = request.form['key_value']
                store = season_operations()
                result=store.update_season(key, name)
                return redirect(url_for('admin.season_page', error=result))


@admin.route('/season/add')
@admin.route('/season/<int:key>')
@admin_required
def season_edit_page(key=None):
    store = season_operations()
    season = store.get_season(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('season_edit.html', season=season, current_time=now.ctime())


@admin.route('/gender', methods=['GET','POST'])
@admin_required
def gender_page(key=None,operation=None, error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = gender_operations()
            result=store.delete_gender(request.args.get('key'))
            return redirect(url_for('admin.gender_page', error=result))
        else:
            store = gender_operations()
            genders=store.get_genders()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_genders.html', genders=genders, error = error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.gender_page'))

        else:
            if request.form['key_value']=='':
                type = request.form['name']
                gender = Gender(None,type, 0)
                store = gender_operations()
                result=store.add_gender(gender)
                return redirect(url_for('admin.gender_page', error=result))
            else:
                type = request.form['name']
                key = request.form['key_value']
                store = gender_operations()
                result=store.update_gender(key, type)
                return redirect(url_for('admin.gender_page', error=result))


@admin.route('/gender/add')
@admin.route('/gender/<int:key>')
@admin_required
def gender_edit_page(key=None):
    store = gender_operations()
    gender = store.get_gender(key) if key is not None else None
    now = datetime.datetime.now()
    return render_template('gender_edit.html', gender=gender, current_time=now.ctime())


@admin.route('/coaches', methods=['GET','POST'])
@admin_required
def coach_page(key=None,operation=None, error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = coach_operations()
            result=store.delete_coach(request.args.get('key'))
            return redirect(url_for('admin.coach_page', error=result))
        else:
            store = coach_operations()
            coaches=store.get_coaches()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_coaches.html', coaches=coaches, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.coach_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                surname = request.form['surname']
                countryid = request.form['countryid']
                teamid = request.form['teamid']
                birthyear = request.form['birthyear']
                genderid = request.form['genderid']
                coach = Coach(None,name, surname, countryid, None, teamid, None, birthyear, genderid, None, 0)
                store = coach_operations()
                result=store.add_coach(coach)
                return redirect(url_for('admin.coach_page', error=result))
            else:
                name = request.form['name']
                surname = request.form['surname']
                key = request.form['key_value']
                countryid = request.form['countryid']
                teamid = request.form['teamid']
                birthyear = request.form['birthyear']
                genderid = request.form['genderid']
                store = coach_operations()
                result=store.update_coach(key,name,surname,countryid,teamid, birthyear, genderid)
                return redirect(url_for('admin.coach_page', error=result))

@admin.route('/coaches/add')
@admin.route('/coaches/<int:key>')
@admin_required
def coach_edit_page(key=None):
    store = coach_operations()
    storeTeam = team_operations()
    storeCountry = country_operations()
    storeGenders = gender_operations()
    coach = store.get_coach(key) if key is not None else None
    teams = storeTeam.get_teams()
    countries = storeCountry.get_countries()
    genders = storeGenders.get_genders()
    now = datetime.datetime.now()
    return render_template('coach_edit.html', coach=coach, teams=teams, countries=countries, genders=genders, current_time=now.ctime())

@admin.route('/matches', methods=['GET','POST'])
@admin_required
def match_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = match_operations()
            result=store.delete_match(request.args.get('key'))
            return redirect(url_for('admin.match_page',error=result))
        else:
            store = match_operations()
            matches=store.get_matches()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_matches.html', matches=matches, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.match_page'))

        else:
            if request.form['key_value']=='':
                hometeamid = request.form['hometeamid']
                awayteamid = request.form['awayteamid']
                courtid = request.form['courtid']
                matchdate = request.form['matchdate']
                match = Match(None,hometeamid, None, awayteamid, None, courtid, None, matchdate, 0)
                store = match_operations()
                result=store.add_match(match)
                return redirect(url_for('admin.match_page', error=result))
            else:
                hometeamid = request.form['hometeamid']
                awayteamid = request.form['awayteamid']
                courtid = request.form['courtid']
                matchdate = request.form['matchdate']
                key = request.form['key_value']
                store = match_operations()
                result=store.update_match(key,hometeamid,awayteamid,courtid,matchdate)
                return redirect(url_for('admin.match_page', error=result))

@admin.route('/matches/add')
@admin.route('/matches/<int:key>')
@admin_required
def match_edit_page(key=None):
    store = match_operations()
    storeTeam = team_operations()
    storeCourt = court_operations()

    match = store.get_match(key) if key is not None else None
    teams = storeTeam.get_teams()
    courts = storeCourt.get_courts()

    now = datetime.datetime.now()
    return render_template('match_edit.html', match=match, teams=teams, courts=courts, current_time=now.ctime())

@admin.route('/players', methods=['GET','POST'])
@admin_required
def player_page(key=None,operation=None,error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = player_operations()
            result=store.delete_player(request.args.get('key'))
            return redirect(url_for('admin.player_page',error=result))
        else:
            store = player_operations()
            players=store.get_players()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_players.html', players=players, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.player_page'))

        else:
            if request.form['key_value']=='':
                name = request.form['name']
                surname = request.form['surname']
                birthdate = request.form['birthdate']
                height = request.form['height']
                weight = request.form['weight']
                startdate = request.form['startdate']
                teamid = request.form['teamid']
                countryid = request.form['countryid']
                genderid = request.form['genderid']
                positionid = request.form['positionid']
                handid = request.form['handid']
                number = request.form['number']
                player = Player(None, name, surname, birthdate, height, weight, startdate, teamid, None, countryid, None, genderid, None, positionid, None, handid, None, number, 0)
                store = player_operations()
                result=store.add_player(player)
                return redirect(url_for('admin.player_page', error=result))
            else:
                name = request.form['name']
                surname = request.form['surname']
                birthdate = request.form['birthdate']
                height = request.form['height']
                weight = request.form['weight']
                startdate = request.form['startdate']
                teamid = request.form['teamid']
                countryid = request.form['countryid']
                genderid = request.form['genderid']
                positionid = request.form['positionid']
                handid = request.form['handid']
                number = request.form['number']
                key = request.form['key_value']
                store = player_operations()
                result=store.update_player(key,name, surname, birthdate, height, weight, startdate, teamid, countryid, genderid, positionid, handid, number)
                return redirect(url_for('admin.player_page', error=result))

@admin.route('/players/add')
@admin.route('/players/<int:key>')
@admin_required
def player_edit_page(key=None):
    store = player_operations()
    storeCountry = country_operations()
    storeTeam = team_operations()
    storeGender = gender_operations()
    storePosition = position_operations()
    storeHand = hand_operations()

    player = store.get_player(key) if key is not None else None
    teams = storeTeam.get_teams()
    countries = storeCountry.get_countries()
    genders = storeGender.get_genders()
    positions = storePosition.get_positions()
    hands = storeHand.get_hands()

    now = datetime.datetime.now()
    return render_template('player_edit.html', player=player, teams=teams, countries=countries, genders=genders, positions=positions, hands=hands, current_time=now.ctime())


@admin.route('/statistics', methods=['GET','POST'])
@admin_required
def statistic_page(key=None,operation=None, error=None):
    if request.method == 'GET':
        if request.args.get('operation') == 'delete':
            store = statistic_operations()
            result=store.delete_statistic(request.args.get('key'))
            return redirect(url_for('admin.statistic_page', error=result))
        else:
            store = statistic_operations()
            statistics=store.get_statistics()
            now = datetime.datetime.now()
            error = request.args.get('error')
            return render_template('admin_statistics.html', statistics=statistics, error=error, current_time=now.ctime())
    else:
        if request.form['submit']=='cancel':
            return redirect(url_for('admin.statistic_page'))

        else:
            if request.form['key_value']=='':
                assistnumber = request.form['assistnumber']
                blocknumber = request.form['blocknumber']
                score = request.form['score']
                cardnumber = request.form['cardnumber']
                seasonid = request.form['seasonid']
                playerid = request.form['playerid']
                statistic = Statistic(None, assistnumber, blocknumber, score, cardnumber, seasonid, None, playerid, None, 0)
                store = statistic_operations()
                result=store.add_statistic(statistic)
                return redirect(url_for('admin.statistic_page', error=result))
            else:
                key = request.form['key_value']
                assistnumber = request.form['assistnumber']
                blocknumber = request.form['blocknumber']
                score = request.form['score']
                cardnumber = request.form['cardnumber']
                seasonid = request.form['seasonid']
                playerid = request.form['playerid']
                store = statistic_operations()
                result=store.update_statistic(key,assistnumber,blocknumber,score,cardnumber,seasonid,playerid)
                return redirect(url_for('admin.statistic_page', error=result))

@admin.route('/statistics/add')
@admin.route('/statistics/<int:key>')
@admin_required
def statistic_edit_page(key=None):
    store = statistic_operations()
    storeSeason = season_operations()
    storePlayer = player_operations()
    statistic = store.get_statistic(key) if key is not None else None
    seasons = storeSeason.get_seasons()
    players = storePlayer.get_players()
    now = datetime.datetime.now()
    return render_template('statistic_edit.html', statistic=statistic, seasons=seasons,players=players, current_time=now.ctime())