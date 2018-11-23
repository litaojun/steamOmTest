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
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initInput
from steam.user.order.userListOrderActivityService import UserListOrderActivityService
from steam.util.testJsonFormat import initInputService
class UserListOrderActivityTest(SteamTestCase):
      '''
            用户查询订单列表
      '''
      __interfaceName__ = "/order-service/order"
      @initInputService(services=[],
                 curser=UserListOrderActivityService)
      def __init__(self, methodName='runTest', param=None):
          super(UserListOrderActivityTest,self).__init__(methodName,param)

      def userListOrderActivity(self):
          userListOrderRsp = self.myservice.userListOrderActivity()
          retcode = self.myservice.getRetcodeByListOrderRsp(response=userListOrderRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\order-serviceorders.yml",
                        testclse = UserListOrderActivityTest
                 )