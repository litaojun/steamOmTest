#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userDetailOrderTest.py 
@time: 2018/7/11 10:09 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.user.member.memberAddressService import MemberAddressService
from steam.user.order.userDetailOrderService import  UserDetailOrderActivityService
from steam.util.testJsonFormat import initInput
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewActivityService import  UserViewActivityService
class UserDetailOrderActivityTest(SteamTestCase):
      '''
            点赞
      '''
      __interfaceName__ = "/order-service/order/detail"
      @initInput(services=[WeixinSearchService,
                           UserViewActivityService,
                           MemberAddressService],
                 curser=UserDetailOrderActivityService)
      def __init__(self, methodName='runTest', param=None):
          super(UserDetailOrderActivityTest,self).__init__(methodName,param)

      def userDetailOrderActivity(self):
          userDetailOrderRsp = self.myservice.userDetailOrderActivity()
          retcode = self.myservice.getRetcodeByOrderRsp(response=userDetailOrderRsp)
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
                        casefilepath = "\\steamcase\\user\\userDetailOrderActivitycase.xlsx",
                        testclse = UserDetailOrderActivityTest
                 )