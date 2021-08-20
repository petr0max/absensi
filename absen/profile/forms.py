from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField,
                     SelectField, IntegerField)
from wtforms.validators import (DataRequired, Length, Email, Regexp,
                                NumberRange, Optional)
from . import profile


class EditProfileForm(FlaskForm):
    realname = StringField('Nama Lengkap', validators=[
        Length(0, 64),
        Regexp(r'^[A-Za-z\s\-\']+$', 0, 'Upss... pakai huruf yah')])
    location = StringField('Lokasi Kantor', validators=[Length(0, 64)])
    about_me = TextAreaField('Tentang Saya', validators=[Length(0, 64)])
    study = StringField('Universitas / Sekolah', validators=[Length(0, 64)])
    jurusan = StringField('Jurusan', validators=[Length(0, 64)])
    gelar = StringField('Gelar Pendidikan', validators=[Length(0, 64)])
    address_before = StringField('Alamat Asal', validators=[Length(0, 64)])
    address_now = StringField('Alamat Sekarang', validators=[Length(0, 64)])
    blood = SelectField('Golongan Darah', choices=[
        ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    gender = SelectField('Jenis Kelamin', choices=[
        ('Pria', 'Pria'), ('Wanita', 'Wanita')
    ])
    religion = StringField('Agama', validators=[Length(0, 64)])
    warga_negara = SelectField('Kewarganegaraan', choices=[
        ('WNI', 'WNI'), ('WNA', 'WNA')])
    married = SelectField('Status Nikah', choices=[
        ('Menikah', 'Menikah'), ('Belum Nikah / Cerai', 'Belum Nikah / Cerai')
    ])
    no_hp = IntegerField('No. Handphone', validators=[Optional()])
    nik = IntegerField('NIK', validators=[Optional()])
    npwp = IntegerField('NPWP', validators=[Optional()])
    zone = SelectField('Zona Waktu', choices=[
        ('WIB', 'WIB'), ('WITA', 'WITA'), ('WIT', 'WIT')])
    submit = SubmitField('Ubah Data')
