from flask import Flask, render_template, request
from exts import db
import config
from models import Player, Role


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    return 'Search ' + request.args.get('s1') + ' ' + request.args.get('s2')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return f"Your username is {request.form.get('username')} \t\t Your password is {request.form.get('password')}"


if __name__ == '__main__':
    app.run()
