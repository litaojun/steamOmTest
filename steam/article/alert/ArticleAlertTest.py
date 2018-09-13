#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleAlertTest.py 
@time: 2018/4/23 16:13 
"""
from steam.article.alert.ArticleAlertService import ArticleAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class ArticleAlertTest(SteamTestCase):
      '''
            管理后台修改文章
      '''
      __interfaceName__ = "/operation-manage/media/updateMedia"
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ArticleAlertTest,self).__init__(methodName,param)
          self.articleSer =  ArticleAlertService(self.inputdata)
          self.setService(self.articleSer)

      def testArticleAlertNor(self):
          articlersp = self.articleSer.alertArticle()
          rspcode    = self.articleSer.getRetcodeByArticleRsp(articleRsp=articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\articlealertcase.xlsx",
                    testclse = ArticleAlertTest
                )