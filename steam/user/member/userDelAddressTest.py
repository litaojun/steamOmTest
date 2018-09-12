#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userDelAddressTest.py 
@time: 2018/7/25 11:45 
"""

from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.member.userDelAddressService import UserDelAddressService
from steam.user.member.memberAddressService import MemberAddressService
from steam.user.member.userAddAddressService import UserAddAddressService
from steam.util.testJsonFormat import initInput
class UserDelAddressTest(SteamTestCase):
      '''
            微信端用户删除一个地址
      '''
      __interfaceName__ = "/member-service/address-del"
      @initInput(services=[],
                 curser=UserDelAddressService)
      def __init__(self, methodName='runTest', param=None):
          super(UserDelAddressTest,self).__init__(methodName,param)

      def userDelAddressTest(self):
          rsp     = self.myservice.userDelAddressReq()
          retcode = self.myservice.getRetcodeByRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userDelAddresscase.xlsx",
                        testclse = UserDelAddressTest
                 )