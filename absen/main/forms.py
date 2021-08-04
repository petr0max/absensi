from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField,
                     SelectField)
from wtforms.validators import DataRequired, Length, Email, Regexp
from . import main
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('Coba input', validators=[DataRequired()])
    submit = SubmitField('Kirim')


class EditProfileForm(FlaskForm):
    name = StringField('Nama Lengkap', validators=[Length(0,64)])
    location = StringField('Lokasi', validators=[Length(0, 64)])
    about_me = TextAreaField('Tentang Saya')
    submit = SubmitField('Kirim')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                                Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Nama Lengkap', validators=[Length(0, 64)])
    location = StringField('Lokasi', validators=[Length(0, 64)])
    about_me = TextAreaField('Tentang Saya')
    submit = SubmitField('Kirim')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.filter_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
