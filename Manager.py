#!/usr/bin/env python
# coding=utf-8
from app import create_app
from app import db
Manager = create_app(db)

if __name__ == '__main__':
    Manager.run(debug=True)