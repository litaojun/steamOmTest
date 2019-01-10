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
            # sendReqByCode(code      = retcode,
            #               fileName  = dataPath,
            #               inputData = data)

def rtcdToReq(fileName = ""):
    casedataFilePath = casepath + os.sep + \
                       "testdata" + os.sep + \
                       "data"  + os.sep + fileName
    testdata = loadYamlFileData(filePath = casedataFilePath)
    return dict([(codedata["code"],codedata) for codedata in testdata["data"]])

def sendReqByCode(code = "100001",fileName = "",inputData = {} ):
    sendData  = rtcdToReq(fileName = fileName).get(code,None)
    if sendData is not None:
       testClass = allTestClass[sendData["apiInterface"]]
       casedata  = [1, 2, 3, 4, 5, sendData["data"].update(inputData), 7, 8]
       reqdata   = None
       if sendData["reqType"] == "data":
          reqdata = sendData["data"]
       testClass(methodName = "compareRetcodeTest",
                 param      =  casedata).myservice.sendHttpReq(reqdata = reqdata)


if __name__ == "__main__":
    checkTestData()