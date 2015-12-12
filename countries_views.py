import datetime

from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

from config import app, login_required
from classes.country import Country
from classes.operations.country_operations import country_operations

@app.route('/countries', methods=['GET','POST'])
@login_required
def countries_page():
    if request.method == 'GET':
        store = country_operations()
        countries=store.get_countries()
        now = datetime.datetime.now()
        return render_template('countries.html', countries=countries, current_time=now.ctime())
