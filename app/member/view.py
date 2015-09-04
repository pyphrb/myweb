#!/usr/bin/env python
# coding=utf-8
__author__ = 'pyphrb'
from .import member

@member.route('/')
def member():
    return 'admin'