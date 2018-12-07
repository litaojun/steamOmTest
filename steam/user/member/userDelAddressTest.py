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
from steam.util.testJsonFormat import initInputService
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
      @initInputService(services = [UserAddAddressService,MemberAddressService],
                         curser  = UserDelAddressService)
      def __init__(self, methodName='runTest', param=None):
          super(UserDelAddressTest,self).__init__(methodName,param)

if  __name__ == "__main__":
    from steam.user.member.userAddAddressTest import UserAddAddressTest
    from steam.user.member.memberAddressTest import MemberAddressTest
    UserAddAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    MemberAddressTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath =  "\\steamcase\\user\\member-serviceaddress-dels.yml",
                        testclse     =  UserDelAddressTest
                 )