#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.data_required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.data_required()])