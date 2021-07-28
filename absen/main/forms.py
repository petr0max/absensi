from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from . import main


class NameForm(FlaskForm):
    name = StringField('Coba input', validators=[DataRequired()])
    submit = SubmitField('Kirim')
