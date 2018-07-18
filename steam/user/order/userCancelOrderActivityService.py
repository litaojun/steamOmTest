#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelOrderActivityService.py 
@time: 2018/7/9 18:23 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userCancelOrderActivityUrl
from opg.util.schemajson import check_rspdata
from opg.util.httptools import httpPost
from steam.user.order.userOrederActivityService import UserOrderActivityService
class UserCancelOrderActivityService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwarg = {},modul = "",filename = "",reqjsonfile = "weixinUserCancelOrderActivitisReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserCancelOrderActivityService, self).__init__(modul, filename, sqlvaluedict=kwarg , reqjsonfile = reqjsonfile)
        self.userCancelOrderActivityReqjson = self.reqjsondata

    # @decorator(["tearInterfaceUserCancelOrderActivity"])
    def userCancelOrderActivity(self):
        self.rsp =  httpPost(
                                        url     =   userCancelOrderActivityUrl,
                                        headers =    self.jsonheart,
                                        reqJsonData =  self.userCancelOrderActivityReqjson
                            )
        return self.rsp

    @decorator(["preInterfaceUserOrderActivtiy"])
    def userOrderActivity(self):
        uos = UserOrderActivityService(kwargs=self.sqlvaluedict)
        rsp = uos.userOrderActivity()
        self.userCancelOrderActivityReqjson["orderId"] = uos.getOrderIdFromRsp(response=rsp)

    #@check_rspdata(filepath=weixinUserCancelOrderActivityRspFmt)
    @check_rspdata(filepath="weixinUserCancelOrderActivitisRspFmt")
    def getRetcodeByOrderRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
    kwarg = {
                "orderId": "15311885444040000005112",
                "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4"
            }
    ucoas  = UserCancelOrderActivityService(kwarg=kwarg)
    rsp = ucoas.userCancelOrderActivity()
    retcode = ucoas.getRetcodeByOrderRsp(response=rsp)
    print(retcode)