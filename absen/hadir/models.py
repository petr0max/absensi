from .. import db
from datetime import datetime


class Permit(db.Model):
    __tablename__ = 'permits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    permit = db.Column(db.String(64), index=True)
    long_date = db.Column(db.Integer)
    start_date = db.Column(db.DateTime(), default=datetime.now())
    permit_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class CheckIn(db.Model):
    __tablename__ = 'checkins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.DateTime(), default=datetime.now())
    jam_datang = db.Column(db.Time(), default=datetime.now())


class CheckOut(db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.DateTime(), default=datetime.now())
    jam_pulang = db.Column(db.Time(), default=datetime.now())
