from .. import db
import datetime


class Permit(db.Model):
    __tablename__ = 'permits'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keterangan = db.Column(db.String(64), index=True)
    long_date = db.Column(db.Integer)
    start_date = db.Column(db.Date(), default=datetime.date.today())
    disetujui = db.Column(db.Boolean, default=False)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Absen(db.Model):
    __tablename__ = 'absens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dates = db.Column(db.Date())
    jam_datang = db.Column(db.Time())
    jam_pulang = db.Column(db.Time())
    keterangan = db.Column(db.String(64), index=True)
    #surat_sakit
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<{self.dates}>"
