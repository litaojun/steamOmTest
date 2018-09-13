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
from steam.user.member.memberAddressService import MemberAddressService
from steam.util.testJsonFormat import initInput
class MemberAddressTest(SteamTestCase):
      '''
            微信端用户进入地址管理，获取地址列表
      '''
      __interfaceName__ = "/member-service/address/memberId"
      @initInput(services=[],
                 curser=MemberAddressService)
      def __init__(self, methodName='runTest', param=None):
          super(MemberAddressTest,self).__init__(methodName,param)

      def memberAddressTest(self):
          rsp     = self.myservice.memberAddressReq()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\memberAddresscase.xlsx",
                        testclse = MemberAddressTest
                 )