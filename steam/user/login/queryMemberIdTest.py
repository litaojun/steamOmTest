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
from steam.util.testJsonFormat import initInput
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.user.login.QueryMemberIdService import QueryMemberIdService
class UserLoginTest(SteamTestCase):
      '''
            微信端用户通过token获取memberID
      '''
      __interfaceName__ = "/member/login/queryMemberInfo"
      @initInput(services = [WeixinUserVerfiyCodeService ,
                             WeixinUserLoginService ],
                 curser   =  QueryMemberIdService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserLoginTest,self).__init__(methodName,param)

      def getUserMidTest(self):
          rsp     = self.myservice.userMemberIdReq()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userQueryMemberIdcase.xlsx",
                        testclse     = UserLoginTest
                 )