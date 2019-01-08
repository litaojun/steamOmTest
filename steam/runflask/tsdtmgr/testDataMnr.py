#!/usr/bin/env python  
# encoding: utf-8
""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: testDataMnr.py 
@time: 2019/1/7 11:36 
"""
from steam.runflask.util.initData import testSuite,allTestClass
from steam.mockhttp.util.initFile import casepath
from opg.util.testcaseTool import loadYamlFileData
import os
def checkTestData():
    testdataFilePath = casepath + os.sep + "testdata" + os.sep + "testData.yml"
    testdata         = loadYamlFileData(filePath = testdataFilePath)
    for apiListData in testdata["testdata"]:
        apiInterface = apiListData["apiInterface"]
        testClass    = allTestClass[apiInterface]
        for data in apiListData["data"]:
            dataPath = data["dataPath"]
            casedata = [1,2,3,4,5,data,7,8]
            retcode = testClass(methodName = "compareRetcodeTest",
                                param      = casedata).myservice.findTestdataByStatus()
            if retcode == "000000":
                pass
            elif retcode == "100001":
                pass
            elif retcode == "100002":
                pass

