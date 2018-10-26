#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: testcaseRun.py 
@time: 2018/10/25 10:34 
"""
from flask import Flask, jsonify,request
from steam.mediares.query import mediaresQueryTest
from steam.runflask.outapi import interfaceMnr,testcaseRun
from flask_cors import *
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from opg.unit.flaskRunMgr import queryStateByTokenPro,queryTestPlanList,queryPlanDetailByInterfaceName
import threading
from opg.unit.flaskRunMgr import genTestCaseByInterfaceOrCaseIds,runOneTestcase
from steam.runflask.util.initData import allTestCase,allTestClass
from flask import Blueprint
from steam.runflask.dao.queryDbRunTestcase import queryTokenByPlanId

bapp = Blueprint('tsrun', __name__)
@bapp.route("/prop/interfacelist", methods=['GET'])
def runOneTestCase():
    planId        = int(request.args.get("planId"))
    projectName   = request.args.get("projectname")
    caseId        = request.args.get("caseId")
    interfaceName = request.args.get("interfaceName")[28:]
    print("planId=%s,projectName=%s,caseId=%s,interfaceName=%s" %(planId,projectName,caseId,interfaceName))
    token         = queryTokenByPlanId(planId      = planId,
                                       projectName = projectName)
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = allTestClass ,
                                                     allCase       = allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = [caseId] )
    runOneTestcase(suites=testSuite,planId=planId,token=token,title=projectName,description="%s-用例测试情况" % projectName)
    # t = threading.Thread(target = runOneTestcase,
    #                      kwargs = {
    #                                     "suites" : testSuite,
    #                                     "planId" : planId ,
    #                                     "title"  : projectName,
    #                                     "description" : "%s-用例测试情况" % projectName,
    #                                     "token"        :  token
    #                               }
    #                      )
    # t.start()
    return jsonify({
                        "code" : "000000",
                        "token": token
                   })

if __name__ == "__main__":
    pass


