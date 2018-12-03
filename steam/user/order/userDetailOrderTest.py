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
from steam.user.member.memberAddressService import MemberAddressService
from steam.user.order.userDetailOrderService import  UserDetailOrderActivityService
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewActivityService import  UserViewActivityService
from steam.util.testJsonFormat import initInputService
from steam.user.order.userOrederActivityService import UserOrderActivityService
class UserDetailOrderActivityTest(SteamTestCase):
      '''
            点赞
      '''
      __interfaceName__ = "/order-service/order/detail"
      @initInputService( services = [ WeixinSearchService      ,
                                     UserViewActivityService  ,
                                     UserOrderActivityService ,
                                     MemberAddressService   ] ,
                           curser = UserDetailOrderActivityService )
      def __init__(self, methodName='runTest', param=None):
          super(UserDetailOrderActivityTest,self).__init__(methodName,param)

      # def userDetailOrderActivity(self):
      #     userDetailOrderRsp = self.myservice.userDetailOrderActivity()
      #     retcode            = self.myservice.getRetcodeByOrderRsp(response=userDetailOrderRsp)
      #     self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    from steam.user.weixin.userViewActivityTest import UserViewActivityTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    from steam.user.order.userOrderActivityTest import UserOrderActivityTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserViewActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserOrderActivityTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\order-serviceorderdetails.yml",
                        testclse = UserDetailOrderActivityTest
                 )