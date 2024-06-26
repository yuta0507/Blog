from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/index.html')

@bp.route('/posts')
def posts():
    return render_template('blog/posts.html')
