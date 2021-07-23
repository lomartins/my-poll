from flask import request, redirect, url_for, flash, render_template, Blueprint
from flask_login import current_user, login_user, login_required, logout_user

from ..models import User
from .forms import LoginForm, SignUpForm
from ..poll_app import db


blueprint = Blueprint("Authentication", __name__)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        login_user(user)
        origin_url = request.args.get('origin')
        flash('Logged in successfully.')
        return redirect(origin_url or url_for('home_page'))

    if form.is_submitted():
        flash('Login or password incorrect.')

    return render_template('login/login.html', form=form)


@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)

    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        origin_url = request.args.get('origin')
        login_user(user)
        flash('Your new account has been created.')
        return redirect(origin_url or url_for('home_page'))

    return render_template('login/signup.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))
