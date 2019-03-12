#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewActivityService.py 
@time: 2018/7/9 15:53 
"""
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class UserViewActivityService(HttpUopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserViewActivityService, self).__init__(module       = modul,
                                                      filename     = filename,
                                                      sqlvaluedict = kwargs ,
                                                      reqjsonfile  = reqjsonfile)


    def userViewActivity(self):
        # self.rsp =  httpGet(
        #                           url     = userViewActivityUrl + self.reqjsondata,
        #                           headers = self.jsonheart
        #                     )
        self.rsp = self.sendHttpReq()
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def getSkuDict(self,response = None):
        if response is None:
           return None
        skuList = query_json(json_content = json.loads(response),
                             query        = "data.skuList")
        return dict([(sku["skuName"],sku) for sku in skuList])

    def getSkuByName(self,response = None):
        return self.getSkuDict(response=response)["skuName"]

    def getCollectsNumByRsp(self,response = None):
        return query_json(json_content=json.loads(response),
                          query       ="data.collects")

    @decorator(["setupUserViewActivityGoodsDetail"])
    def setInPutData(self):
        try:
            if self.rsp is None:
               self.rsp = self.userViewActivity()
            skuNmIdDict = self.getSkuDict(response = self.rsp)
            if self.inputKV.get("skuName") is not None and skuNmIdDict is not None:
               self.inputKV["skuId"]    = skuNmIdDict[self.inputKV["skuName"]]["skuId"]
               self.inputKV["payPrice"] = skuNmIdDict[self.inputKV["skuName"]]["price"]
        except  Exception as e:
            print("init fail")

    def findTestDataBySkuName(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        skuDict = self.getSkuDict()
        if "skuName" not in self.inputKV or self.inputKV["skuName"] in skuDict:
            return "000000"
        return "100001"


if  __name__ == "__main__":
    pass