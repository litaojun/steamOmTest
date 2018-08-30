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
import copy
from flask import Flask, jsonify,request
from steam.mediares.query import mediaresQueryTest
from flask_cors import *
import sys
from flask import render_template
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
#from opg.unit.testcaseRunMgr import runTest
from opg.unit.flaskRunMgr import runTest,queryStateByTokenPro,queryTestPlanList,queryPlanDetailByInterfaceName
import threading
from opg.unit.flaskRunMgr import getRunTestTokenId,initAllTestCase,initAllTestClass,genAllTestCase,runAllTestCase
app = Flask(__name__,template_folder='templates',static_url_path='/static/')
CORS(app, supports_credentials=True)
app.register_blueprint(mediaresQueryTest.bapp,url_prefix="/mediares")
sign = True
testSuite = None
if sign :
    allTestClass = initAllTestClass()
    allTestCase  = initAllTestCase()
    #testSuite    = genAllTestCase(allCase=allTestCase,allTestClass=allTestClass)
    tokenList = []
    sign = False
@app.route('/prop/runtestplan', methods=['GET'])
def start_tasks():
    projectName = request.args.get("projectname")
    retdata = getRunTestTokenId(projectname=projectName)
    t = threading.Thread(target = runTest,
                         kwargs = {
                                         "title":projectName,
                                         "description":"%s-用例测试情况" % projectName,
                                         "token":retdata[0]
                                   }
                         )
    t.start()
    return jsonify({
                        'sign'  : "000000",
                        "token" : retdata[0],
                        "starttime" : retdata[1]
                   })

@app.route('/prop/runTestPro', methods=['GET'])
def start_steam_tasks():
    projectName = request.args.get("projectname")
    retdata = getRunTestTokenId(projectname=projectName)
    testSuite = genAllTestCase(allCase=allTestCase, allTestClass=allTestClass)
    t = threading.Thread(target = runAllTestCase,
                         kwargs = {
                                        "suites" : testSuite,
                                         "title" : projectName,
                                         "description" : "%s-用例测试情况" % projectName,
                                         "token"        :  retdata[0]
                                   }
                         )
    t.start()
    tokenList.append(retdata[0])
    return jsonify({
                        'sign'  : "000000",
                        "token" : retdata[0],
                        "starttime" : retdata[1]
                   })

@app.route('/prop/queryRunProcess', methods=['GET'])
def query_run_state():
    token       = request.args.get("token")
    projectName = request.args.get("projectname")
    return jsonify(queryStateByTokenPro(projectName = projectName,
                                        token       = token))

@app.route('/prop/testplanlist', methods=['GET'])
def query_planlist():
    projectName = request.args.get("projectname")
    return jsonify(queryTestPlanList(projectName = projectName))

@app.route('/prop/testappmap', methods=['GET'])
def query_plan_CaseRecord():
    planid = request.args.get("planid")
    return jsonify(queryPlanDetailByInterfaceName(planId=planid))

@app.route('/prop/getOneTestcase', methods=['GET'])
def query_testCase():
    interface = request.args.get("interface")
    methonName = request.args.get("methonName")
    caseId = request.args.get("caseId")
    print("%s-%s-%s" % (interface,methonName,caseId))
    if interface in allTestCase:
        if methonName in allTestCase[interface]:
            for testcase in allTestCase[interface][methonName]:
                if testcase[0] == caseId:
                    return jsonify(testcase)
    return "no data"

def stop_test_run():
    testSuite = None
    return jsonify({
                        'code': "000000"
                   })

@app.route('/')
def hello_world():
    return render_template("pytest.html", content="hello flask ")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8181)