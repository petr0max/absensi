from .. import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), index=True)
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.Date(), default=datetime.date.today())
    last_seen = db.Column(db.DateTime(), default=datetime.datetime.now())
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
    profile_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    def ping(self):
        self.last_seen = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()
