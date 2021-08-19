from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, TextAreaField,
                     SelectField, IntegerField)
from wtforms.validators import (DataRequired, Length, Email, Regexp, 
                                NumberRange, Optional)
from . import main


class NameForm(FlaskForm):
    name = StringField('Coba input', validators=[DataRequired()])
    submit = SubmitField('Kirim')
