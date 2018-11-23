#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewMediaresTest.py 
@time: 2018/9/14 16:30 
"""
from steam.util.testJsonFormat import initInput
from steam.util.steamLog import SteamTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.user.search.weixinSearchService import WeixinSearchService
from steam.user.weixin.userVievMediaresService import UserViewMediaresService

from steam.util.testJsonFormat import initInputService
class UserViewMediaresTest(SteamTestCase):
      '''
            用户浏览视频文章
      '''
      #__interfaceName__ = "/operation-manage/media/queryMediaByID"
      __interfaceName__ = "/steam-media/media/getMediaDetailByID"
      @initInputService(services = [ WeixinSearchService ],
                 curser   =   UserViewMediaresService )
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(UserViewMediaresTest,self).__init__(methodName,param)

      def userViewMediaresNor(self):
          articlersp = self.myservice.userViewMediares()
          rspcode    = self.myservice.getRetcodeByRsp( response = articlersp )
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\user\\userViewMediacase.xlsx",
                    testclse     = UserViewMediaresTest
                )