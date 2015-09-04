__author__ = 'pyphrb'
from flask_wtf import Form
from  wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameFrom(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')