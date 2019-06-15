from exts import db


class Region(db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Shop(db.Model):
    __tablename__ = 'shop'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey(
        'region.id'), nullable=False)
    locate_region = db.relationship('Region', backref=db.backref('shops'))