#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleAddTest.py 
@time: 2018/4/20 17:42
"""
from steam.util.steamLog import SteamTestCase
from steam.article.add.ArticleAddService import ArticleAddService
from opg.unit.testcaseRunMgr import runTestOneCls

class ArticleAddTest(SteamTestCase):
      '''
            管理后台新增文章视频
      '''
      __interfaceName__ = "/steam-media/media/addMedia-article"
      def __init__(self, methodName='runTest', param=None):
          super(ArticleAddTest,self).__init__(methodName,param)
          self.inputdata  =  self.getInputData()
          self.expectdata =  self.getExpectData()
          self.articleSer =  ArticleAddService(self.inputdata)
          self.setService(self.articleSer)

      def testArticleAddNor(self):
          articlersp = self.articleSer.addArticle()
          rspcode    = self.articleSer.getRetcodeByArticleRsp(response=articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\articleaddcase.xlsx",
                    testclse = ArticleAddTest
                )