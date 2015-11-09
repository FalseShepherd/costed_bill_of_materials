# project/models.py


import datetime

from project import db


class Cbom(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(265), unique=True, nullable=False)
    rows = db.relationship('CbomRow',backref='cbom',lazy='dynamic')

class CbomRow(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cbom_id = db.Column(db.Integer, db.ForeignKey('cbom.id'))
    

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)
