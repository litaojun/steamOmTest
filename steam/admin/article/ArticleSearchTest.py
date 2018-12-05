#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleSearchTest.py 
@time: 2018/12/4 16:58 
"""

from steam.util.steamLog import SteamTestCase
from steam.admin.article.ArticleSearchService import ArticleSearchService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.testJsonFormat import initInputService
class ArticleSearchTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/operation-manage/media/queryMedias"

      @initInputService(services = [],
                        curser   = ArticleSearchService)
      def __init__(self, methodName='runTest', param=None):
          super(ArticleSearchTest,self).__init__(methodName,param)

if __name__ == "__main__":

   runTestOneCls(
                    casefilepath = "\\steamcase\\article\\operation-managemediaqueryMedias.yml",
                    testclse = ArticleSearchTest
                )