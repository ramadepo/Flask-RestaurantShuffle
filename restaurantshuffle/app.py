from flask import Flask, render_template, request, redirect, url_for
from util.exts import db
from util.models import *
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/subject')
def subject_page():
    return render_template('subject.html')


@app.route('/subject/<number>')
def subject_profile(number):
    return render_template('subject_profile.html')


@app.route('/history')
def history_page():
    return render_template('history.html')


@app.route('/log')
def log_page():
    return render_template('log.html')


@app.route('/user')
def user_page():
    return render_template('user.html')


@app.route('/user/<username>')
def user_profile(username):
    return render_template('user_profile.html')


if __name__ == '__main__':
    app.run()
