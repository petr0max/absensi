from .. import db
import datetime


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_lengkap = db.Column(db.String(64), index=True)
    tempat_lahir = db.Column(db.String(64), index=True)
    tanggal_lahir = db.Column(db.Date(), default=datetime.date.today())
    tentang_saya = db.Column(db.Text())
    divisi = db.Column(db.String(64), index=True)
    jabatan = db.Column(db.String(64), index=True)
    lokasi_kantor = db.Column(db.String(64), index=True)
    status_pegawai = db.Column(db.String(64), index=True)
    pendidikan_terakhir = db.Column(db.String(64), index=True)
    gelar_pendidikan = db.Column(db.String(64), index=True)
    nama_almamater = db.Column(db.String(64), index=True)
    jurusan = db.Column(db.String(64), index=True)
    alamat_asal = db.Column(db.String(240), index=True)
    alamat_domisili = db.Column(db.String(240), index=True)
    golongan_darah = db.Column(db.String(64), index=True)
    jenis_kelamin = db.Column(db.String(64), index=True)
    status_pernikahan = db.Column(db.String(64), index=True)
    nama_pasangan = db.Column(db.String(64), index=True)
    agama = db.Column(db.String(64), index=True)
    warga_negara = db.Column(db.String(64), index=True)
    nik = db.Column(db.BigInteger, index=True, unique=True)
    npwp = db.Column(db.String(240), index=True, unique=True)
    no_bpjs_ketenagakerjaan = db.Column(db.Integer, index=True, unique=True)
    no_bpjs_kesehatan = db.Column(db.Integer, index=True, unique=True)
    no_hp = db.Column(db.Integer, index=True)
    zona_waktu = db.Column(db.String(64), index=True)

    # Create Bank account detail
    nama_bank = db.Column(db.String(64), index=True)
    nama_rekening = db.Column(db.String(64), index=True)
    no_rekening = db.Column(db.Integer, index=True)
    
    nama_wali = db.Column(db.String(64), index=True)
    hubungan_wali = db.Column(db.String(64), index=True)
    alamat_wali = db.Column(db.String(240), index=True)
    no_kontak_wali = db.Column(db.Integer, index=True)

    member_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    child_id = db.Column(db.Integer, db.ForeignKey('childs.id'))

    def __repr__(self):
        return f"{self.nama_lengkap}"


class Child(db.Model):
    __tablename__ = 'childs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    nama_anak = db.Column(db.String(64), index=True)
    
    profiles = db.relationship('Profile', backref='child', lazy='dynamic')

    def __repr__(self):
        return f"{self.nama_anak}"
