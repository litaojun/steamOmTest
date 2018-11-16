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
    for method in httpData:
        for httppath in httpData[method]:
            reqjsonpath = httpData[method][httppath][0].replace(os.sep,os.sep+os.sep)
            rspjsonpath = httpData[method][httppath][2].replace(os.sep,os.sep+os.sep)
            sqlStr = "insert interface_mgr(aliasName,interfaceNameAddr,reqDataPath,rspDataPath, \
            projectname,reqtype) value('%s','%s','%s','%s','%s','%s')" % (httppath,"https://uat-steam-api.opg.cn"+httppath \
                                                               ,reqjsonpath,rspjsonpath,'OMSTEAM亲子教育',method)
            print(sqlStr)
            dbManger.insertData(sql_insert = sqlStr)

if __name__ == "__main__":
    insertInterfaceTable()



