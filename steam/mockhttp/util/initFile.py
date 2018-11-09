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
urldata = collections.defaultdict(lambda :{})
def loadFileData():
    basePath = os.getcwd()
    filePath = os.sep.join([basePath ,"steam","mockhttp",  "jsonfile" , "testjson.yml"])
    print("filepath = %s " % filePath)
    with open(filePath, 'r') as f:
        ymldata = yaml.load(f.read())
        print("ymldata = %s " % ymldata)
        # adminUrlData = traverseFileData(ymldata,"admin",basePath)
        # weixinUrlData = traverseFileData(ymldata,"weixin",basePath)
        # for method in adminUrlData:
        #     for url in adminUrlData[method]:
        #         weixinUrlData[method][url] = adminUrlData[method][url]
        #return weixinUrlData
        # for urltype in ymldata["steam"]:
        #     data = traverseFileData(ymldata,urltype,basePath)
        #     for method in data:
        #         for url in data[method]:
        #             urldata[method][url] = data[method][url]
        # return urldata
        return ymldata

        #traverseFileData(ymlfile, "weixin", basePath)
def generateUrlToFilePath():
    ymldata  = loadFileData()
    basePath = os.getcwd()
    for urltype in ymldata["steam"]:
        data = traverseFileData(ymldata, urltype)
        for method in data:
            for url in data[method]:
                urldata[method][url] = data[method][url]
    return urldata
def traverseFileData(ymldata,dir):
    filedata = ymldata["steam"][dir]
    rtdata = collections.defaultdict(lambda :{})
    basePath = ymldata["config"]["basepath"]
    dir = [basePath,"steam",dir]
    for curdir in filedata:
        for pathurl in  filedata[curdir]:
            data = filedata[curdir][pathurl]
            method = data["method"]
            format = data["formatone"][2]
            tempdir = dir + [curdir,format]
            rtdata[method][pathurl] = os.sep.join(tempdir)
    return rtdata

def generateDelayTimeConfig():
    ymldata = loadFileData()
    return ymldata["config"]["delay"]

if __name__ == "__main__":
   print(loadFileData())
