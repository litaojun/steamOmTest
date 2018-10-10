#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelOrderActivityTest.py 
@time: 2018/7/11 10:09 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.user.member.memberAddressService import MemberAddressService
from steam.user.order.userCancelOrderActivityService import UserCancelOrderActivityService
from steam.util.testJsonFormat import initInput
from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.user.weixin.userViewActivityService import UserViewActivityService
from steam.user.search.weixinSearchService import WeixinSearchService
class UserCancelOrderActivityTest(SteamTestCase):
      '''
            取消点赞
      '''
      __interfaceName__ = "/order-service/order/cancel"
      @initInput(services = [WeixinSearchService,
                             UserViewActivityService,
                             MemberAddressService],
                 curser = UserCancelOrderActivityService)
      def __init__(self, methodName='runTest', param=None):
          super(UserCancelOrderActivityTest,self).__init__(methodName,param)

      def userCancelOrderActivity(self):
          userCancelOrderRsp = self.myservice.userCancelOrderActivity()
          retcode            = self.myservice.getRetcodeByOrderRsp(response=userCancelOrderRsp)
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
                        casefilepath = "\\steamcase\\user\\userCancelOrderActivitycase.xlsx",
                        testclse = UserCancelOrderActivityTest
                 )