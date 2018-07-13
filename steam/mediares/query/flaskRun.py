#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: flaskRun.py 
@time: 2018/7/11 15:09 
"""
#!flask/bin/python
from flask import Flask, jsonify,request
from steam.mediares.query import mediaresQueryTest
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
#from opg.unit.testcaseRunMgr import runTest
from opg.unit.flaskRunMgr import runTest
import threading
app = Flask(__name__)
app.register_blueprint(mediaresQueryTest.bapp,url_prefix="/mediares")

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/testcase/runSteamTest', methods=['GET'])
def get_tasks():
    starttime = request.args.get("starttime")
    t = threading.Thread(target=runTest,
                         kwargs={
                                     "title":u"steam亲子教育",
                                     "description":u"用例测试情况",
                                     "starTime": starttime
                                 }
                         )
    t.start()
    return jsonify({'sign': "000000"})

if __name__ == '__main__':
    app.run(debug=True)