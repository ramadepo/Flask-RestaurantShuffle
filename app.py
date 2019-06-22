from flask import Flask, render_template, request, redirect, url_for
from exts import db
import config
from models import Region, Shop


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    regions = Region.query.order_by(Region.name).all()
    region_id = request.args.get('region_id')

    if region_id:
        pass
    else:
        pass

    return render_template('index.html', regions=regions)


@app.route('/', methods=['POST'])
def shuffle_restaurant():
    pass


@app.route('/region', methods=['POST'])
def create_region():
    name = request.form.get('name')

    region = Region.query.filter(Region.name == name).first()

    if region or name == '':
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


@app.route('/region/delete', methods=['POST'])
def delete_region():
    name = request.form.get('name')

    if name:
        region = Region.query.filter(Region.name == name).first()
        if region:
            for shop in region.shops:
                db.session.delete(shop)
            db.session.delete(region)
            db.session.commit()
    else:
        pass

    return redirect(url_for('get_regions'))


@app.route('/region/<id>')
def get_region(id):
    pass


@app.route('/shop', methods=['POST'])
def create_shop():
    name = request.form.get('name')
    region_id = int(request.form.get('region_id', '0'))

    if region_id == 0 or name == '':
        pass
    else:
        shop = Shop.query.filter(
            Shop.name == name, Shop.region_id == region_id).first()
        if shop:
            pass
        else:
            new_shop = Shop(name=name, region_id=region_id)
            db.session.add(new_shop)
            db.session.commit()

    return redirect(url_for('get_shops'))


@app.route('/shop')
def get_shops():
    regions = Region.query.order_by(Region.name).all()
    region_id = int(request.args.get('region_id', '0'))

    if region_id:
        shops = Shop.query.filter(Shop.region_id == region_id)
    else:
        shops = Shop.query.join(Region).order_by(Region.name).all()

    return render_template('shop.html', regions=regions, shops=shops, region_id=region_id)


@app.route('/shop/delete', methods=['POST'])
def delete_shop():
    id = request.form.get('id')

    if id:
        shop = Shop.query.filter(Shop.id == id).first()
        if shop:
            db.session.delete(shop)
            db.session.commit()
    else:
        pass

    return redirect(url_for('get_shops'))


@app.route('/shop/<id>')
def get_shop(id):
    pass


if __name__ == '__main__':
    app.run()
