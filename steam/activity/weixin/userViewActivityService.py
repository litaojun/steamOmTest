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
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userViewActivityUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserViewActivityReq,weixinUserViewActivityRspFmt
from opg.util.httptools import httpGet,httpPost
#from steam.activity.search.searchActivityService  import ActivitySearchService


class UserViewActivityService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwarg={},modul="",filename= "",reqjsonfile = "weixinUserViewActivitisReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserViewActivityService, self).__init__(modul, filename, sqlvaluedict=kwarg , reqjsonfile = reqjsonfile)
        self.userViewActivityReqjson = userViewActivityUrl + self.reqjsondata

    def userViewActivity(self):
        userViewActivityRsp =  httpGet(
                                            url     = self.userViewActivityReqjson,
                                            headers = self.jsonheart
                                       )
        self.rsp = userViewActivityRsp
        return userViewActivityRsp

    @check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getSkuDict(self,response = None):
        d = {}
        skuList = query_json(json_content=json.loads(response), query="data.skuList")
        if skuList is not None:
            lensku = len(skuList)
            for i in range(lensku):
                data = query_json(json_content=json.loads(response), query = "data.skuList.%d" % i)
                d[data["skuName"]] = data
        return d

    def getSkuByName(self,dt = None,response = None,skuName = ""):
        if response is None:
            if self.rsp is None:
                self.rsp = self.userViewActivity()
            response =  self.rsp
        if dt is None:
            dt = self.getSkuDict(response=self.rsp)
        if skuName in dt:
            return dt[skuName]
        else:
            return  None

    def getCollectsNumByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="data.collects")

if  __name__ == "__main__":
    # kwarg = {
    #             "memberId": "09c1316f-b304-46b1-96ff-c9ebbd93a617",
    #             "resourceTypeId":12,
    #             "title":"QUEENS PALACE高级定制馆C-自动化"
    #         }
    # aqs = ActivitySearchService(kwargs=kwarg)
    # queryResultRsp = aqs.queryActivity()
    # rsid = aqs.getFirstActivityIdByRsp(queryRsp=queryResultRsp)
    # kwarg["resourceId"] = rsid
    # uvms = UserViewActivityService(kwarg=kwarg)
    # rsp = uvms.userViewActivity()
    # retcode = uvms.getRetcodeByRsp(response=rsp)
    # print(retcode)
    # sku = uvms.getSkuByName(response=rsp,skuName="套餐1")
    # print(sku)
    pass