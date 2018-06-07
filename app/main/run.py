#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/6/7 13:26
author:    peak
description:
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()