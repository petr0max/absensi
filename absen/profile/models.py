from .. import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(64), index=True)
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    study = db.Column(db.String(64), index=True)
    jurusan = db.Column(db.String(64), index=True)
    gelar = db.Column(db.String(64), index=True)
    address_before = db.Column(db.String(64), index=True)
    address_now = db.Column(db.String(64), index=True)
    blood = db.Column(db.String(64), index=True)
    religion = db.Column(db.String(64), index=True)
    warga_negara = db.Column(db.String(64), index=True)
    nik = db.Column(db.Integer, index=True)
    npwp = db.Column(db.Integer, index=True)
    no_hp = db.Column(db.Integer, index=True)
    zone = db.Column(db.String(64), index=True)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
