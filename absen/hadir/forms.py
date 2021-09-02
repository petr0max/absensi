from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateField, DateTimeField,
                     IntegerField, TimeField, BooleanField)
from wtforms.validators import DataRequired, Length, Optional


class PermitForm(FlaskForm):
    long_date = IntegerField('Izin Berapa Hari', validators=[DataRequired()])
    start_date = DateField('Mulai Tanggal', validators=[DataRequired()])
    keterangan = StringField('Keperluan Izin', validators=[DataRequired(),
                                                       Length(1, 125)])
    submit = SubmitField('Kirim')

class PermitConfirmForm(FlaskForm):
    checkbox = BooleanField("Disetujui ?")
    submit = SubmitField('Kirim')


class CheckInForm(FlaskForm):
    dates = DateField('Tanggal', validators=[DataRequired()])
    jam_input = TimeField('Jam Datang', validators=[DataRequired()],
                           format='%H:%M')
    submit = SubmitField('Kirim')


class CheckOutForm(FlaskForm):
    dates = DateField('Tanggal', validators=[DataRequired()])
    jam_pulang = TimeField('Jam Pulang', validators=[DataRequired()],
                           format='%H:%M')
    keterangan = StringField('Keterangan',
                             validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Kirim')


class SickForm(FlaskForm):
    input_date = DateField('Tanggal', validators=[DataRequired()])
    diagnosa = StringField('Diagnosa', validators=[DataRequired(),
                                                   Length(1, 64)])
    long_date = IntegerField('Izin Hari', validators=[Optional()])
    submit = SubmitField('Kirim')
