from academy import app
from flask import render_template

def show(msg):
    print('*'*50)
    print(msg)
    print('*'*50)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')
