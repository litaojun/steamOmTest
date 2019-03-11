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
from steam.util.testJsonFormat import initInputService
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userViewActivityService import UserViewActivityService
class UserViewActivityTest(SteamTestCase):
      '''
            用户浏览活动视频
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
   from opg.bak.flaskRunMgr import  genAllTestCase
   from steam.runflask.util.initData import allTestCase, allTestClass
   genAllTestCase(allCase= allTestCase,allTestClass=allTestClass)
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\steam-resourceproductdetails.yml",
                    testclse     = UserViewActivityTest
                )