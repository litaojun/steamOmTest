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
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.activity.down.downActivityService import ActivityUnPublishService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
class ActivityUnPublishTest(SteamTestCase):
      '''
            根据ID下架活动
      '''
      __interfaceName__ = "/operation-manage/product/unPublish"

      @initInput(services = [ActivitySearchService,
                             ActivityQueryService],
                 curser   = ActivityUnPublishService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivityUnPublishTest,self).__init__(methodName,param)


      def upPublishActivityTest(self):
          # activityRsp = self.myservice.queryActivity()
          # code = self.myservice.getRetcodeByActRsp(queryRsp=activityRsp)
          # self.assertTrue(code == self.expectdata["code"])
          # rssid = self.myservice.getFirstActivityIdByRsp(queryRsp=activityRsp)
          # self.inputdata["resourceId"] = rssid
          # queryActSer = ActivityUnPublishService(kwargs = self.inputdata)
          oneActRsp = self.myservice.unPublishActivitySer()
          code      = self.myservice.getRetcodeByDownactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])


if __name__ == "__main__":
          runTestOneCls(
				          casefilepath="\\steamcase\\activity\\activityunpublishcase.xlsx",
				          testclse=ActivityUnPublishTest
			           )