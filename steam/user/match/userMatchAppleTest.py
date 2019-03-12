#!/usr/bin/env python  
# encoding: utf-8  

from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.match.userMatchAppleService import UserMatchAppleService
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.util.testJsonFormat import initInputService
from steam.user.match.userCancelMatchAppleService import UserCancelMatchAppleService
from steam.user.match.userMatchAppleQueryService import UserMatchAppleQueryService
class UserMatchAppleTest(SteamTestCase):
      """
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      """
      __interfaceName__ = "/match-service/member/apply"
      @initInputService( services = [ [UserMatchQueryService,"preMatchQueryReqjsonfile"],
                                      [UserMatchAppleQueryService,"preMatchAppleQueryReqjsonfile"] ,
                                      [UserCancelMatchAppleService ,"preCancelMatchAppleReqjsonfile"]],
                         curser   =  UserMatchAppleService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserMatchAppleTest,self).__init__(methodName,param)

      # def userMatchAppleTest(self):
      #     rsp     = self.myservice.userMatchApple()
      #     retcode = self.myservice.getRetcodeByRsp(response=rsp)
      #     self.assertTrue(retcode == self.expectdata["code"] ,
      #                     msg     =  "return code is %s,and expect code is %s" %
      #                                (retcode,self.expectdata["code"]))

if  __name__ == "__main__":
    from steam.user.match.userMatchQueryTest import UserMatchQueryTest
    from steam.user.login.userLoginTest import UserLoginTest
    from steam.user.match.userMatchAppleQueryTest import UserMatchAppleQueryTest
    from steam.user.match.userCancelMatchAppleTest import UserCancelMatchAppleTest
    UserMatchQueryTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserMatchAppleQueryTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {"matchId": 22}, 7, 8])
    UserCancelMatchAppleTest( methodName="compareRetcodeTest" , param=[1, 2, 3, 4, 5, {}, 7, 8] )
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath  =  "\\steamcase\\user\\match-servicememberapplys.yml" ,
                        testclse      =   UserMatchAppleTest
                 )