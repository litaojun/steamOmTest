#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryMemberIdTest.py 
@time: 2018/9/17 14:39 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initInputService
from steam.user.login.QueryMemberIdService import QueryMemberIdService
class QueryMemberIdTest(SteamTestCase):
      '''
            微信端用户通过token获取memberID
      '''
      __interfaceName__ = "/member/login/queryMemberInfo"
      @initInputService( services =  [ ] ,
                         curser   =  QueryMemberIdService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(QueryMemberIdTest,self).__init__(methodName,param)

      # def getUserMidTest(self):
      #     rsp     = self.myservice.userMemberIdReq()
      #     retcode = self.myservice.getRetcodeByRsp(response=rsp)
      #     self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest( methodName = "compareRetcodeTest" ,
                        param      = [1, 2, 3, 4, 5, {}, 7, 8] )
    UserLoginTest( methodName = "compareRetcodeTest" ,
                   param      = [1, 2, 3, 4, 5, {}, 7, 8] )
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\memberloginqueryMemberInfos.yml",
                        testclse     = QueryMemberIdTest
                 )