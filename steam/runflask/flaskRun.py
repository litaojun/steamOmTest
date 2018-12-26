#!/usr/bin/env python  
# encoding: utf-8  
from flask import Flask, jsonify,request
from steam.runflask.outapi import interfaceMnr,testcaseRun,reportQuery
from flask_cors import *
from steam.mockhttp.util.initFile import ip
import sys
from steam.util.steamLog import SteamTestCase
from flask import render_template
from steam.runflask.dao.queryDbFlask import queryTestResultByPlanIdOrCaseId
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from opg.unit.flaskRunMgr import queryStateByTokenPro,queryTestPlanList,queryPlanDetailByInterfaceName
import threading
from opg.unit.flaskRunMgr import getRunTestTokenId,genAllTestCase,runAllTestCase
from steam.runflask.util.initData import allTestCase,allTestClass,tokenList
app = Flask(__name__,template_folder='templates',static_url_path='/static/')
CORS(app, supports_credentials=True)
# app.register_blueprint(mediaresQueryTest.bapp , url_prefix = "/mediares")
app.register_blueprint( interfaceMnr.bapp,       url_prefix = "/infcs"   )
app.register_blueprint( testcaseRun.bapp,        url_prefix = "/tsrun"   )
app.register_blueprint( reportQuery.bapp,        url_prefix = "/rptqy"   )

@app.route('/prop/runTestPro', methods=['GET'])
def start_steam_tasks():
    projectName = request.args.get("projectname")
    retdata     = getRunTestTokenId(projectname = projectName)
    testSuite   = genAllTestCase(allCase        = allTestCase,
                                 allTestClass   = allTestClass)
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
    tokenList.append(retdata[0])
    return jsonify({
                        'sign'  : "000000",
                        "token" : retdata[0],
                        "starttime" : retdata[1]
                   })

@app.route('/prop/queryRunProcess', methods=['GET'])
def query_run_state():
    """
        根据token查询用例执行是否完成
        :return:
    """
    token       = request.args.get("token")
    projectName = request.args.get("projectname")
    rtRunDt     = queryStateByTokenPro(projectName = projectName,
                                       token       = token)
    return jsonify(rtRunDt)

@app.route('/prop/testplanlist', methods=['GET'])
def query_planlist():
    """
        列出选择项目下所有测试执行计划列表
        :return:
    """
    projectName = request.args.get("projectname")
    return jsonify(queryTestPlanList(projectName = projectName))

@app.route('/prop/getOneTestcase', methods=['GET'])
def query_testCase():
    """
        根据interface,planId,caseId查询单个单个用例的详细信息
        :return:
    """
    interface  = request.args.get("interface")
    methonName = request.args.get("methonName")
    caseId     = request.args.get("caseId")
    planId     = request.args.get("planId")
    resultSign = queryTestResultByPlanIdOrCaseId(planId = planId,
                                                 caseId = caseId)
    className  =  allTestClass[interface].__name__
    if interface in allTestCase:
       if methonName in allTestCase[interface]:
          for testcase in allTestCase[interface][methonName]:
              if testcase[0] == caseId:
                 if testcase is not None and len(testcase)==9:
                    testcase.append(className)
                    testcase.append(resultSign)
                 return jsonify(testcase)
    return "no data"

def stop_test_run():
    global testSuite
    testSuite = None
    return jsonify({
                        'code': "000000"
                   })

@app.route('/', methods=['GET'])
def hello_world():
    return render_template( "pytest.html", content="hello flask " )


@app.route('/local', methods=['GET'])
def hello_world_local():
    return render_template( "pytestlocal.html", ipStr = ip )

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True,port=8181)