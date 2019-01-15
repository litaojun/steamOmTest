#!/usr/bin/env python  
# encoding: utf-8
from steam.runflask.util.initData import allTestClass
from steam.mockhttp.util.initFile import casepath
from opg.util.testcaseTool import loadYamlFileData
import os
def checkTestData():
    testdataFilePath = casepath + os.sep + "testdata" +\
                       os.sep   +  "testData.yml"
    testdata         = loadYamlFileData(filePath = testdataFilePath)
    for apiListData in testdata["testdata"]:
        apiInterface = apiListData["apiInterface"]
        testClass    = allTestClass[apiInterface]
        for data in apiListData["data"]:
            dataPath = data["dataPath"]
            casedata = [1,2,3,4,5,data,7,8]
            tc = testClass( methodName = "compareRetcodeTest" ,
                            param      = casedata )
            tc.getInputDataInit()
            retcode = tc.myservice.findTestdataByStatus()
            print("retcode = " + retcode)
            sendReqByCode(code      = retcode,
                          fileName  = dataPath,
                          inputData = data)

def rtcdToReq(fileName = ""):
    casedataFilePath = casepath    + os.sep + \
                       "testdata" + os.sep + \
                       "data"      + os.sep + fileName
    if not os.path.exists(casedataFilePath):
        return {}
    testdata = loadYamlFileData(filePath = casedataFilePath)
    return dict((codedata["code"],codedata) for codedata in testdata["data"])

def sendReqByCode( code = "100001",fileName = "",inputData = {} ):
    sendData  = rtcdToReq(fileName = fileName).get(code,None)
    if sendData is not None:
       testClass = allTestClass[sendData["apiInterface"]]
       sendData["data"].update(inputData)
       casedata  = [ 1, 2, 3, 4, 5,sendData["data"] , 7, 8 ]
       reqdata   = None
       if sendData["reqType"] == "data":
          reqdata = sendData["data"]
       tc = testClass(methodName = "compareRetcodeTest",
                      param      =  casedata)
       tc.getInputDataInit()
       tc.myservice.sendHttpReq(reqdata = reqdata)

if __name__ == "__main__":
   checkTestData()
   # sendReqByCode(code="100001",fileName="product1Goods.yml",inputData={})
   # sendReqByCode(code="100002", fileName="media2Media.yml", inputData={"resourceId": 5269})
   # sendReqByCode(code="100002", fileName="media3Media.yml", inputData={"resourceId": 5270})
   # sendReqByCode(code="100002", fileName="product1Goods.yml", inputData={"resourceId": 5271})
   # sendReqByCode(code="100002", fileName="course1Course.yml", inputData={"resourceId": 4542})
   # if ""  is None:
   #     print("ff")