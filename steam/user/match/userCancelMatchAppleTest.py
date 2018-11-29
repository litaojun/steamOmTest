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
from steam.user.match.userMatchQueryService import UserMatchQueryService
from steam.user.match.userMatchAppleService import UserMatchAppleService
from steam.user.match.userMatchAppleQueryService import UserMatchAppleQueryService
from steam.util.testJsonFormat import initInputService
class UserCancelMatchAppleTest(SteamTestCase):
      '''
            微信端用户取消报名
      '''
      __interfaceName__ = "/match-service/member/apply/cancel"
      @initInputService( services = [ UserMatchQueryService,
                                      [UserMatchAppleService,'preMatchAppleReqjsonfile'],
                                      UserMatchAppleQueryService ],
                         curser   =  UserCancelMatchAppleService )
      def __init__(self, methodName='runTest', param=None):
          super(UserCancelMatchAppleTest,self).__init__(methodName,param)

      # def userCancelMatchAppleTest(self):
      #     rsp     = self.myservice.userCancelMatchApple()
      #     retcode = self.myservice.getRetcodeByRsp( response = rsp )
      #     self.assertTrue(retcode == self.expectdata["code"] ,
      #                     msg     =  "retcode = %s,expectCode =%s" % (retcode ,self.expectdata["code"]))

if  __name__ == "__main__":
    from steam.user.match.userMatchQueryTest import UserMatchQueryTest
    from steam.user.match.userMatchAppleTest import UserMatchAppleTest
    from steam.user.match.userMatchAppleQueryTest import UserMatchAppleQueryTest
    UserMatchQueryTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserMatchAppleTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {"matchId": 22,"subMatchName":"sss"}, 7, 8])
    UserMatchAppleQueryTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {"matchId": 22}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\match-servicememberapplycancels.yml" ,
                        testclse     = UserCancelMatchAppleTest
                 )