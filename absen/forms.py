from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from absen.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('Tentang Saya', validators=[Length(min=0, max=140)])
    submit = SubmitField('Ubah')

class LoginForm(FlaskForm):
    username = StringField('Nama Pengguna', validators=[DataRequired()])
    password = PasswordField('Kata Kunci', validators=[DataRequired()])
    remember_me = BooleanField('Ingat Saya')
    submit = SubmitField('Masuk')


class RegistrationForm(FlaskForm):
    username = StringField('Nama Pengguna', validators=[DataRequired()])
    email = StringField('Alamat Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Ulangi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Buat Akun')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Silahkan menggunakan akun yang lain.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Silahkan menggunakan email yang lain.')