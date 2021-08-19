from .. import db
import datetime


class Permit(db.Model):
    __tablename__ = 'permits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keterangan = db.Column(db.String(64), index=True)
    long_date = db.Column(db.Integer)
    start_date = db.Column(db.Date(), default=datetime.date.today())
    disetujui = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class CheckIn(db.Model):
    __tablename__ = 'checkins'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.Date(), default=datetime.date.today())
    jam_datang = db.Column(db.Time(), default=datetime.time())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class CheckOut(db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.Date(), default=datetime.date.today())
    jam_pulang = db.Column(db.Time(), default=datetime.time())
    keterangan = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Sick(db.Model):
    __tablename__ = 'sicks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl = db.Column(db.Date(), default=datetime.date.today())
    long_date = db.Column(db.Integer)
    keterangan = db.Column(db.String(64), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
