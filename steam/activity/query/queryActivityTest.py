#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryActivityTest.py 
@time: 2018/5/10 16:38 
"""
from opg.unit.parametrized import ParametrizedTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.util.steamLog import SteamTestCase
class ActivityQueryTest(SteamTestCase):
      '''
            根据ID搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/query"
      def __init__(self, methodName='runTest', param=None):
          super(ActivityQueryTest,self).__init__(methodName,param)
          self.activitySer = ActivitySearchService(self.inputdata)
          self.setService(self.activitySer)

      def queryActivityDetail(self):
          activityRsp = self.activitySer.queryActivity()
          code = self.activitySer.getRetcodeByActRsp(queryRsp=activityRsp)
          self.assertTrue(code == self.expectdata["code"])
          rssid = self.activitySer.getFirstActivityIdByRsp(queryRsp=activityRsp)
          self.inputdata["resourceId"] = rssid
          queryActSer = ActivityQueryService(kwargs=self.inputdata)
          oneActRsp = queryActSer.queryOneActivity()
          code = queryActSer.getRetcodeByOneactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])

if __name__ == "__main__":
          runTestOneCls(
				          casefilepath =  "\\steamcase\\activity\\activityquerycase.xlsx",
				          testclse     =  ActivityQueryTest
			           )