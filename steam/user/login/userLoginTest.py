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
from steam.user.verfiycode.userVerfiyCodeService import WeixinUserVerfiyCodeService
from steam.util.testJsonFormat import initInputService
from steam.user.login.userLoginService import WeixinUserLoginService
from steam.util.steamLog import SteamTestCase
from opg.unit.parametrized import ParametrizedTestCase
class UserLoginTest(SteamTestCase):
      '''
            微信端用户通过手机号码登录
      '''
      __interfaceName__   = "/member/login/memberLogin"
      @initInputService( services = [ WeixinUserVerfiyCodeService ] ,
                         curser   =   WeixinUserLoginService )
      def __init__( self, methodName = 'runTest',
                          param      = None ):
          super(UserLoginTest,self).__init__(methodName,param)

if  __name__ == "__main__":
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\memberloginmemberLogins.yml",
                        testclse     = UserLoginTest
                 )