from exts import db


class Region(db.Model):
    __tablename__ = 'region'
    __table_args__ = (
        db.UniqueConstraint('name', name='UC_Region'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Shop(db.Model):
    __tablename__ = 'shop'
    __table_args__ = (
        db.UniqueConstraint('name', 'region_id', name='UC_Shop'),
    )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey(
        'region.id'), nullable=False)
    locate_region = db.relationship('Region', backref=db.backref('shops'))