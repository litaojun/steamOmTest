#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userListOrderActivityService.py 
@time: 2018/7/9 19:08 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userListOrderActivityUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserListOrderActivityReq,weixinUserListOrderActivityRspFmt
from opg.util.httptools import httpGet,httpPost
from opg.util.lginfo import  logger
import operator as op
from steam.util.httpUopService import  HttpUopService
class UserListOrderActivityService(HttpUopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwargs = {},
                       modul  = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserListOrderActivityService, self).__init__(modul,
                                                           filename,
                                                           sqlvaluedict = kwargs ,
                                                           reqjsonfile  = reqjsonfile)
        self.userListOrderActivityReqjson = self.reqjsondata

    def userListOrderActivity(self):
        self.rsp =  httpPost(
                                        url         =  userListOrderActivityUrl,
                                        headers     =  self.jsonheart,
                                        reqJsonData =  self.userListOrderActivityReqjson
                            )
        return self.rsp

    @check_rspdata(filepath="weixinUserListOrderActivitisRspFmt")
    def getRetcodeByListOrderRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def getOrderList(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "data.orderList")

    def getTitleOrderDictByOl(self,orderList = None):
        if orderList is None:
            orderList = self.getOrderList(response = self.rsp)
        d = {}
        for data in orderList:
            title = data["title"]
            orderId = data["orderId"]
            if title not in d:
                d[title] = []
                d[title].append(orderId)
        return  d

    def getOrderDictByOl(self,orderList = None):
        if orderList is None:
            orderList = self.getOrderList(response= self.rsp)
        d = {}
        for data in orderList:
            orderId = data["orderId"]
            d[orderId] = data
        return  d


if __name__ == "__main__":
    kwarg = {
                "orderId": "15311885444040000005112",
                "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "orderStatus": "11"   # 11 待付款，12 待发货，"" 全部
            }
    name = "【重走古丝绸之路】2018梦回西北重返经典"
    a = UserListOrderActivityService(kwarg=kwarg)
    rsp = a.userListOrderActivity()
    retcode = a.getRetcodeByListOrderRsp(response=rsp)
    print(retcode)
    todict = a.getTitleOrderDictByOl()
    print(todict)
    x = a.getOrderDictByOl()
    print(x)
    ordId = todict[name]
    print(str(ordId))
    odr = x[ordId[0]]
    print(odr)


