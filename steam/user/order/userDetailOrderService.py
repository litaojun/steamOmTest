#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userDetailOrderService.py 
@time: 2018/7/9 19:09 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userDetailOrderActivityUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserDetailOrderActivityReq,weixinUserDetailOrderActivityRspFmt
from opg.util.httptools import httpGet,httpPost
from steam.util.testJsonFormat import initInput
from steam.util.httpUopService import  HttpUopService
from steam.user.order.userOrederActivityService import UserOrderActivityService
class UserDetailOrderActivityService(HttpUopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwargs = {},
                       modul  = "",
                       filename    = ""):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserDetailOrderActivityService, self).__init__(modul,
                                                             filename,
                                                             sqlvaluedict=kwargs )
        self.userDetailOrderActivityReqjson = self.reqjsondata

    def userDetailOrderActivity(self):
        self.rsp =  httpPost(
                                        url     =   userDetailOrderActivityUrl,
                                        headers =    self.jsonheart,
                                        reqJsonData =  self.userDetailOrderActivityReqjson
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserDetailOrderActivityRspFmt)
    def getRetcodeByOrderRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    @decorator(["setupGetTicketNo"],userType="weixin")
    def getTicketNo(self):
        """获取订单的核销卷码"""
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        self.inputKV["ticketCode"] = query_json(json_content=json.loads(self.rsp),
                                                  query="data.ticketNo")

    @decorator(["preInterfaceUserOrderActivtiy"])
    def userOrderActivity(self):
        uos = UserOrderActivityService(kwargs=self.inputKV)
        rsp = uos.userOrderActivity()
        self.userDetailOrderActivityReqjson["orderId"] = uos.getOrderIdFromRsp(response=rsp)

if __name__ == "__main__":
    kwarg = {
                "orderId": "15311885444040000005112",
                "memberId": "e99abfeb-1ae5-41d8-a422-63bc108026d4"
            }
    a = UserDetailOrderActivityService(kwargs=kwarg)
    rsp = a.userDetailOrderActivity()
    retcode = a.getRetcodeByOrderRsp(response=rsp)
    print(retcode)