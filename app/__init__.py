#!/usr/bin/env python
# coding=utf-8
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .index import index as index_blueprint
from .member import member as member_blueprint
from .admin import myview
from flask_admin import Admin
from flask import request
from flask_login import LoginManager

db = SQLAlchemy()
def create_app(db):
    app = Flask(__name__)
    app.register_blueprint(index_blueprint, url_prefix='/')
    app.register_blueprint(member_blueprint, url_prefix='/member/')
    app.config['SECRET_KEY'] = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wangqi@localhost/myweb'
    login = LoginManager()
    bootstrap = Bootstrap()
    admin = Admin(name="APP admin", template_mode='bootstrap3')
    admin.add_view(myview.MyView(name='Hello'))
    admin.init_app(app)
    bootstrap.init_app(app)
    login.init_app(app)
    db.init_app(app)
    return app
