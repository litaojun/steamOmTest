#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelMatchAppleTest.py 
@time: 2018/7/26 15:34 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.match.userCancelMatchAppleService import UserCancelMatchAppleService
from steam.util.testJsonFormat import initInput
class UserCancelMatchAppleTest(SteamTestCase):
      '''
            微信端用户取消报名
      '''
      __interfaceName__ = "/match-service/member/apply/cancel"
      @initInput(services=[],
                 curser=UserCancelMatchAppleService)
      def __init__(self, methodName='runTest', param=None):
          super(UserCancelMatchAppleTest,self).__init__(methodName,param)

      def userCancelMatchAppleTest(self):
          rsp = self.myservice.userCancelMatchApple()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userCancelMatchApplecase.xlsx",
                        testclse = UserCancelMatchAppleTest
                 )