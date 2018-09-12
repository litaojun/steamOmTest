#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: upActivityTest.py 
@time: 2018/5/10 17:54 
"""
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.activity.up.upActivityService import ActivityPublishService
from steam.util.testJsonFormat import initInput
from steam.activity.search.searchActivityService import ActivitySearchService
from steam.activity.query.queryActivityService import ActivityQueryService
from steam.activity.down.downActivityService import ActivityUnPublishService
from steam.util.steamLog import SteamTestCase
class ActivityPublishTest(SteamTestCase):
      '''
            根据ID搜索活动
      '''
      __interfaceName__ = "/operation-manage/product/publish"

      @initInput(services = [ActivitySearchService,
                             ActivityQueryService ],
                 curser   =  ActivityPublishService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivityPublishTest,self).__init__(methodName,param)

      def publishActivityTest(self):
          oneActRsp = self.myservice.publishActivitySer()
          code      = self.myservice.getRetcodeByUpactRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])


if __name__ == "__main__":
          runTestOneCls(
				          casefilepath="\\steamcase\\activity\\activitypublishcase.xlsx",
				          testclse=ActivityPublishTest
			           )