#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: searchActivityService.py 
@time: 2018/5/7 17:33 
"""
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import searchActivityurl
from steam.util.reqFormatPath import fxt,activitySearchReq
from steam.activity.weixin.userViewActivityService import  UserViewActivityService

class ActivitySearchService(UopService):
    '''
        查询分类
    '''
    def __init__(self,kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ActivitySearchService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(activitySearchReq))
        # self.rsp = None
        self.activityQueryReqjson = self.reqjsondata
        # self.jsonheart = {
	     #                     "x-token":"admin"
        #                  }

    def queryActivity(self):
        queryResult = requests.post(url = searchActivityurl,
                                    json=self.activityQueryReqjson,
                                    headers=self.jsonheart,
                                    verify=False
                                    )
        return queryResult.text

    def getFirstActivityIdByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.0.resourceId")

    def getSku(self,skuName):
        if self.rsp is None:
            self.rsp  = self.queryActivity()
        actId = self.getFirstActivityIdByRsp(queryRsp=self.rsp)
        self.inputKV["resourceId"] = actId
        userViewActSer = UserViewActivityService(kwarg=self.inputKV )
        sku = userViewActSer.getSkuByName(skuName=skuName)
        return sku

    def getSkuIdBySkuName(self,skuName =""):
        return self.gesku()["skuName"]

    def getSkuPayPriceBySkuName(self,skuName=""):
        return self.gesku()["skuName"]
    def setInPutData(self):
        sku = self.getSku(skuName=self.inputKV["skuName"])
        resourceId = self.getFirstActivityIdByRsp(queryRsp=self.rsp)
        self.inputKV["skuId"] = sku["skuId"]
        self.inputKV["resourceId"] = resourceId
        self.inputKV["payPrice"] = sku["price"]


    def getRetcodeByActRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="code")

if __name__ == "__main__":
    queryJsonData = {
                         "currentPage":1,
                         "pageSize":10,
                         "resourceTypeId":12,
                         "title":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                         "skuName":"价格（成人）"
                     }
    aqs = ActivitySearchService(kwargs=queryJsonData)
    queryResultRsp = aqs.queryActivity()
    rsid = aqs.getFirstActivityIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)
    skuid = aqs.getSkuIdBySkuName(skuName=queryJsonData["skuName"])
    print("skuid = %s" % skuid)