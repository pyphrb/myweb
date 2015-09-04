#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
