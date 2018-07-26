#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userAddAddressTest.py 
@time: 2018/7/25 11:45 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.member.userAddAddressService import UserAddAddressService
from steam.util.testJsonFormat import initInput
class UserAddAddressTest(SteamTestCase):
      '''
            微信端用户新增一个地址
      '''
      __interfaceName__ = "/member-service/address-add"
      @initInput(services=[],
                 curser=UserAddAddressService)
      def __init__(self, methodName='runTest', param=None):
          super(UserAddAddressTest,self).__init__(methodName,param)

      def memberAddressTest(self):
          rsp = self.myservice.userAddAddressReq()
          retcode = self.myservice.getRetcodeByRsp(response=rsp)
          #retcode = self.myservice.getMemberAddressIdFromRsp(response=rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userAddAddresscase.xlsx",
                        testclse = UserAddAddressTest
                 )