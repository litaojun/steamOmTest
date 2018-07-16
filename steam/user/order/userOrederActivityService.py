#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userOrederActivityService.py 
@time: 2018/7/9 17:22 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userOrderActivityUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserOrderActivityReq,weixinUserOrderActivityRspFmt
from opg.util.httptools import httpPost
#from steam.user.order.userDetailOrderService import  UserDetailOrderActivityService
class UserOrderActivityService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwarg={},modul="",filename= "",reqjsonfile = weixinUserOrderActivityReq):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserOrderActivityService, self).__init__(modul, filename, sqlvaluedict=kwarg , reqjsonfile = reqjsonfile)
        self.userThOrderActivityReqjson = self.reqjsondata

    @decorator(["tearInterfaceUserOrderActivity","preInterfaceUserOrderActivity"])
    def userOrderActivity(self):
        self.rsp =  httpPost(
                                        url     =   userOrderActivityUrl,
                                        headers =    self.jsonheart,
                                        reqJsonData =  self.userThOrderActivityReqjson
                            )
        return self.rsp

    @check_rspdata(filepath=weixinUserOrderActivityRspFmt)
    def getRetcodeByOrderRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getOrderIdFromRsp(self,response = None):
        if response is None:
            response = self.userOrderActivity()
        return query_json(json_content=json.loads(response), query="data.orderId")

    # def detailOrderActivtiy(self):
    #     orderId = self.getOrderIdFromRsp(response=self.rsp)
    #     self.sqlvaluedict["orderId"] = orderId
    #     userDetailOrdSer = UserDetailOrderActivityService(kwarg=self.sqlvaluedict)
    #     rsp = userDetailOrdSer.userDetailOrderActivity()
    #     retcode = UserDetailOrderActivityService.getRetcodeByOrderRsp(response=rsp)
    #     return retcode



if __name__ == "__main__":
    kwarg = {
              "resourceId":"1767",
              "skuId":"563",
              "addressId":"b9a6e45e-8355-11e8-9033-02a7e93155ea",
              "payPrice":"0.01",
              "num":1,
              "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
              "resourceTypeId": 12,
            }
    userOrderAct = UserOrderActivityService(kwarg=kwarg)
    rsp = userOrderAct.userOrderActivity()
    print(rsp)