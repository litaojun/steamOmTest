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
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.util.testJsonFormat import initInput,initInputService
class WeixinSearchTest(SteamTestCase):
      '''
            微信端用户进入报名页面，获取到赛事，场次，赛题相关信息
      '''
      __interfaceName__ = "/steam-search/search/keywordSearch"
      @initInputService(services = [],
                        curser   = WeixinSearchService)
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(WeixinSearchTest,self).__init__(methodName,param)

      # def userSearchContentTest(self):
      #     rsp     = self.myservice.weixinUserSearchReq()
      #     retcode = self.myservice.getRetcodeByRsp(response = rsp)
      #     self.assertTrue(retcode == self.expectdata["code"])

if  __name__ == "__main__":
    # from steam.user.search.weixinSearchTest import WeixinSearchTest
    # WeixinSearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    # from steam.user.verfiycode.userVerfiyCodeTest import UserVerfiyCodeTest
    # from steam.user.login.userLoginTest import UserLoginTest
    # UserVerfiyCodeTest(methodName="compareRetcodeTest",
    #                    param=[1, 2, 3, 4, 5, {}, 7, 8])
    # UserLoginTest(methodName="compareRetcodeTest",
    #               param=[1, 2, 3, 4, 5, {}, 7, 8])
    from steam.runflask.util.initData import allTestCase, allTestClass
    from opg.unit.flaskRunMgr import  genAllTestCase
    genAllTestCase(allTestClass=allTestClass,allCase=allTestCase)
    runTestOneCls(
                        casefilepath = "\\steamcase\\user\\steam-searchsearchkeywordSearchs.yml",
                        testclse     = WeixinSearchTest
                 )