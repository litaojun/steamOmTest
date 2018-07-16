#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userListOrderActivityTest.py 
@time: 2018/7/11 10:10 
"""
from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.user.member.memberAddressService import MemberAddressService
from steam.user.order.userListOrderActivityService import UserListOrderActivityService
class UserListOrderActivityTest(SteamTestCase):
      '''
            点赞
      '''
      __interfaceName__ = "/order-service/order"
      def __init__(self, methodName='runTest', param=None):
          super(UserListOrderActivityTest,self).__init__(methodName,param)
          # ActivitySearchService(kwargs=self.inputdata).setInPutData()
          # MemberAddressService(kwargs=self.inputdata).setInPutData()
          self.userListOrderSer = UserListOrderActivityService(self.inputdata)
          self.setService(self.userListOrderSer)

      def userListOrderActivity(self):
          userListOrderRsp = self.userListOrderSer.userListOrderActivity()
          retcode = self.userListOrderSer.getRetcodeByListOrderRsp(response=userListOrderRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    kwarg = {
                "memberId": "09c1316f-b304-46b1-96ff-c9ebbd93a617",
                "resourceTypeId":12,
                "title":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                "skuName":"价格（成人）",
                "skuId":1,
                "resourceId":1
             }
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userListOrderActivitycase.xlsx",
                        testclse = UserListOrderActivityTest
                 )