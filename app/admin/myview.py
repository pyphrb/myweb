#!/usr/bin/python
# coding=utf8
__author__ = 'pyphrb'
from flask_admin import Admin, BaseView, expose
from flask import request, redirect, url_for,render_template,flash
from flask import template_rendered
from .model import RegistrationForm
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/xx.html')
    @expose('/resign/', methods=['GET', 'POST'])
    def resign(self):
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User(form.username.data, form.email.data,
                        form.password.data)
            db_session.add(user)
            flash('Thanks for registering')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)