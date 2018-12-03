#!/usr/bin/env python  
# encoding: utf-8  
from steam.admin.activity.addActivityService import ActivityAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
from steam.util.testJsonFormat import initInputService
class ActivityAddTest(SteamTestCase):
      '''
            新增活动
      '''
      __interfaceName__ = "/operation-manage/product/add"
      @initInputService(curser = ActivityAddService)
      def __init__(self, methodName = 'runTest',
                         param      =  None):
          super(ActivityAddTest,self).__init__(methodName,param)

      # def addActivity(self):
      #     addActRsp = self.myservice.addActivity()
      #     retcode   = self.myservice.getRetcodeByRsp(response = addActRsp)
      #     self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath = "\\steamcase\\activity\\operation-manageproductadds.yml",
					testclse     = ActivityAddTest
				)