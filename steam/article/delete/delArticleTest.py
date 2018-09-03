#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delArticleTest.py 
@time: 2018/4/23 16:24 
"""

from steam.util.steamLog import SteamTestCase
from steam.classify.delclassify.delClassifyService import ClassfiyDelService
from steam.article.delete.delArticleService import ArticleDelService
from opg.unit.testcaseRunMgr import runTestOneCls

class ArticleDelTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/steam-media/media/deleteMedia"
      def __init__(self, methodName='runTest', param=None):
          super(ArticleDelTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.articleSer = ArticleDelService(self.inputdata)
          self.setService(self.articleSer)

      def testArticleDelNor(self):
          articlersp = self.articleSer.delClassfiy(title=self.inputdata["title"],
                                                   resourceTypeId=self.inputdata["resourceTypeId"])
          rspcode = self.articleSer.getRetcodeByArticleRsp (articlersp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\articledelcase.xlsx",
                    testclse = ArticleDelTest
                )