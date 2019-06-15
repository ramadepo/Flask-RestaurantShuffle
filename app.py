from flask import Flask, render_template, request
from exts import db
import config
from models import *


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
