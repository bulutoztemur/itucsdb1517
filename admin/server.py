from flask import Blueprint
from flask import render_template

bp = Blueprint('admin', __name__,template_folder='templates')


@bp.route('/')
def admin_page():
    return render_template('admin.html')
