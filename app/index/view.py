#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'

from .import index
from flask import render_template
from model import NameFrom
@index.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameFrom()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index/index.html', form=form, name=name)