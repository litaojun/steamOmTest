#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userOrderActivityTest.py 
@time: 2018/7/11 10:09 
"""
from steam.user.order.userOrederActivityService import UserOrderActivityService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.member.memberAddressService import MemberAddressService
from steam.util.testJsonFormat import initInput
from steam.user.weixin.userViewActivityService import UserViewActivityService
from steam.util.testJsonFormat import initInputService
class UserOrderActivityTest(SteamTestCase):
      '''
            用户订购活动
      '''
      __interfaceName__ = "/order-service/order/submitAndPay"
      @initInputService(services = [ WeixinSearchService     ,
                                     UserViewActivityService ,
                                     MemberAddressService ]  ,
                 curser = UserOrderActivityService)
      def __init__(self, methodName='runTest', param=None):
          super(UserOrderActivityTest,self).__init__(methodName,param)

      def userOrderActivity(self):
          userOrderRsp = self.myservice.userOrderActivity()
          retcode      = self.myservice.getRetcodeByOrderRsp(response = userOrderRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.weixin.userViewActivityTest import UserViewActivityTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserViewActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath =  "\\steamcase\\user\\order-serviceordersubmitAndPays.yml",
                        testclse     =  UserOrderActivityTest
                 )