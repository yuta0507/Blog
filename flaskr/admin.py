from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db
from flaskr.auth import login_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def index():
    return render_template('admin/index.html')
