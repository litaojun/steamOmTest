#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userLoginService.py 
@time: 2018/6/5 14:33 
"""
from opg.unit.parametrized import ParametrizedTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.util.testJsonFormat import initInput
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
class UserLoginTest(ParametrizedTestCase):
      '''
            微信端用户通过手机号码登录
      '''
      __interfaceName__   = "/member/login/memberLogin"
      @initInput(services = [WeixinUserVerfiyCodeService],
                 curser   =  WeixinUserLoginService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserLoginTest,self).__init__(methodName,param)

      def userLoginTest(self):
          rsp     = self.myservice.weixinUserLogin()
          retcode = self.myservice.getRetcodeByUserLoginRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userLogincase.xlsx",
                        testclse     = UserLoginTest
                 )