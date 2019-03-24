from opg.util.dbtools import Database
from steam.mockhttp.util.initFile import generateUrlToFilePath
from opg.unit.loader import initAllTestClass
# from steam.runflask.util.initData import allTestClass
allTestClass = initAllTestClass()
allInterfacesData = generateUrlToFilePath()
def genNullTestCaseByInterface():
    retList = []
    # allInterfaceList = allInterfacesData.keys()
    for interfaceName in allInterfacesData:
        if interfaceName not in allTestClass:
            retList.append({ "total":0, "success":0 , "fail":0, "error":0 ,"interfaceName":interfaceName, "result": [] })
    return retList

def queryPlanDetailByInterfaceName(planId = 22):
    planRecordList = queryTestPlanRecord(planId=planId)
    allRecordList  = queryTestPlanAllInterfaceName(planId=planId)
    for planRecord in planRecordList:
        interfaceName         = planRecord["interfaceName"]
        interfacePlanRecord   = [record for record in allRecordList if record["interfacename"] == interfaceName]
        planRecord["result"] = interfacePlanRecord
    #加入未实现自动化用例的接口，空用例
    nullIfsTestcaseList = genNullTestCaseByInterface()
    planRecordList.extend(nullIfsTestcaseList)
    retDict = {}
    retDict["code"] = "000000"
    retDict["testrst"] = planRecordList
    return  retDict

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
    dataList = dbManager.queryAll(sql=querySql,dbName="ltjtest")
    if dataList is None:
       dataList = []
    retList = [dict(zip(keyls, data)) for data in dataList]
    return retList


def queryTestPlanAllInterfaceName(interfaceName = "",planId = 22,db = None):
    dbManager = getDbManger()
    keyls = ["interfacename", "testcaseid", "testpoint", "resultSign","errordes"]
    querySql = """select  interfacename, testcaseid, testpoint, result_sign, errordes 
                  from test_case_record r	
                  where r.plan_id = %s ;""" % planId
    dataList = dbManager.queryAll(sql=querySql,dbName="ltjtest")
    if dataList is None:
        dataList = []
    retList  = [dict(zip(keyls,data)) for data in dataList]
    return retList

def getDbManger():
    return Database()


def queryTestPlanList(projectName = ""):
    dbManager = getDbManger()
    keyls = ["id", "plantime", "projectname", "description"]
    querySql = """select id, plantime, projectname, description 
                  from test_plan p 
                  where projectname = "%s"   ;""" % projectName
    dataList = dbManager.queryAll(sql=querySql,dbName="ltjtest")
    retList  = [dict(zip(keyls,data)) for data in dataList]
    retDict = {}
    retDict["code"] = "000000"
    retDict["listplan"] = retList
    return retDict

