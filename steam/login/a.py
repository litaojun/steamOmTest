#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: a.py 
@time: 2018/7/11 14:42 
"""
#coding=utf-8

from flask import Flask
from flask import request
import json

app = Flask(__name__)
testk = {
         "username":"litaojun",
         "passwd":"ffff"
         }

@app.route("/login", methods=["GET", "POST"])
def hello_str():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    else:
        username = request.args.get("username")
    jsonstr = json.dumps(testk)
    s = json.loads(jsonstr)
    return jsonstr



if __name__ == "__main__":
    app.run(port=8000, debug=True)