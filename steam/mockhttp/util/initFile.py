#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: initFile.py 
@time: 2018/11/7 14:07 
"""
import os
import yaml
import collections
from configparser import ConfigParser
cf=ConfigParser(allow_no_value=True)
cf.read(os.sep.join([os.getcwd() ,"steam","mockhttp",  "jsonfile" , "config.ini"]))

basePath = cf.get('path', 'basepath')
urldata = collections.defaultdict(lambda :{})
def loadFileData():
    filePath = os.sep.join([basePath  , "testjson.yml"])
    return loadYamlFileData(filePath = filePath)

def loadYamlFileData(filePath = None):
    print("filepath = %s " % filePath)
    with open(filePath, 'r',encoding="utf-8") as f:
        ymldata = yaml.load(f.read())
        print("ymldata = %s " % ymldata)
        return ymldata

def generateUrlToFilePath():
    ymldata  = loadFileData()
    # basePath = os.getcwd()
    for urltype in ymldata["steam"]:
        data = traverseFileData(ymldata, urltype)
        for url in data:
            urldata[url] = data[url]
    return urldata

def traverseFileData(ymldata,dir):
    filedata = ymldata["steam"][dir]
    rtdata = collections.defaultdict(lambda :{})
    # basePath = ymldata["config"]["basepath"]
    # basePath
    dir = [basePath,"steam",dir]
    for curdir in filedata:
        for pathurl in  filedata[curdir]:
            data    = filedata[curdir][pathurl]
            method  = data["method"]
            url     = data["url"]
            # format  = data["formatone"]
            # tempdir = dir + [curdir,format]
            pathdict = {}
            for key in data:
                if key != "method":
                   pathdict[key] = [os.sep.join(dir + [curdir, filename]) for filename in data[key]]
            rtdata[pathurl] = [method, pathdict,url]
    return rtdata

def generateDelayTimeConfig():
    return cf["delay"]["time"]

if __name__ == "__main__":
   filePath = "D:\litaojun\steamyml\matchAppleTestCase.yml"
   ymldata = loadYamlFileData(filePath = filePath)
   print(ymldata)
   tdict = collections.defaultdict(lambda :{})
   for infsTestcases in ymldata["testcases"]:
       interfaceName = infsTestcases["interfaceName"]
       tdict[interfaceName] = collections.defaultdict(lambda :[])
       for case in infsTestcases["case"]:
           preConditions  = case.get("preConditions","")
           operationSteps = case["operationSteps"]
           testData       = case["testData"]
           expectedResult = case["expectedResult"]
           for data in case["testData"]:
               testPoint = data["testPoint"]
               caseid    = data["caseid"]
               tdict[interfaceName][operationSteps].append([caseid,interfaceName,testPoint,preConditions,operationSteps,data,expectedResult])
   print(tdict)
   print("fsdfyml".endswith(".yml"))



