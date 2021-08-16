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
    checkin_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class CheckOut(db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.DateTime(), default=datetime.now())
    jam_pulang = db.Column(db.Time(), default=datetime.now())
    keterangan = db.Column(db.String(64), index=True)
    checkout_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Sick(db.Model):
    __tablename__ = 'sicks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.DateTime(), default=datetime.now())
    long_date = db.Column(db.Integer)
    diagnose = db.Column(db.String(64), index=True)
    sick_id = db.Column(db.Integer, db.ForeignKey('users.id'))
