#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: mediaresQueryTest.py 
@time: 2018/4/23 17:02 
"""
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from opg.unit.testcaseRunMgr import runTest
from flask import Blueprint
#https://www.cnblogs.com/freely/p/8022923.html
bapp = Blueprint('mediares', __name__)
def func():
	pass

@bapp.route('/testcase/runSteamTest', methods=['GET'])
def get_tasks():
	return "ssas"

class Main():
	def __init__(self):
		pass

if __name__ == "__main__":
	testResult = runTest(title=u"steam亲子教育", description=u"用例测试情况")
	import uuid
	a = uuid.uuid4()
	print(a)