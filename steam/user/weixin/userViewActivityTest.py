#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewActivityTest.py 
@time: 2018/9/14 16:30 
"""
from steam.util.testJsonFormat import initInput,initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewActivityService import UserViewActivityService
class UserViewActivityTest(SteamTestCase):
      '''
            用户浏览视频文章
      '''
      __interfaceName__   = "/steam-resource/product/detail"
      @initInputService(services = [ WeixinSearchService ],
                        curser   = UserViewActivityService)
      def __init__(self, methodName = 'runTest',
                         param      = None      ):
          super(UserViewActivityTest,self).__init__(methodName,param)

      # def userViewActivityNor(self):
      #     articlersp = self.myservice.userViewActivity()
      #     rspcode    = self.myservice.getRetcodeByRsp(response = articlersp)
      #     self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   from opg.unit.flaskRunMgr import getRunTestTokenId, genAllTestCase, runAllTestCase
   from steam.runflask.util.initData import allTestCase, allTestClass, tokenList
   a = genAllTestCase(allCase= allTestCase,allTestClass=allTestClass)
   # from steam.user.search.weixinSearchTest import WeixinSearchTest
   # WeixinSearchTest(methodName="compareRetcodeTest",param = [1,2,3,4,5,{},7,8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-resourceproductdetails.yml",
                    testclse     = UserViewActivityTest
                )