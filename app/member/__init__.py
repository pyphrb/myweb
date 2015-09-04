#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from flask import Blueprint
member = Blueprint('member', __name__, template_folder='templates')
from .import view
