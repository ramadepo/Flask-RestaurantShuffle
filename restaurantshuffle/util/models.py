from util.exts import db


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.String(6), primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(70), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    permission = db.Column(db.Integer, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'create_date': self.create_date,
            'permission': self.permission
        }


class Subject(db.Model):
    __tablename__ = 'subject'

    account_id = db.Column(db.String(6), db.ForeignKey(
        'account.id'), primary_key=True, nullable=False)
    number = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_date = db.Column(db.DateTime, nullable=False)

    account = db.relationship('Account', backref=db.backref('subjects'))

    @property
    def serialize(self):
        return {
            'account_id': self.account_id,
            'number': self.number,
            'name': self.name,
            'last_date': self.last_date
        }


class Element(db.Model):
    __tablename__ = 'element'

    account_id = db.Column(db.String(6), db.ForeignKey(
        'subject.account_id'), primary_key=True, nullable=False)
    number = db.Column(db.Integer, primary_key=True, nullable=False)
    subject_no = db.Column(db.String(6), db.ForeignKey(
        'subject.number'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    account = db.relationship(
        'Account', foreign_keys='Element.account_id', backref=db.backref('elements'))
    subject = db.relationship('Subject', backref=db.backref('elements'))

    @property
    def serialize(self):
        return {
            'account_id': self.account_id,
            'number': self.number,
            'subject_no': self.subject_no,
            'name': self.name,
            'description': self.description
        }


class History(db.Model):
    __tablename__ = 'history'

    account_id = db.Column(db.String(6), db.ForeignKey(
        'account.id'), primary_key=True, nullable=False)
    number = db.Column(db.Integer, primary_key=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

    account = db.relationship('Account', backref=db.backref('historys'))

    @property
    def serialize(self):
        return {
            'account_id': self.account_id,
            'number': self.number,
            'create_date': self.create_date
        }


class WithHistoryElements(db.Model):
    __tablename__ = 'withhistoryelements'

    account_id = db.Column(db.String(6), db.ForeignKey(
        'account.id'), primary_key=True, nullable=False)
    history_no = db.Column(db.Integer, db.ForeignKey(
        'history.number'), primary_key=True, nullable=False)
    element_no = db.Column(db.Integer, db.ForeignKey(
        'element.number'), primary_key=True, nullable=False)
    check = db.Column(db.Boolean, default=True, nullable=False)

    @property
    def serialize(self):
        return {
            'account_id': self.account_id,
            'history_no': self.history_no,
            'element_no': self.element_no,
            'check': self.check
        }


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.String(6), db.ForeignKey(
        'account.id'), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)

    account = db.relationship('Account', backref=db.backref('messages'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'create_date': self.create_date,
            'content': self.content
        }


class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author,
            'create_date': self.create_date,
            'title': self.title,
            'content': self.content
        }
