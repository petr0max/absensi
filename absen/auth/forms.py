from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
form wtforms.validators import Datarequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Alamat Email', validators=[Datarequired(),
                                                    Length(1, 64),
                                                    Email()])
    password = PasswordField('Kata Sandi', validators=[Datarequired()])
    remember_me = BooleanField('Ingat saya')
    submit = SubmitField('Masuk')
