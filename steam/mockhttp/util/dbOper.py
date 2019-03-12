from steam.mockhttp.util.initFile import generateUrlToFilePath
import os
from opg.bak.flaskRunMgr import getDbManger
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



