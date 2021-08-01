from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Alamat Email', validators=[DataRequired(),
                                                    Length(1, 64),
                                                    Email()])
    password = PasswordField('Kata Sandi', validators=[DataRequired()])
    remember_me = BooleanField('Ingat saya')
    submit = SubmitField('Masuk')
