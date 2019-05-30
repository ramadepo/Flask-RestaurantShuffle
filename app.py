from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

db.create_all()

@app.route('/')
def index():
    print(url_for('user', id=5))
    return redirect(url_for('user', id=5))

@app.route('/user/<id>/')
def user(id):
    return f'User : {id}'

if __name__ == '__main__':
    app.run()