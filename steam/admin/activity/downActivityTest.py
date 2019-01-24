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
from steam.admin.activity.searchActivityService import ActivitySearchService
from steam.admin.activity.queryActivityService import ActivityQueryService
from steam.admin.activity.downActivityService import ActivityUnPublishService
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initAdminInputService
class ActivityUnPublishTest(SteamTestCase):
      '''
            根据ID下架活动
      '''
      __interfaceName__ = "/operation-manage/product/unPublish"
      @initAdminInputService(services = [ ActivitySearchService,
                                     ActivityQueryService ],
                 curser   =   ActivityUnPublishService )
      def __init__(self, methodName = 'runTest', param = None ):
          super(ActivityUnPublishTest,self).__init__(methodName,param)

      def upPublishActivityTest(self):
          oneActRsp = self.myservice.unPublishActivitySer()
          code      = self.myservice.getRetcodeByRsp(oneActRsp = oneActRsp)
          self.assertTrue(code == self.expectdata["code"])


if __name__ == "__main__":
    from steam.admin.activity.searchActivityTest import ActivitySearchTest
    ActivitySearchTest(methodName="compareRetcodeTest", param=[1, 2, 3, 4, 5, {}, 7, 8])
    runTestOneCls(
				          casefilepath="\\steamcase\\activity\\operation-manageproductunPublishs.yml",
				          testclse=ActivityUnPublishTest
			           )