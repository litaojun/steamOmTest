#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryActivityService.py 
@time: 2018/5/7 14:06 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import queryIdActivityurl
from steam.util.reqFormatPath import fxt,activityQueryReq
from opg.util.httptools import httpGet
class ActivityQueryService(UopService):
    '''
        查询活动文章
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(ActivityQueryService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(activityQueryReq))

    def initReqJsonIdData(self,kwargs):
        skuIdLs = self.getSkuIdFmtListByFormat(size = kwargs['skulist'])
        imgIdLs = self.getImageListByFormat(size = kwargs["imglist"])
        shareIdLs = self.getShareListByFormat(size=1)
        reqjsondata = eval(self.reqjsondata)
        for i,sku in enumerate(skuIdLs):
            pass

    def queryOneActivity(self):
        self.rsp = httpGet(url=queryIdActivityurl +  self.reqjsondata,
                              headers=self.jsonheart)
        return self.rsp

    def getListIdByFormat(self,formatstr = "" ,size = 2):
        idls = [formatstr % i for i in range(size)]
        return idls

    def getSkuIdFmtListByFormat(self,size=2):
        skuIdLs = self.getListIdByFormat("data.skuList.%d.skuId",size)
        return skuIdLs

    def getSkuNameFmtListByFormat(self,size=2):
        skuNamels = self.getListIdByFormat("data.skuList.%d.skuName",size)
        return skuNamels

    def getSkuNameIdDict(self,rsp = None):
        skuList = query_json(json_content=json.loads(rsp), query="data.skuList")
        return dict([(sku["skuName"],sku) for sku in skuList])

    def getSkuIdBySkuName(self,rsp = None,skuName = ""):
        skuNameIdDict = self.getSkuNameIdDict(rsp = rsp)
        return skuNameIdDict[skuName]
        # skuIdFmtList = self.getSkuIdFmtListByFormat(size=len(skuList))
        # skuNameFmtList = self.getSkuNameFmtListByFormat(size=len(skuList))
        # skuIdList = [query_json(json_content=json.loads(rsp), query=x) for x in skuIdFmtList]
        # skuNameList = [query_json(json_content=json.loads(rsp), query=x) for x in skuNameFmtList]


    def getImageListByFormat(self,size=2):
        idls = self.getListIdByFormat("data.imageList.%d.id",size)
        return idls

    def getShareListByFormat(self,size =1):
        idls =  self.getListIdByFormat("data.shareInfoList.%d.id",size)
        return idls

    def getIdValueListByRsp(self,ids=[],rsp = None):
        idvls = []
        for idtag in ids:
            idvlaue = query_json(json_content=json.loads(rsp), query=idtag)
            idvls.append(idvlaue)
        return idvls

    def getRetcodeByOneactRsp(self,oneActRsp = None):
        return query_json(json_content=json.loads(oneActRsp), query="code")

    def setInPutData(self):
        if self.rsp is None:
            self.rsp = self.queryOneActivity()
        skuNmIdDict = self.getSkuNameIdDict(rsp = self.rsp)
        if self.inputKV.get("skuName") is not None :
            self.inputKV["skuId"] = skuNmIdDict[self.inputKV["skuName"]]["skuId"]
            self.inputKV["payPrice"] = skuNmIdDict[self.inputKV["skuName"]]["price"]

if __name__ == "__main__":

    queryJsonData = {
                       "resourceId":1469,
                       "skulist":2,
                       "imglist":1,
                       "sharelist":1,
                       "resourceTypeId":11,
                       "title":"QUEENS PALACE高级定制馆C-自动化"
                    }
    aqs = ActivityQueryService(kwargs=queryJsonData)
    aqs.getSkuListByFormat(size=2)
    queryResultRsp = aqs.queryOneActivity()
    idlsformat = aqs.getImageListByFormat(size = queryJsonData["imglist"])
    ids = aqs.getIdValueListByRsp(ids=idlsformat,rsp=queryResultRsp)
    idlsformat = aqs.getShareListByFormat(size=1)
    ids = aqs.getIdValueListByRsp(ids=idlsformat,rsp=queryResultRsp)
    idlsformat = aqs.getSkuNameIdDict(rsp=queryResultRsp)
    ids = aqs.getIdValueListByRsp(ids=idlsformat, rsp=queryResultRsp)
    print("rsid = %s" % ids)