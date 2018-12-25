#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.util.testJsonFormat import initInputService
class ActivitySearchTest(SteamTestCase):
      '''
            根据名称搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/queryProducts"

      @initInputService(services = [],
                 curser   = ActivitySearchService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivitySearchTest,self).__init__(methodName,param)

      def searchActivity(self):
          activityRsp = self.myservice.queryActivity()
          code        = self.myservice.getRetcodeByActRsp(queryRsp=activityRsp)
          self.assertTrue(code == self.expectdata["code"])

if __name__ == "__main__":

    runTestOneCls(
				          casefilepath = "\\steamcase\\activity\\operation-manageproductqueryProducts.yml",
				          testclse     = ActivitySearchTest
			     )