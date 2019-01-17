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
from opg.unit.flaskRunMgr import getDbManger
from steam.runflask.util.initData import allTestCase
# from opg.unit.flaskRunMgr import queryAllInterfaceByProjectName
from flask import Blueprint
bapp = Blueprint('infcs', __name__)
interfaceAliasList = allTestCase.keys()
@bapp.route("/prop/interfacelist", methods=['GET'])
def query_allInterface():
    """
        查询项目下的所有接口
        :return:
    """
    projectName = request.args.get("projectname")
    return jsonify(queryAllInterfaceByProjectName(projectName = projectName))

def queryAllInterfaceByProjectName(projectName = None):
    dbManager = getDbManger()
    keyls = ["aliasName","interfaceAddr","reqtype","module","mark","reqpath","rsppath","sign"]
    querySql = """select inf.aliasName,inf.interfaceNameAddr,inf.reqtype,CONCAT(mt.mtype,'-',mt.module ) as 'module',inf.mark,inf.reqDataPath,inf.rspDataPath ,0 
                  from interface_mgr inf,module_type mt  
                  where inf.projectname = "%s" and inf.module = mt.module  order by mt.sortsign;""" % projectName
    dataList = dbManager.queryAll(sql = querySql)
    if dataList is None:
       dataList = [ ]
    retList = [ dict(zip(keyls, data)) for data in dataList ]
    for data in retList:
        if data["aliasName"] in interfaceAliasList:
           data["sign"] = 1
    #sorted(retList,key = lambda a:  a["sign"] )
    retList.sort(key = lambda a:a["sign"],reverse=True)
    retdata = {
                 "code":"000000",
                 "infsList":retList
               }
    return retdata