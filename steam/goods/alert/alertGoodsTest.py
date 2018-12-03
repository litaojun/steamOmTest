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
class GoodsAlertTest(SteamTestCase):
      '''
            新增文章
      '''
      __interfaceName__ = "/steam-resource/admin/product/update-goodsaaaa"
      def __init__(self, methodName='runTest', param=None):
          super(GoodsAlertTest,self).__init__(methodName,param)
          self.activitySer = ActivityAlertService(self.inputdata)
          self.setService(self.activitySer)

      def alertActivityNor(self):
          alertActRsp = self.activitySer.alertActivity(kwargs=self.inputdata)
          retcode = self.activitySer.getRetcodeByActivityRsp(articleRsp=alertActRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath="\\steamcase\\goods\\goodsalertcase.xlsx",
					testclse=GoodsAlertTest
				)