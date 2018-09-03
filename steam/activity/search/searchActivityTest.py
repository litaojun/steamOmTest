#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: searchActivityTest.py 
@time: 2018/5/10 16:38 
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.activity.search.searchActivityService import ActivitySearchService
class ActivitySearchTest(SteamTestCase):
      '''
            根据名称搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/queryProducts"
      def __init__(self, methodName='runTest', param=None):
          super(ActivitySearchTest,self).__init__(methodName,param)
          self.activitySer = ActivitySearchService(self.inputdata)
          self.setService(self.activitySer)

      def searchActivity(self):
          activityRsp = self.activitySer.queryActivity()
          code = self.activitySer.getRetcodeByActRsp(queryRsp=activityRsp)
          self.assertTrue(code == self.expectdata["code"])

if __name__ == "__main__":
          runTestOneCls(
				          casefilepath = "\\steamcase\\activity\\activitysearchcase.xlsx",
				          testclse     = ActivitySearchTest
			           )