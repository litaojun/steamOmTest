#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: homeCnfQueryService.py 
@time: 2018/6/4 17:59 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json,del_json_data
from steam.util.configurl import homeConfigQueryurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import homeConfigQueryReq,homeConfigQueryRspFmt
from opg.util.httptools import httpGet
from opg.util.lginfo import  logger
import operator as op
from decimal import Decimal
class HomeCnfQueryService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(HomeCnfQueryService, self).__init__("weixin", "cnfDataDb.xml", kwargs , reqjsonfile = homeConfigQueryReq)
        self.rsp = None
        self.homeCnfQueryReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryHomePageCnf(self):
        homePageCnfRsp =  httpGet(
                                        url     = homeConfigQueryurl + self.homeCnfQueryReqjson,
                                        headers = self.jsonheart
                                  )
        self.rsp = homePageCnfRsp
        return homePageCnfRsp

    @check_rspdata(filepath=homeConfigQueryRspFmt)
    def getRetcodeByActivityRsp(self,response = None):
        print("homePageCnfRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

    def getAllCnfListData(self,response = None):
        """
            :param response:
            :return:
        """
        showInfos = query_json(json_content=json.loads(response), query="showInfos")
        num = len(showInfos)
        retdata = {}
        for i in range(num):
            positionQuery = "showInfos.%d.position" % i
            infosQuery = "showInfos.%d.showSummaryInfos" % i
            curposition = query_json(json_content=json.loads(response), query=positionQuery)
            curinfos = query_json(json_content=json.loads(response), query=infosQuery)
            retdata[curposition] = curinfos
        return retdata

    def dataFilterFields(self,dictData = {},fields = []):
        allFields = ["collectState","sales","visits","collects","state","holdingTime","activityAddress","subHead"]
        if fields is not None and len(fields) > 0:
            allFields = fields
        positionKeys = dictData.keys()
        for key in positionKeys:
            totalLen = len(dictData[key])
            for i in range(totalLen):
                for field in allFields:
                    queryStr = "%s.%d.%s" % (key,i,field)
                    del_json_data(dictData,queryStr)
        return dictData


    def getDbHomePageData(self):
        homePageDbDataList = self.selectAllDataBySqlName("select_t_sku_HomePage")
        dbDataDict = {}
        fields = ['resourceId','specificType','bannerUrl','thumbUrl','resourceType','title','position','minPrice','originalPrice']
        tranDictList = []
        for data in homePageDbDataList:
            print(data[7],data[8])
            if data[7] is not None:
               data[7] = float(str(data[7]))
            if data[8] is not None:
               data[8] = float(str(data[8]))
            tranDictList.append(dict(zip(fields,data)))
        for homeData in tranDictList:
            positionKey = homeData["position"]
            if positionKey in dbDataDict:
                dbDataDict[positionKey].append(homeData)
            else:
                dbDataDict[positionKey] = [homeData]
        return dbDataDict

    def compareData(self,response = None):
        pageDataDict = self.getAllCnfListData(response = response)
        pageDict = self.dataFilterFields(dictData=pageDataDict)
        dbDataDict = self.getDbHomePageData()
        page01 = pageDict["01"]
        db01 = dbDataDict["01"]
        for i,data in enumerate(page01):
            cmpRstSign = op.eq(data,db01[i])
            print(cmpRstSign)

if __name__ == "__main__":
    kwargs = {
                "phoneNo":"18916899938",
                "memberId":"0e399155-0a89-40e7-8177-e032984bf87c",
                "pageType":"0"
             }
    homeCnfSer = HomeCnfQueryService(kwargs=kwargs)
    homeRsp = homeCnfSer.queryHomePageCnf()
    retcode = homeCnfSer.getRetcodeByActivityRsp(response=homeRsp)
    retdata = homeCnfSer.getAllCnfListData(response=homeRsp)
    data01 = retdata['01']
    data02 = retdata['02']
    data05 = retdata['05']
    data07 = retdata['07']
    data10 = retdata['10']
    homeCnfSer.dataFilterFields(dictData=retdata,fields=[])
    homeCnfSer.compareData(response=homeRsp)
    print(retdata)
    print("retcode=%s" % retcode)