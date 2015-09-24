#!/usr/bin/env python
# coding=utf-8
import hashlib
from app import db
import hashlib
class Portscan(db.Model):
    vid = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), index=True)
    report = db.Column(db.TEXT)
    time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, ip, report):
        self.ip = ip
        self.report = hashlib.sha1(report).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.ip



