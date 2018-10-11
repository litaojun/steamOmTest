#!/usr/bin/env python  
# encoding: utf-8  

from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls,runTestOneTestcaseByCls
from steam.user.match.userMatchAppleService import UserMatchAppleService
from steam.util.testJsonFormat import initInput
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.user.match.appleResetTools import userAppleMatchTwo
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
          #userAppleMatchTwo()
          rsp     = self.myservice.userMatchApple()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"] ,
                          msg     =  "return code is %s,and expect code is %s" %
                                     (retcode,self.expectdata["code"]))

if  __name__ == "__main__":
    # runTestOneCls(
    #                     casefilepath  =  "\\steamcase\\user\\userMatchApplecase.xlsx",
    #                     testclse      =  UserMatchAppleTest
    #              )
    runTestOneTestcaseByCls(
                             casefilepath  =  "\\steamcase\\user\\userMatchApplecase.xlsx",
                             testclse      =  UserMatchAppleTest,
                             caseids       =  ["match_apple_6"]
                            )