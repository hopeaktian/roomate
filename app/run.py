#!/usr/bin/env python
#coding:utf-8
"""
file:.py
date:2018/6/7 13:26
author:    peak
description:
"""
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="袋鼠邻居")
@app.route('/login')
def login():
    return render_template('login.html', title="登陆  袋鼠邻居")

if __name__ == '__main__':
    app.run()
