#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: alertActivityTest.py 
@time: 2018/5/9 17:44 
"""
from steam.admin.activity.alertActivityService import ActivityAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
class ActivityAlertTest(SteamTestCase):
      '''
            新增活动
      '''
      __interfaceName__ = "/operation-manage/product/update"
      @initInputService(services = [],
                        curser   = ActivityAlertService)
      def __init__(self, methodName='runTest', param=None):
          super(ActivityAlertTest,self).__init__(methodName,param)

      def alertActivityNor(self):
          alertActRsp = self.myservice.alertActivity()
          retcode     = self.myservice.getRetcodeByRsp(articleRsp = alertActRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath="\\steamcase\\activity\\activityalertcase.xlsx",
					testclse=ActivityAlertTest
				)