#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: weixinSearchService.py 
@time: 2018/8/13 17:11 
"""
import json
from opg.util.utils import query_json
from steam.util.configurl import weixinSearchUrl
from steam.user.weixin.userViewActivityService import  UserViewActivityService
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
from opg.bak.uopService import decorator
class WeixinSearchService(HttpUopService):
    '''
        微信端-搜索
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(WeixinSearchService, self).__init__( module       = "",
                                                   filename     = "",
                                                   sqlvaluedict = kwargs,
                                                   reqjsonfile  = None)

    def weixinUserSearchReq(self):
        self.rsp = httpGet(
                                  url     =  weixinSearchUrl + self.reqjsondata ,
                                  headers =  self.jsonheart
                           )
        return self.rsp

    def getFirstActivityIdByRsp(self,queryRsp = None):
        if queryRsp is None:
           # queryRsp = self.weixinUserSearchReq()
           queryRsp = self.sendHttpReq()
        return query_json(json_content = json.loads(queryRsp),
                          query        = "data.targets.0.resourceId")

    def getSku(self,skuName):
        if self.rsp is None:
           self.rsp  = self.weixinUserSearchReq()
        actId = self.getFirstActivityIdByRsp(queryRsp = self.rsp)
        self.inputKV["resourceId"] = actId
        userViewActSer = UserViewActivityService(kwargs = self.inputKV)
        sku            = userViewActSer.getSkuByName(skuName  = skuName,
                                                     response = self.rsp)
        return sku

    def getSkuIdBySkuName(self,skuName =""):
        return self.getSku(skuName=skuName)["skuName"]

    def getSkuPayPriceBySkuName(self,skuName=""):
        return self.getSku(skuName=skuName)["skuName"]

    @decorator(["setupgetFirstResourceId"])
    def setInPutData(self):
        resourceId = self.getFirstActivityIdByRsp(queryRsp=self.rsp)
        self.inputKV["resourceId"] = resourceId
        self.inputKV["courseId"]   = resourceId

    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
    queryJsonData = {
                         "currentPage":1,
                         "pageSize":10,
                         "resourceTypeId":12,
                         #"keyword":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                         "keyword": "早鸟价",
                         "skuName":"价格（成人）",
                         "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                         "token":"e1974c2a63ab445dba7e0392b90a81bb"
                     }
    aqs = WeixinSearchService(kwargs=queryJsonData)
    queryResultRsp = aqs.weixinUserSearchReq()
    rsid = aqs.getFirstActivityIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)
    queryJsonData["resourceId"] = rsid
    userViewActSer = UserViewActivityService(kwarg=queryJsonData)
    rsp = userViewActSer.userViewActivity()
    skuDict = userViewActSer.getSkuDict(response=rsp)
    skuvalue = skuDict[queryJsonData["skuName"]]
    print(skuvalue)
    # skuid = aqs.getSkuIdBySkuName(skuName=queryJsonData["skuName"])
    # print("skuid = %s" % skuid)