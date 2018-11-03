#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: reportQuery.py 
@time: 2018/10/25 11:14 
"""
from flask import jsonify,request
import sys
sys.path.append("/home/nicepy/testhome/unittestExBaseb")
from steam.runflask.dao.queryDbFlask import queryTestResultByPlanIdOrCaseId
from steam.runflask.util.initData import allTestCase,allTestClass

from opg.unit.flaskRunMgr import queryTestPlanList,queryPlanDetailByInterfaceName
from flask import Blueprint
bapp = Blueprint('rptqy', __name__)
@bapp.route('/prop/testplanlist', methods=['GET'])
def query_planlist():
    """
        列出选择项目下所有测试执行计划列表
        :return:
    """
    projectName = request.args.get("projectname")
    return jsonify(queryTestPlanList(projectName = projectName))

@bapp.route('/prop/testappmap', methods=['GET'])
def query_plan_CaseRecord():
    """
        根据计划ID查询测试报告记录
        :return:
    """
    planid = request.args.get("planid")
    return jsonify(queryPlanDetailByInterfaceName(planId=planid))

@bapp.route('/prop/getOneTestcase', methods=['GET'])
def query_testCase():
    """
    根据interface,planId,caseId查询单个单个用例的详细信息
    :return:
    """
    interface  = request.args.get("interface")
    # methonName = request.args.get("methonName")
    caseId     = request.args.get("caseId")
    planId     = request.args.get("planId")
    resultSign = queryTestResultByPlanIdOrCaseId(planId = planId,
                                                 caseId = caseId)
    className  =  allTestClass[interface].__name__
    if interface in allTestCase:
       for methonName in allTestCase[interface]:
          for testcase in allTestCase[interface][methonName]:
              if testcase[0] == caseId:
                 if testcase is not None and len(testcase)==9:
                    testcase.append(className)
                    testcase.append(resultSign)
                 return jsonify(testcase)
    return "no data"