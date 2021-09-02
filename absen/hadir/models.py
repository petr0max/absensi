from .. import db
import datetime


class Permit(db.Model):
    __tablename__ = 'permits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keterangan = db.Column(db.String(64), index=True)
    long_date = db.Column(db.Integer)
    start_date = db.Column(db.Date(), default=datetime.date.today())
    confirm_manager = db.Column(db.Boolean, default=False)
    agree_hrd = db.Column(db.Boolean, default=False)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.keterangan}'


class Absen(db.Model):
    __tablename__ = 'absens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    input_date = db.Column(db.DateTime(), default=datetime.datetime.now(),
                           unique=True)
    dates = db.Column(db.Date())
    jam_datang = db.Column(db.DateTime())
    jam_pulang = db.Column(db.DateTime())
    keterangan = db.Column(db.String(64), index=True)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<{self.dates}>"


class Sick(db.Model):
    __tablename__ = 'sicks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    input_date = db.Column(db.Date(), default=datetime.date.today())
    diagnosa = db.Column(db.String(64), index=True)
    long_date = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"{self.diagnosa.title()}"
