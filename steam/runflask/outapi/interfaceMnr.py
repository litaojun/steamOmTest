#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: interfaceMnr.py 
@time: 2018/10/25 10:33 
"""

from flask import Flask, jsonify,request
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from opg.unit.flaskRunMgr import queryAllInterfaceByProjectName
from flask import Blueprint
bapp = Blueprint('infcs', __name__)

@bapp.route("/prop/interfacelist", methods=['GET'])
def query_allInterface():
    """
        查询项目下的所有接口
        :return:
    """
    projectName = request.args.get("projectname")
    return jsonify(queryAllInterfaceByProjectName(projectName = projectName))