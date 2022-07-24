import os
from flask import Flask, render_template, request
import academy
import db



app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'my_db.sqlite'),
)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
app.register_blueprint(academy.bp)
with app.app_context():
    db.init_app(app)
    db.init_db()

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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
