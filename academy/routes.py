from academy import app
from flask import flash, render_template, redirect, url_for, request
from academy.forms import RegisterUserForm, LoginUserForm
from academy.models import User
from academy import db
from werkzeug.security import generate_password_hash

def show(msg):
    print('*'*50)
    print(msg)
    print('*'*50)

@app.route('/')
def root():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginUserForm()
    if request.method == 'POST':
        return redirect(url_for('root'))
    return render_template('academy/login.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register_user():
    form = RegisterUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            show('registring.....')
            new_user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password1.data,
                user_type=form.user_type.data
            )
            show('USER is set!')

            db.session.add(new_user)
            show('session. ADDED')
            db.session.commit()
            show('COMMITED REGISTERED!')
            return redirect(url_for('root'))
        if form.errors != {}:
            for error in form.errors.values():
                flash(f'FORM ERROR: {error}', category='danger')

    return render_template('academy/register.html', form=form)


@app.route('/testing')
def testing():
    return render_template('testing.html')
