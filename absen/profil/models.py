from .. import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(64), index=True)
    birthday = db.Column(db.Date(), default=datetime.date.today())
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    status_pegawai = db.Column(db.String(64), index=True)
    study = db.Column(db.String(64), index=True)
    jurusan = db.Column(db.String(64), index=True)
    gelar = db.Column(db.String(64), index=True)
    address_before = db.Column(db.String(64), index=True)
    address_now = db.Column(db.String(64), index=True)
    blood = db.Column(db.String(64), index=True)
    gender = db.Column(db.String(64), index=True)
    married = db.Column(db.String(64), index=True)
    religion = db.Column(db.String(64), index=True)
    warga_negara = db.Column(db.String(64), index=True)
    nik = db.Column(db.Integer, index=True)
    npwp = db.Column(db.Integer, index=True)
    no_hp = db.Column(db.Integer, index=True)
    zone = db.Column(db.String(64), index=True)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    childs = db.relationship('Child', backref='profile', lazy='dynamic')
    parents = db.relationship('Parent', backref='profile', lazy='dynamic')

    def __repr__(self):
        return f"{self.realname.title()}"


class Child(db.Model):
    __tablename__ = 'childs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    childname = db.Column(db.String(64), index=True)


class Parent(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    parent_name = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    parent_address = db.Column(db.String(64), index=True)
