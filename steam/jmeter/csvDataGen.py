#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: li.taojun
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006
@software: PyCharm
@file: alertActivityService.py
@time: 2018/5/7 13:57
"""
from opg.util.dbtools import DbManager
def writeDataToFile(filepath = "" ,datalist = []):
    wfile = open(filepath, 'w')
    wfile.writelines("\n".join(datalist))
    wfile.close()

def genDataListFromDbByFormatOrSql(format = "",sqlStr = "",dbinfo = {}):
    """
    :param format: 
    :param sqlStr: 
    :return: 
    """
    retDataList = []
    dataList = genDataListFromSql(sqlstr = sqlStr,dbinfo = dbinfo)
    for data in dataList :
        retDataList.append(format % data)
    return retDataList

def genDataListFromSql(sqlstr = "",dbinfo = None):
    """
    :param sqlstr:
    :param dbinfo:
    :return:
    """
    DbManager.cleanDB()
    dbManager   =   DbManager(host = dbinfo["host"],
                              user =  dbinfo["user"],
                              password =  dbinfo["password"],
                              dbname =  dbinfo["dbname"],
                              port =  dbinfo["port"])
    dataList = dbManager.queryAll(sql = sqlstr)
    return dataList

def genGoodsProductDataList():
    sqlStr = """select r.id resourceId,ss.id skuId,ss.`name` skuName,(ss.price+ss.post_price) payPrice  
from t_resource r LEFT JOIN t_sku ss on ss.resource_id = r.id 
where (r.state = 0 and r.resource_type_id = 11 and EXISTS(select 1 from t_sku s where s.resource_id = r.id and s.inventory>0) ) or 
       (r.state = 0 and r.resource_type_id = 12 and EXISTS(select 1 from t_sku s where s.resource_id = r.id and s.inventory>0)  
                   and EXISTS(select 1 from t_time_slot ts where r.time_slot_id = ts.id and ts.end_time>now())); 
             """
    dbInfo = {
               "host":"steam-uat-resource.cmcutmukkzyn.rds.cn-north-1.amazonaws.com.cn",
               "user":"root",
               "password":"Bestv001!",
               "dbname": "resource",
               "port": 3306
             }
    formatStr = "%s,%s,%s,%s"
    filepath = "D:\BaiduYunDownload\goodsProduct.csv"
    datalist = genDataListFromDbByFormatOrSql(format = formatStr ,sqlStr = sqlStr,dbinfo=dbInfo)
    writeDataToFile(filepath = filepath,datalist = datalist)

def genMediaDataList():
    sqlStr = """select r.id resourceId from t_resource r where r.state = 0 and r.resource_type_id in(1,2);"""
    dbInfo = {
               "host":"steam-uat-resource.cmcutmukkzyn.rds.cn-north-1.amazonaws.com.cn",
               "user":"root",
               "password":"Bestv001!",
               "dbname": "resource",
               "port": 3306
             }
    formatStr = "%s"
    filepath = "D:\BaiduYunDownload\mediaDataList.csv"
    datalist = genDataListFromDbByFormatOrSql(format = formatStr ,sqlStr = sqlStr,dbinfo=dbInfo)
    writeDataToFile(filepath = filepath,datalist = datalist)

def genEntryIdDataList():
    sqlStr = """select e.id,e.`order` from t_entry e order by e.`order` limit 0 ,6;"""
    dbInfo = {
               "host":"steam-uat-resource.cmcutmukkzyn.rds.cn-north-1.amazonaws.com.cn",
               "user":"root",
               "password":"Bestv001!",
               "dbname": "resource",
               "port": 3306
             }
    formatStr = "%s,%s"
    filepath = "D:\BaiduYunDownload\entryIdData.csv"
    datalist = genDataListFromDbByFormatOrSql(format = formatStr ,sqlStr = sqlStr,dbinfo=dbInfo)
    writeDataToFile(filepath = filepath,datalist = datalist)

def genMemberIdDataList():
    sqlStr = """select m.ID from t_member m where  EXISTS(select 1 from t_member_address a where a.member_id = m.id );"""
    dbInfo = {
               "host":"steam-uat-allin.cmcutmukkzyn.rds.cn-north-1.amazonaws.com.cn",
               "user":"root",
               "password":"Bestv001!",
               "dbname": "allin",
               "port": 3306
             }
    formatStr = "%s"
    filepath = "D:\BaiduYunDownload\memberIdData.csv"
    datalist = genDataListFromDbByFormatOrSql(format = formatStr ,sqlStr = sqlStr,dbinfo=dbInfo)
    writeDataToFile(filepath = filepath,datalist = datalist)
if __name__ == "__main__":
    genGoodsProductDataList()
    genMediaDataList()
    genEntryIdDataList()
    genMemberIdDataList()


