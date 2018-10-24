#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: resourceVisitTest.py 
@time: 2018/10/19 17:42 
"""
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.weixin.resourceVisitService import ResourceVisitService
class ResourceVisitTest(SteamTestCase):
      '''
            用户浏览视频文章
      '''
      __interfaceName__   = "/steam-resource/product/detail"
      @initInput(services = [  ],
                 curser   = ResourceVisitService)
      def __init__(self, methodName = 'runTest',
                         param      = None      ):
          super(ResourceVisitTest,self).__init__(methodName,param)

      def userVisitResourceNor(self):
          articlersp = self.myservice.sendInterfaceUrlReq()
          rspcode    = self.myservice.getRetcodeByRsp(response = articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\resourceVisitCase.xlsx",
                    testclse     = ResourceVisitTest
                )