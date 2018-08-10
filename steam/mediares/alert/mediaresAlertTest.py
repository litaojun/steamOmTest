#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: mediaresAlertTest.py 
@time: 2018/4/23 17:01 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.article.alert.ArticleAlertService import ArticleAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import  SteamTestCase
class MediaresAlertTest(SteamTestCase):
      '''
            修改作品
      '''
      __interfaceName__ = "/steam-media/media/updateMedia"
      def __init__(self, methodName='runTest', param=None):
          super(MediaresAlertTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.articleSer = ArticleAlertService(self.inputdata)
          self.setService(self.articleSer)

      def testMediaresAlertNor(self):
          articlersp = self.articleSer.alertArticle()
          print("articlersp====" + str(articlersp))
          rspcode = self.articleSer.getRetcodeByArticleRsp(articleRsp=articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\mediares\\mediaresalertcase.xlsx",
                    testclse = MediaresAlertTest
                )