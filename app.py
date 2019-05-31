from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    owner = db.relationship('Player', backref=db.backref('roles'))


db.create_all()


@app.route('/')
def index():
    p1 = Player(username='a', password='1')
    r1 = Role(name='ar', level=0, owner_id=1)
    db.session.add(p1)
    db.session.add(r1)

    r2 = Role(name='arr', level=1)
    r2.owner = Player.query.filter(Player.id == 1).first()
    db.session.add(r2)
    db.session.commit()

    player = Player.query.filter(Player.id == 1).first()
    print(player.roles)
    return 'Index'


if __name__ == '__main__':
    app.run()
