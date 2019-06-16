from flask import Flask, render_template, request, redirect, url_for
from exts import db
import config
from models import Region, Shop


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/region', methods=['POST'])
def create_region():
    name = request.form.get('name')

    region = Region.query.filter(Region.name == name).first()

    if region:
        pass
    else:
        new_region = Region(name=name)
        db.session.add(new_region)
        db.session.commit()

    return redirect(url_for('get_regions'))


@app.route('/region')
def get_regions():
    regions = Region.query.order_by(Region.name).all()
    return render_template('region.html', regions=regions)


@app.route('/region/<id>')
def get_region(id):
    pass


@app.route('/shop', methods=['POST'])
def create_shop():
    name = request.form.get('name')
    region_id = request.form.get('region_id')

    shop = Shop(name=name, region_id=region_id)
    db.session.add(shop)
    db.session.commit()

    return redirect(url_for('get_shops'))


@app.route('/shop')
def get_shops():
    return render_template('shop.html')


@app.route('/shop/<id>')
def get_shop(id):
    pass


if __name__ == '__main__':
    app.run()
