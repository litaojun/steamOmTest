#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: mediaresAddTest.py 
@time: 2018/4/23 17:01 
"""
from steam.util.steamLog import SteamTestCase
from steam.article.add.ArticleAddService import ArticleAddService
from opg.unit.testcaseRunMgr import runTestOneCls

class MediaresAddTest(SteamTestCase):
      '''
            新增文章
      '''
      __interfaceName__ = "/steam-media/media/addMediass"
      def __init__(self, methodName='runTest', param=None):
          super(MediaresAddTest,self).__init__(methodName,param)
          self.articleSer = ArticleAddService(self.inputdata)
          self.setService(self.articleSer)

      def testMediaresAddNor(self):
          articlersp = self.articleSer.addArticle()
          print("articlersp====" + str(articlersp))
          rspcode = self.articleSer.getRetcodeByArticleRsp(response=articlersp)
          expectCode = self.expectdata["code"]
          self.assertEqual(rspcode,expectCode)
          #self.assertTrue(rspcode == expectCode)


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\mediares\\mediaresaddcase.xlsx",
                    testclse = MediaresAddTest
                )