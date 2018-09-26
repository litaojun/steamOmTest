#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchAppleTest.py 
@time: 2018/7/25 11:19 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.match.userMatchAppleService import UserMatchAppleService
from steam.util.testJsonFormat import initInput
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.user.match.appleResetTools import userAppleMatch,userCancelAppleMatch,userAppleMatchTwo
class UserMatchAppleTest(SteamTestCase):
      """
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      """
      __interfaceName__ = "/match-service/member/apply"
      @initInput(services=[UserMatchQueryService],
                 curser  =UserMatchAppleService)
      def __init__(self, methodName='runTest',
                         param     =None):
          super(UserMatchAppleTest,self).__init__(methodName,param)

      def userMatchAppleTest(self):
          userAppleMatchTwo()
          rsp     = self.myservice.userMatchApple()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"] ,
                          msg     =  "return code is %s,and expect code is %s" % (retcode,self.expectdata["code"]))

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath  =  "\\steamcase\\user\\userMatchApplecase-test.xlsx",
                        testclse      =  UserMatchAppleTest
                 )