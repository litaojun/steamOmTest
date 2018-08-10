#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: SessionUpdateTest.py 
@time: 2018/7/30 17:20 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.session.update.SessionUpdateService import SessionUpdateService
from steam.util.testJsonFormat import initInput
import time
class SessionUpdateTest(SteamTestCase):
      '''
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      '''
      __interfaceName__ = "/match-service/member/apply"
      @initInput(services = [],
                 curser   = SessionUpdateService)
      def __init__(self, methodName='runTest', param=None):
          super(SessionUpdateTest,self).__init__(methodName,param)

      def sessionUpdateTest(self):
          time.sleep(20)
          rsp = self.myservice.sessionUpdateReq()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"],
                          msg = "return code is %s,and expect code is %s" % (retcode,self.expectdata["code"]))

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userMatchApplecase.xlsx",
                        testclse = SessionUpdateTest
                 )