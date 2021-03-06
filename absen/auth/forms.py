from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                                                    Length(1, 64),
                                                    Email()])
    pass_hash = PasswordField('Kata Sandi', validators=[DataRequired()])
    remember_me = BooleanField('Ingat saya')
    submit = SubmitField('Masuk')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    pass_hash = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Password harus sama.')])
    password2 = PasswordField('Ulangi Password', validators=[DataRequired()])
    submit = SubmitField('Daftar')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email telah terdaftar.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username telah digunakan.')


class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('Password Lama', validators=[DataRequired()])
    pass_hash = PasswordField('Password Baru', validators=[
        DataRequired(), EqualTo('password2', message='Password harus sama.')])
    password2 = PasswordField('Ulangi Password', validators=[DataRequired()])
    submit = SubmitField('Ubah Password')


class ForgetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Kirim')


class ForgetPasswordForm(FlaskForm):
    pass_hash = PasswordField('Password Baru', validators=[
        DataRequired(), EqualTo('password2', message='Password harus sama.')])
    password2 = PasswordField('Ulangi Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')
