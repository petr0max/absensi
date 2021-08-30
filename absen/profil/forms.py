from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField,
                     SelectField, IntegerField, DateField)
from wtforms.validators import (DataRequired, Length, Email, Regexp,
                                NumberRange, Optional, InputRequired)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from . import profil
from ..createform.models import Choice


class EditProfileForm(FlaskForm):

    def status_parent_choices():
        return Choice.query.filter(Choice.choice_id==12).all()

    def divisi_choices():
        return Choice.query.filter(Choice.choice_id==1).all()

    def jabatan_choices():
        return Choice.query.filter(Choice.choice_id==2).all()
 
    def kantor_choices():
        return Choice.query.filter(Choice.choice_id==3).all()

    def stat_emp_choices():
        return Choice.query.filter(Choice.choice_id==4).all()

    def last_study_choices():
        return Choice.query.filter(Choice.choice_id==5).all()
    
    def blood_choices():
        return Choice.query.filter(Choice.choice_id==7).all()
    
    def gender_choices():
        return Choice.query.filter(Choice.choice_id==6).all()

    def married_choices():
        return Choice.query.filter(Choice.choice_id==10).all()

    def religion_choices():
        return Choice.query.filter(Choice.choice_id==8).all()
    
    def country_choices():
        return Choice.query.filter(Choice.choice_id==9).all()

    def zone_time_choices():
        return Choice.query.filter(Choice.choice_id==14).all()

    def name_bank_choices():
        return Choice.query.filter(Choice.choice_id==11).all()

    nama_lengkap = StringField('Nama Lengkap', validators=[
        Length(0, 64),
        Regexp(r'^[A-Za-z\s\-\']+$', message='Upss... pakai huruf yah..')])

    tempat_lahir = StringField('Tempat Lahir', validators=[
        Length(0, 64),
        Regexp(r'^[A-Za-z\s\-\']+$', message='Upss... pakai huruf yah..')
    ])

    tanggal_lahir = DateField('Tanggal Lahir', validators=[DataRequired()])

    tentang_saya = TextAreaField('Tentang Saya', validators=[Length(0, 64)])

    divisi = QuerySelectField('Divisi', query_factory=divisi_choices,
                              allow_blank=True)

    jabatan = QuerySelectField('Jabatan', query_factory=jabatan_choices,
                               allow_blank=True)

    lokasi_kantor = QuerySelectField('Kantor', query_factory=kantor_choices,
                                     allow_blank=True)

    status_pegawai = QuerySelectField('Status Kepegawaian',
                                      query_factory=stat_emp_choices,
                                      allow_blank=True)

    pendidikan_terakhir = QuerySelectField('Pendidikan Terakhir',
                                           query_factory=last_study_choices,
                                           allow_blank=True)

    gelar_pendidikan = StringField('Gelar Pendidikan', validators=[Length(0, 64)])

    nama_almamater = StringField('Nama Almamater', validators=[Length(0, 64)])

    jurusan = StringField('Jurusan', validators=[Length(0, 64)])

    alamat_asal = TextAreaField('Alamat Asal', validators=[Length(0, 240)])

    alamat_domisili = TextAreaField('Alamat Domisili', validators=[Length(0, 240)])

    golongan_darah = QuerySelectField('Golongan Darah',
                                      query_factory=blood_choices,
                                      allow_blank=True)

    jenis_kelamin = QuerySelectField('Jenis Kelamin',
                                     query_factory=gender_choices,
                                     allow_blank=True)

    status_pernikahan = QuerySelectField('Status Pernikahan',
                                         query_factory=married_choices,
                                         allow_blank=True)

    nama_pasangan = StringField('Nama Suami/Istri', validators=[Length(0, 64)])

    agama = QuerySelectField('Agama', query_factory=religion_choices,
                             allow_blank=True)

    warga_negara = QuerySelectField('Warga Negara',
                                    query_factory=country_choices,
                                    allow_blank=True)

    nik = IntegerField('NIK KTP', validators=[Optional()])

    npwp = IntegerField('NPWP', validators=[Optional()])

    no_bpjs_ketenagakerjaan = IntegerField('No. BPJS Ketenagakerjaan',
                                           validators=[Optional()])

    no_bpjs_kesehatan = IntegerField('No. BPJS Kesehatan',
                                     validators=[Optional()])

    no_hp = IntegerField('No. Handphone', validators=[Optional()])

    zona_waktu = QuerySelectField('Zona Waktu', query_factory=zone_time_choices,
                                  allow_blank=True)

    nama_bank = QuerySelectField('Nama Bank', query_factory=name_bank_choices,
                                 allow_blank=True)
    nama_rekening = StringField('Nama Rekening', validators=[Length(0, 64)])

    no_rekening = IntegerField('Nomor Rekening', validators=[Optional()])

    # nama_anak = StringField('Nama Anak', validators=[Length(0, 64)])

    nama_wali = StringField('Nama Wali', validators=[Length(0, 64)])

    hubungan_wali = QuerySelectField('Hubungan Wali',
                                     query_factory=status_parent_choices,
                                     allow_blank=True)

    alamat_wali = TextAreaField('Alamat Wali', validators=[Length(0, 240)])
    
    no_kontak_wali = IntegerField('Nomor Kontak Wali', validators=[Optional()])

    submit = SubmitField('Ubah Data')
