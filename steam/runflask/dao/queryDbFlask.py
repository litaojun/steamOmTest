#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryDbFlask.py 
@time: 2018/8/31 10:50 
"""
from opg.unit.flaskRunMgr import getDbManger
import uuid
from opg.util.timeTool import getNowTime
def getRunTestTokenId(projectname = "",starTime="sss"):
    dbManager = getDbManger()
    starttime = getNowTime()
    tokenId = uuid.uuid4()
    sqlstr  = "insert into test_run_process(token,starttime,status,projectname) value('%s','%s',1,'%s')" % (tokenId,starttime,projectname)
    dbManager.insertData(sql_insert=sqlstr)
    return  tokenId,starttime

def queryStateByTokenPro(projectName = "",token = ""):
    dbManager = getDbManger()
    keyls = ["id", "starttime", "status", "endtime", "projectname","hourtime","mintime","sectime"]
    querySql = """select  id, starttime, status, endtime, projectname ,HOUR(timediff(endtime , starttime)) hourtime ,minute(timediff(endtime , starttime)) mintime,SECOND(timediff(endtime , starttime)) sectime
                      from test_run_process p 
                      where p.projectname = "%s" 
                            and  p.token = "%s";""" % (projectName, token)
    dataList = dbManager.queryAll(sql=querySql)
    if dataList is not None and len(dataList) > 0:
        return dict(zip(keyls,dataList[0]))

def queryTestPlanList(projectName = ""):
    dbManager = getDbManger()
    keyls = ["id", "plantime", "projectname", "description"]
    querySql = """select id, plantime, projectname, description 
                  from test_plan p 
                  where projectname = "%s"   ;""" % projectName
    dataList = dbManager.queryAll(sql=querySql)
    retList  = [dict(zip(keyls,data)) for data in dataList]
    retDict = {}
    retDict["code"] = "000000"
    retDict["listplan"] = retList
    return retDict

def queryTestPlanByInterfaceName(interfaceName = "",planId = 22,db = None):
    dbManager = getDbManger()
    keyls = ["interfacename", "testcaseid", "testpoint", "result_sign","errordes"]
    querySql = """select  interfacename, testcaseid, testpoint, result_sign, errordes 
                  from test_case_record r	
                  where r.plan_id = %s and 
                        r.interfacename = '%s';""" % (planId,interfaceName)
    dataList = dbManager.queryAll(sql=querySql)
    retList  = [dict(zip(keyls,data)) for data in dataList]
    return retList

def queryTestPlanAllInterfaceName(interfaceName = "",planId = 22,db = None):
    dbManager = getDbManger()
    keyls = ["interfacename", "testcaseid", "testpoint", "resultSign","errordes"]
    querySql = """select  interfacename, testcaseid, testpoint, result_sign, errordes 
                  from test_case_record r	
                  where r.plan_id = %s ;""" % planId
    dataList = dbManager.queryAll(sql=querySql)
    if dataList is None:
        dataList = []
    retList  = [dict(zip(keyls,data)) for data in dataList]
    return retList

def queryTestPlanRecord(planId = 11):
    dbManager = getDbManger()
    keyls = ["interfaceName", "success", "fail", "error", "total"]
    querySql = """select  r.interfacename 'interfaceName',
							CONVERT(sum(case r.result_sign  when '0' then 1 else 0 end) ,SIGNED )  'success',
							CONVERT(sum(case r.result_sign  when '1' then 1 else 0 end),SIGNED )  'fail',
							CONVERT(sum(case r.result_sign  when '2' then 1 else 0 end),SIGNED )  'error',
			                CONVERT(sum(1),SIGNED )  'total'
			        from test_case_record r 
			        where r.plan_id = %s group by r.interfacename;""" % planId
    dataList = dbManager.queryAll(sql=querySql)
    if dataList is None:
       dataList = []
    retList = [dict(zip(keyls, data)) for data in dataList]
    return retList


def queryPlanDetailByInterfaceName(planId = 22):
    planRecordList = queryTestPlanRecord(planId=planId)
    allRecordList =queryTestPlanAllInterfaceName(planId=planId)
    for planRecord in planRecordList:
        interfaceName = planRecord["interfaceName"]
        interfacePlanRecord = [record for record in allRecordList if record["interfacename"] == interfaceName]
        planRecord["result"] = interfacePlanRecord
    retDict = {}
    retDict["code"] = "000000"
    retDict["testrst"] = planRecordList
    return  retDict


def queryTestResultByPlanIdOrCaseId(planId,caseId):
    sign = None
    querySql = """select result_sign from test_case_record r where r.plan_id = %s and r.testcaseid = "%s";""" %(planId,caseId)
    result = getDbManger().queryAll(sql = querySql)
    if result is not None:
        sign = result[0][0]
    return  sign