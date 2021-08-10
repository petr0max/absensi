from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, DateField, DateTimeField,
                     IntegerField, TimeField)
from wtforms.validators import DataRequired, Length


class PermitForm(FlaskForm):
    long_date = IntegerField('Izin Berapa Hari', validators=[DataRequired()])
    start_date = DateField('Mulai Tanggal', validators=[DataRequired()])
    permit = StringField('Keperluan Izin', validators=[DataRequired(),
                                                       Length(1, 125)])


class CheckInForm(FlaskForm):
    tgl = DateField('Tanggal', validators=[DataRequired()])
    jam_datang = TimeField('Jam Datang', validators=[DataRequired()],
                           format='%H:%M')
