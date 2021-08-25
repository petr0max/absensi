from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateField, DateTimeField,
                     IntegerField, TimeField)
from wtforms.validators import DataRequired, Length


class PermitForm(FlaskForm):
    long_date = IntegerField('Izin Berapa Hari', validators=[DataRequired()])
    start_date = DateField('Mulai Tanggal', validators=[DataRequired()])
    keterangan = StringField('Keperluan Izin', validators=[DataRequired(),
                                                       Length(1, 125)])
    submit = SubmitField('Kirim')


class CheckInForm(FlaskForm):
    dates = DateField('Tanggal', validators=[DataRequired()])
    jam_datang = TimeField('Jam Datang', validators=[DataRequired()],
                           format='%H:%M')
    submit = SubmitField('Kirim')


class CheckOutForm(FlaskForm):
    dates = DateField('Tanggal', validators=[DataRequired()])
    jam_pulang = TimeField('Jam Pulang', validators=[DataRequired()])
    keterangan = StringField('Keterangan',
                             validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Kirim')


class SickForm(FlaskForm):
    dates = DateField('Tanggal', validators=[DataRequired()])
    keterangan = StringField('Diagnosa', validators=[DataRequired(),
                                                   Length(1, 64)])
    submit = SubmitField('Kirim')
