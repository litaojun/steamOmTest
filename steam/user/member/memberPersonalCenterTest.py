#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: memberAddressTest.py 
@time: 2018/7/25 11:40 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.member.memberPersonalCenterService import MemberPersonalCenterService
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
class MemberPersonalCenterTest(SteamTestCase):
      '''
            微信端用户个人信息页面
      '''
      __interfaceName__ = "/member-service/members/personalCenter-del"
      @initInputService(services = [],
                        curser   = MemberPersonalCenterService)
      def __init__(self, methodName='runTest', param=None):
          super(MemberPersonalCenterTest,self).__init__(methodName,param)

      def memberPersonalCenterTest(self):
          rsp     = self.myservice.memberPersonalCenterReq()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\memberPersonalCentercase.xlsx",
                        testclse = MemberPersonalCenterTest
                 )