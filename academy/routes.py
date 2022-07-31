from academy import app
from flask import flash, render_template, redirect, url_for, request
from academy.forms import RegisterUserForm, LoginUserForm
from academy.models import User
from academy import db
from flask_login import login_user, logout_user

def show(msg):
    print('*'*50)
    print(msg)
    print('*'*50)

@app.route('/')
def root():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login_user_route():
    form = LoginUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            _user = User.query.filter_by(username=form.username.data).first()
            if _user and _user.check_password_correction(attempted_password=form.password.data):
                login_user(_user)
                flash(f'You are logged in as {_user.username}!', category='success')
                return redirect(url_for('root'))
            else:
                flash(f'Login Error: Username or password is incorrect!', category='danger')
        if form.errors != {}:
            for error in form.errors.values():
                flash(f'FORM ERROR: {error}', category='danger')
    return render_template('academy/login.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    form = RegisterUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password1.data,
                user_type=form.user_type.data
            )

            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('root'))
        if form.errors != {}:
            for error in form.errors.values():
                flash(f'FORM ERROR: {error}', category='danger')

    return render_template('academy/register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('root'))

@app.route('/testing')
def testing():
    return render_template('testing.html')
