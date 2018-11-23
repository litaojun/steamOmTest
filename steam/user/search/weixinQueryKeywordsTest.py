#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: weixinQueryKeywordsTest.py 
@time: 2018/9/17 15:45 
"""
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinQueryKeywordsService import WeixinQueryKeywordsService
from steam.util.testJsonFormat import initInput
from steam.home.cnfquery.homeCnfQueryService import HomeCnfQueryService

from steam.util.testJsonFormat import initInputService
class WeixinSearchTest(SteamTestCase):
      '''
            微信端用户查询热门关键字
      '''
      __interfaceName__   = "/steam-search/search/queryKeywords"
      @initInputService(services = [  ],
                 curser   = WeixinQueryKeywordsService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(WeixinSearchTest,self).__init__(methodName,param)

      def userQueryKeywordsTest(self):
          rsp     = self.myservice.weixinQueryKeywordsReq()
          retcode = self.myservice.getRetcodeByRsp(response = rsp)
          self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\userQueryKeywordscase.xlsx",
                        testclse     = WeixinSearchTest
                 )