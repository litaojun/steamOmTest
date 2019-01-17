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
from flask import jsonify,request
import sys
# from threading import Timer
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from steam.util.steamLog import SteamTestCase
import threading
from opg.unit.flaskRunMgr import genTestCaseByInterfaceOrCaseIds,runOneTestcase
from steam.runflask.util.initData import allTestCase,allTestClass,testSuite
from flask import Blueprint
from steam.runflask.dao.queryDbRunTestcase import queryTokenByPlanId
from opg.unit.flaskRunMgr import getRunTestTokenId,genAllTestCase,runAllTestCase
from opg.unit.flaskRunMgr import queryStateByTokenPro
from steam.runflask.tsdtmgr.testDataMnr import timeCheckData
bapp = Blueprint('tsrun', __name__)
timerSign = False
timer     = threading.Timer(60,timeCheckData)
@bapp.route("/prop/interfacelist", methods=['GET'])
def runOneTestCase():
    """
    执行一个指定的用例
    :return:
    """
    planId        = int(request.args.get("planId"))
    projectName   = request.args.get("projectname")
    caseId        = request.args.get("caseId")
    interfaceName = request.args.get("interfaceName")
    print("planId=%s,projectName=%s,caseId=%s,interfaceName=%s" %(planId,projectName,caseId,interfaceName))
    token         = queryTokenByPlanId(planId      = planId,
                                       projectName = projectName)
    testSuite     = genTestCaseByInterfaceOrCaseIds( allTestClass  = allTestClass ,
                                                     allCase       = allTestCase  ,
                                                     interfaceName = interfaceName,
                                                     caseIds       = [caseId] )
    runOneTestcase(suites      = testSuite,
                   planId      = planId,
                   token       = token,
                   title       = projectName,
                   description = "%s-用例测试情况" % projectName)

    return jsonify({
                        "code" : "000000",
                        "token": token
                   })

@bapp.route('/prop/runTestPro', methods=['GET'])
def start_steam_tasks():
    """
    执行所有用例
    :return:
    """
    projectName = request.args.get("projectname")
    retdata     = getRunTestTokenId(projectname = projectName)
    # testSuite   = genAllTestCase(allCase        = allTestCase,
    #                              allTestClass   = allTestClass)
    SteamTestCase.memberIdDict  = {}
    t = threading.Thread(target = runAllTestCase,
                         kwargs = {
                                        "suites" : testSuite,
                                        "title"  : projectName,
                                        "description" : "%s-用例测试情况" % projectName,
                                        "token"        :  retdata[0]
                                  }
                         )
    t.start()
    # tokenList.append(retdata[0])
    return jsonify({
                        'sign'  : "000000",
                        "token" : retdata[0],
                        "starttime" : retdata[1]
                   })

@bapp.route('/prop/queryRunProcess', methods=['GET'])
def query_run_state():
    """
    查询用例执行是否完成了
    :return:
    """
    """
        根据token查询用例执行是否完成
        :return:
    """
    token       = request.args.get("token")
    projectName = request.args.get("projectname")
    rtRunDt     = queryStateByTokenPro(projectName = projectName,
                                       token       = token)
    return jsonify(rtRunDt)

@bapp.route('/prop/timeCheckData', methods=['GET'])
def dataTimerCheck():
    global timerSign,timer
    rtJson = {"code":"100001" ,"msg":"定时任务已启动"}
    if not timerSign :
       print("定时器启动....")
       timer.start()
       timerSign = True
       rtJson    = {"code": "000000","msg": "定时任务启动成功"}
       print("定时器启动成功")
    return jsonify(rtJson)

if __name__ == "__main__":
    pass


