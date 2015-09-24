__author__ = 'pyphrb'
from flask_wtf import Form
from wtforms import validators
from  wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

class NameFrom(Form):

    name = StringField('What is your name?', [validators.Length(min=4, max=25)])
    password = StringField('What is your PASSWORD?', [validators.Length(min=4, max=25)])
    submit = SubmitField('Submit')