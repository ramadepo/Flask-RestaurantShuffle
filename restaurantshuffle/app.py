from flask import Flask, render_template, request, redirect, url_for
from exts import db
import config
from models import Region, Shop


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/subject')
def subject():
    return render_template('subject.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/log')
def log():
    return render_template('log.html')


if __name__ == '__main__':
    app.run()
