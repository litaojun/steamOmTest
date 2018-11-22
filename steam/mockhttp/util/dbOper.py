#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: dbOper.py 
@time: 2018/11/15 14:51 
"""
from steam.mockhttp.util.initFile import generateDelayTimeConfig,generateUrlToFilePath,cf
from opg.util.uopService import loadStrFromFile
from werkzeug.routing import BaseConverter
import os
from opg.unit.flaskRunMgr import getDbManger
httpData  = generateUrlToFilePath()
def insertInterfaceTable():
    dbManger = getDbManger()
    for urlsign in httpData:
        method = httpData[urlsign][0]
        url    = httpData[urlsign][2]
        module = httpData[urlsign][3]
        title  = httpData[urlsign][4]
        for httpformat in httpData[urlsign][1]:
            reqjsonpath = httpData[urlsign][1][httpformat][1].replace(os.sep,os.sep+os.sep)
            rspjsonpath =  httpData[urlsign][1][httpformat][3].replace(os.sep,os.sep+os.sep)
            sqlStr = "insert interface_mgr(aliasName,interfaceNameAddr,reqDataPath,rspDataPath, \
            projectname,reqtype,module,mark) value('%s','%s','%s','%s','%s','%s','%s','%s')" % (urlsign,url, \
                                                               reqjsonpath,rspjsonpath,'steam亲子教育',method,module,title)
            print(sqlStr)
            dbManger.insertData(sql_insert = sqlStr)

if __name__ == "__main__":
    insertInterfaceTable()



