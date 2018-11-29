#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userVerfiyCodeTest.py 
@time: 2018/9/17 15:49 
"""

from opg.unit.parametrized import ParametrizedTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.util.steamLog import SteamTestCase
class UserVerfiyCodeTest(SteamTestCase):
      '''
            微信端用户通过手机号码登录
      '''
      __interfaceName__ = "/passport/verifyCode"
      @initInputService(services = [],
                        curser   = WeixinUserVerfiyCodeService)
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserVerfiyCodeTest,self).__init__(methodName,param)

      # def userSendVerfiyCodeTest(self):
      #     rsp     = self.myservice.sendUserVerifyCode()
      #     retcode = self.myservice.getRetcodeByRsp(response = rsp)
      #     self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userVerfiyCodecase.xlsx",
                        testclse     = UserVerfiyCodeTest
                 )