#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchAppleQueryTest.py 
@time: 2018/7/26 12:47 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.match.userMatchAppleQueryService import UserMatchAppleQueryService
from steam.util.testJsonFormat import initInput
class UserMatchAppleQueryTest(SteamTestCase):
      '''
            微信用户查询已报名信息
      '''
      __interfaceName__   = "/match-service/member/mp/query"
      @initInput(services = [],
                 curser   = UserMatchAppleQueryService)
      def __init__(self, methodName='runTest', param=None):
          super(UserMatchAppleQueryTest,self).__init__(methodName,param)

      def userMatchAppleQueryTest(self):
          rsp     = self.myservice.userMatchAppleQuery()
          retcode = self.myservice.getRetcodeByRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userMatchAppleQuerycase.xlsx",
                        testclse = UserMatchAppleQueryTest
                 )