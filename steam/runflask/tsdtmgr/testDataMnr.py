#!/usr/bin/env python  
# encoding: utf-8
from steam.runflask.util.initData import allTestClass
from opg.util.lginfo import selectFh
from steam.mockhttp.util.initFile import casepath
from opg.bak.testcaseTool import loadYamlFileData
from opg.unit.runtest import genDir,writeLog
import os
sh = None
def checkTestData():
    from opg.util.timeTool import getNowTime, getTwoFmtTime
    global sh
    datetime,logtime = getTwoFmtTime()
    logDir = genDir(logtime)
    writeDir = writeLog(wtrDir=logDir)
    sh = writeDir("checkTestData.log")
    selectFh(sh)
    testdataFilePath = casepath + os.sep + "testdata" + \
                       os.sep   +  "testData.yml"
    testdata         = loadYamlFileData(filePath = testdataFilePath)
    sign = True
    for apiListData in testdata["testdata"]:
        apiInterface = apiListData["apiInterface"]
        testClass    = allTestClass[apiInterface]
        for data in apiListData["data"]:
            dataPath = data["dataPath"]
            casedata = [1,2,3,4,5,data,7,8]
            tc = testClass( methodName = "compareRetcodeTest" ,
                            param      = casedata )
            checkCode = tc.myservice.findTestdataByStatus()
            print("checkCode = " + checkCode)
            if checkCode != "000000":
               sign = False
            retcode = sendReqByCode(code       = checkCode,
                                    fileName   = dataPath,
                                    inputData  = data)
            if retcode == "211111":
               print("无需重建")
            elif retcode == "000000":
               print("重建数据成功")
            elif retcode == "200001":
                print("重建中返回报文数据异常")
            else:
                print("重建出错，对应返回码为%s" % retcode)
    selectFh(sh,False)
    return sign


def rtcdToReq(fileName = ""):
    casedataFilePath = casepath    + os.sep + \
                       "testdata" + os.sep + \
                       "data"      + os.sep + fileName
    if not os.path.exists(casedataFilePath):
        return {}
    testdata = loadYamlFileData(filePath = casedataFilePath)
    return dict((codedata["code"],codedata) for codedata in testdata["data"])

def sendReqByCode( code = "100001",fileName = "",inputData = {} ):
    #return "211111"：无需重建，"000000":重建成功,"2000001":重建返回报文异常，其它:对应返回错误码
    sendData  = rtcdToReq(fileName = fileName).get(code,None)
    retcode = "211111"
    if sendData is not None:
       testClass = allTestClass[sendData["apiInterface"]]
       sendData["data"].update(inputData)
       casedata  = [ 1, 2, 3, 4, 5,sendData["data"] , 7, 8 ]
       reqdata   = None
       if sendData["reqType"] == "data":
          reqdata = sendData["data"]
       tc = testClass(methodName = "compareRetcodeTest",
                      param      =  casedata)
       # tc.getInputDataInit()
       tc.myservice.sendHttpReq(reqdata = reqdata)
       retcode = tc.myservice.getRetcodeByRsp()
    return retcode

def timeCheckData():
    print("timeCheckData start run ......")
    num = 1
    while(True):
        sign = checkTestData()
        num += 1
        if sign or num > 3 :
           break
    print("timeCheckData end run")

if __name__ == "__main__":
   checkTestData()
   # sendReqByCode(code="100001",fileName="product1Goods.yml",inputData={})
   # sendReqByCode(code="100002", fileName="media2Media.yml", inputData={"resourceId": 5269})
   # sendReqByCode(code="100002", fileName="media3Media.yml", inputData={"resourceId": 5270})
   # sendReqByCode(code="100002", fileName="product1Goods.yml", inputData={"resourceId": 5271})
   # sendReqByCode(code="100002", fileName="course1Course.yml", inputData={"resourceId": 4542})
   # if ""  is None:
   #     print("ff")