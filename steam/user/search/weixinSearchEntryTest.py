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
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchEntryService import UserSearchEntryService
from steam.home.cnfquery.homeCnfQueryService import HomeCnfQueryService
from steam.util.testJsonFormat import initInput
class WeixinSearchEntryTest(SteamTestCase):
      '''
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      '''
      __interfaceName__ = "/steam-resource/index/configs/searchByEntry"
      @initInput(services = [HomeCnfQueryService],
                 curser   = UserSearchEntryService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(WeixinSearchEntryTest,self).__init__(methodName,param)

      def userSearchEntryTest(self):
          rsp     = self.myservice.userSearchEntryReq()
          retcode = self.myservice.getRetcodeByRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userSearchEntrycase.xlsx",
                        testclse     = WeixinSearchEntryTest
                 )