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
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.article.ArticleSearchService import ArticleSearchService

from steam.admin.article.delArticleService import ArticleDelService
from steam.admin.article.ArticleAddService import ArticleAddService

class ArticleDelTest(SteamTestCase):
      '''
            admin删除文章视频
      '''
      __interfaceName__ = "/operation-manage/media/deleteMedia"
      @initAdminInputService( services = [ ArticleAddService  ,
                                      ArticleSearchService  ] ,
                         curser   =   ArticleDelService  )
      def __init__(self, methodName='runTest', param=None):
          super(ArticleDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.article.ArticleAddTest import ArticleAddTest
   from steam.admin.article.ArticleSearchTest import ArticleSearchTest
   ArticleSearchTest( methodName="compareRetcodeTest" , param= [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
   ArticleAddTest( methodName="compareRetcodeTest"    , param= [ 1, 2, 3, 4, 5, {}, 7, 8 ] )
   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\operation-managemediadeleteMedias.yml",
                    testclse     = ArticleDelTest
                )