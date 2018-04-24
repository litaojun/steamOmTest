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
from opg.unit.parametrized import ParametrizedTestCase
from steam.article.alert.ArticleAlertService import ArticleAlertService
from opg.unit.testcaseRunMgr import runTestOneCls

class ArticleAlertTest(ParametrizedTestCase):
      '''
            新增文章
      '''
      __interfaceName__ = "/steam-media/media/updateMedia-article"
      def __init__(self, methodName='runTest', param=None):
          super(ArticleAlertTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.articleSer = ArticleAlertService(self.inputdata)
          self.setService(self.articleSer)

      def testArticleAlertNor(self):
          articlersp = self.articleSer.alertArticle()
          print("articlersp====" + str(articlersp))
          rspcode = self.articleSer.getRetcodeByArticleRsp(articleRsp=articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\articlealertcase.xlsx",
                    testclse = ArticleAlertTest
                )