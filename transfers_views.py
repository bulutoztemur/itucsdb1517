import datetime

from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

from config import app, login_required
from classes.transfer import Transfer
from classes.operations.transfer_operations import transfer_operations

@app.route('/transfers', methods=['GET','POST'])
@login_required
def transfers_page():
    if request.method == 'GET':
        store = transfer_operations()
        transfers=store.get_transfers()
        now = datetime.datetime.now()
        return render_template('transfers.html', transfers=transfers, current_time=now.ctime())
