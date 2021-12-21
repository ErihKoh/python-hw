from flask import render_template, flash, url_for, redirect, request
from assistant_app import db
from flask_login import login_user, current_user, logout_user
from assistant_app.auth.forms import LoginForm, RegistrationForm
from assistant_app.models import User
from assistant_app.auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'Post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('contacts.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('contacts.index'))
    return render_template('login.html', title='Sign in', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('contacts.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)
