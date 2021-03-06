#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: weixinSearchTest.py 
@time: 2018/9/17 14:08 
"""
from steam.util.steamLog import SteamTestCase
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchEntryService import UserSearchEntryService
from steam.util.testJsonFormat import initInputService
class WeixinSearchEntryTest(SteamTestCase):
      '''
            微信端用户按分类搜索
      '''
      __interfaceName__ = "/steam-resource/index/configs/searchByEntry"
      @initInputService(services = [ ],
                 curser   = UserSearchEntryService  )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(WeixinSearchEntryTest,self).__init__(methodName,param)

      def userSearchEntryTest(self):
          rsp     = self.myservice.userSearchEntryReq()
          retcode = self.myservice.getRetcodeByRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    from steam.user.search.weixinSearchTest import WeixinSearchTest
    WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    from steam.user.login.userLoginTest import UserLoginTest
    UserVerfiyCodeTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    UserLoginTest(methodName="compareRetcodeTest",
                       param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\steam-resourceindexconfigssearchByEntrys.yml",
                        testclse     = WeixinSearchEntryTest,
                        basepath     = "D:\\litaojun\\steamyml"
                 )