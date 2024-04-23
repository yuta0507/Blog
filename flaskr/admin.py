from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.utils.validation import Validation
from flaskr.models.post import Post
from flaskr.models.category import Category
from flaskr.models.location import Location

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def index():
    post = Post()

    return render_template(
        'admin/index.html',
        posts=post.fetch_index(),
        published=post.PUBLISHED
    )

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    post = Post()
    category = Category()
    location = Location()

    if request.method == 'POST':
        validation = Validation({
            'store_name': ['required'],
            'title': ['required'],
            'description': ['required'],
            'category_id': ['required'],
            'location_id': ['required'],
            'publish_flag': [],
            'body': ['required'],
        }, request.form)

        if validation.has_error:
            return render_template(
                'admin/create.html',
                categories=category.fetch_all(),
                locations=location.fetch_all(),
                published=post.PUBLISHED,
                error_message=validation.error_message
            )

        post.store(request.form)

        return redirect(url_for('admin.index'))

    return render_template(
        'admin/create.html',
        categories=category.fetch_all(),
        locations=location.fetch_all(),
        published=post.PUBLISHED
    )

@bp.route('/category', methods=('GET', 'POST'))
@login_required
def category():
    category = Category()

    if request.method == 'POST':
        validation = Validation({'name': ['required']}, request.form)

        if validation.has_error:
            return render_template(
                'admin/category.html',
                categories=category.fetch_all(),
                error_message=validation.error_message
            )

        category.store(request.form['name'].title())

    return render_template('admin/category.html', categories=category.fetch_all())

@bp.route('/location', methods=('GET', 'POST'))
@login_required
def location():
    location = Location()

    if request.method == 'POST':
        validation = Validation({'name': ['required']}, request.form)

        if validation.has_error:
            return render_template(
                'admin/location.html',
                locations=location.fetch_all(),
                error_message=validation.error_message
            )

        location.store(request.form['name'].title())

    return render_template('admin/location.html', locations=location.fetch_all())

@bp.route('/change-status/<int:post_id>', methods=('POST',))
@login_required
def change_status(post_id):
    post = Post()
    post.change_publish_flag(post_id)
    return redirect(url_for('admin.index'))
