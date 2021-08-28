from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField,
                     SelectField, IntegerField, DateField)
from wtforms.validators import (DataRequired, Length, Email, Regexp,
                                NumberRange, Optional)
from . import profil


class EditProfileForm(FlaskForm):
    realname = StringField('Nama Lengkap', validators=[
        Length(0, 64),
        Regexp(r'^[A-Za-z\s\-\']+$', message='Upss... pakai huruf yah')])

    birthday = DateField('Tanggal Lahir')

    status_pegawai = SelectField('Status Kepegawaian', choices=[
        ('Pegawai Lepas', 'Pegawai Lepas'), ('Pegawai Tetap', 'Pegawai Tetap'),
        ('Tenaga Kerja Waktu Tertentu/Kontrak', 'Tenaga Kerja Waktu Tertentu/Kontrak')
    ])

    location = StringField('Lokasi Kantor', validators=[Length(0, 64)])

    about_me = TextAreaField('Tentang Saya', validators=[Length(0, 64)])

    study = SelectField('Universitas / Sekolah', choices=[
        ('SD', 'SD'), ('SMP', 'SMP'),
        ('SMA/SMK (Sederajat)', 'SMA/SMK (Sederajat)'),
        ('Diploma', 'Diploma'), ('Strata I', 'Strata I'),
        ('Strata II', 'Strata II'), ('Strata III', 'Strata III')
    ])

    jurusan = StringField('Jurusan', validators=[Length(0, 64)])

    gelar = StringField('Gelar Pendidikan', validators=[Length(0, 64)])

    address_before = StringField('Alamat Asal', validators=[Length(0, 64)])

    address_now = StringField('Alamat Sekarang', validators=[Length(0, 64)])

    blood = SelectField('Golongan Darah', choices=[
        ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'),
        ('Tidak Tahu', 'Tidak Tahu')])

    gender = SelectField('Jenis Kelamin', choices=[
        ('Pria', 'Pria'), ('Wanita', 'Wanita')])

    religion = SelectField('Agama', choices=[
        ('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Hindu', 'Hindu'),
        ('Budha', 'Budha'), ('Konghuchu', 'Konghuchu'), ('Lainnya', 'Lainnya')
    ])

    warga_negara = SelectField('Kewarganegaraan', choices=[
        ('Warga Negara Indonesia', 'Warga Negara Indonesia'),
        ('Warga Negara Asing', 'Warga Negara Asing')])

    married = SelectField('Status Menikah', choices=[
        ('Belum Nikah / Cerai', 'Belum Nikah / Cerai'),
        ('Belum Nikah / Cerai Memiliki Anak 1', 'Belum Nikah / Cerai Memiliki Anak 1'),
        ('Belum Nikah / Cerai Memiliki Anak 2', 'Belum Nikah / Cerai Memiliki Anak 2'),
        ('Belum Nikah / Cerai Memiliki Anak 3', 'Belum Nikah / Cerai Memiliki Anak 3'),
        ('Menikah Belum Memiliki Anak', 'Menikah Belum Memiliki Anak'),
        ('Menikah Memiliki Anak 1', 'Menikah Memiliki Anak 1'),
        ('Menikah Memiliki Anak 2', 'Menikah Memiliki Anak 2'),
        ('Menikah Memiliki Anak 3', 'Menikah Memiliki Anak 3')
    ])

    nama_pasangan = StringField('Nama Suami/Istri', validators=[Length(0, 64)])

    no_hp = IntegerField('No. Handphone', validators=[Optional()])

    nik = IntegerField('NIK KTP', validators=[Optional()])

    npwp = IntegerField('NPWP', validators=[Optional()])

    zone = SelectField('Zona Waktu', choices=[
        ('WIB', 'WIB'), ('WITA', 'WITA'), ('WIT', 'WIT')])

    submit = SubmitField('Ubah Data')
