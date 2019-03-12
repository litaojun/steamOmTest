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
from steam.admin.article.ArticleAddService import ArticleAddService
from opg.bak.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initAdminInputService
from steam.admin.article.delArticleService import ArticleDelService
from steam.admin.article.ArticleSearchService import ArticleSearchService
class ArticleAddTest(SteamTestCase):
      '''
            管理后台新增文章视频
      '''
      __interfaceName__ = "/operation-manage/media/addMedia"
      @initAdminInputService( services =  [ ArticleDelService ,ArticleSearchService] ,
                         curser   =   ArticleAddService  )
      def __init__(self, methodName='runTest', param=None):
          super(ArticleAddTest,self).__init__(methodName,param)

if __name__ == "__main__":
    from steam.admin.article.ArticleSearchTest import ArticleSearchTest
    from steam.admin.article.delArticleTest import ArticleDelTest
    ArticleDelTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
    ArticleSearchTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
                    casefilepath = "\\steamcase\\article\\operation-managemediaaddMedias.yml",
                    testclse     = ArticleAddTest
                 )