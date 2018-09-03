#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: downActivityTest.py 
@time: 2018/5/10 17:48 
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.activity.down.downActivityService import ActivityUnPublishService
from steam.util.steamLog import SteamTestCase
class ActivityUnPublishTest(SteamTestCase):
      '''
            根据ID下架活动
      '''
      __interfaceName__ = "/operation-manage/product/unPublish"
      def __init__(self, methodName='runTest', param=None):
          super(ActivityUnPublishTest,self).__init__(methodName,param)
          self.activitySer = ActivitySearchService(self.inputdata)
          self.setService(self.activitySer)

      def upPublishActivityTest(self):
          activityRsp = self.activitySer.queryActivity()
          code = self.activitySer.getRetcodeByActRsp(queryRsp=activityRsp)
          self.assertTrue(code == self.expectdata["code"])
          rssid = self.activitySer.getFirstActivityIdByRsp(queryRsp=activityRsp)
          self.inputdata["resourceId"] = rssid
          queryActSer = ActivityUnPublishService(kwargs = self.inputdata)
          oneActRsp = queryActSer.unPublishActivitySer()
          code = queryActSer.getRetcodeByDownactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])


if __name__ == "__main__":
          runTestOneCls(
				          casefilepath="\\steamcase\\activity\\activityunpublishcase.xlsx",
				          testclse=ActivityUnPublishTest
			           )