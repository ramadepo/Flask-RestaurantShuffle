from flask import Flask
from exts import db
import config
from models import Player, Role


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


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
