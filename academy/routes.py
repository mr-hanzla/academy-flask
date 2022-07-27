from academy import app
from flask import render_template
from academy.forms import RegisterUserForm

def show(msg):
    print('*'*50)
    print(msg)
    print('*'*50)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register')
def register_user():
    form = RegisterUserForm()
    return render_template('academy/register.html', form=form)


@app.route('/testing')
def testing():
    return render_template('testing.html')
