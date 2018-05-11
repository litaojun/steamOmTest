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
from opg.unit.parametrized import ParametrizedTestCase
from steam.article.add.ArticleAddService import ArticleAddService
from steam.activity.alert.alertActivityService import ActivityAlertService
from opg.unit.testcaseRunMgr import runTestOneCls

class ActivityAlertTest(ParametrizedTestCase):
      '''
            新增文章
      '''
      __interfaceName__ = "/steam-resource/admin/product/update-activity"
      def __init__(self, methodName='runTest', param=None):
          super(ActivityAlertTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.activitySer = ActivityAlertService(self.inputdata)
          self.setService(self.activitySer)

      def alertActivityNor(self):
          alertActRsp = self.activitySer.alertActivity(kwargs=self.inputdata)
          retcode = self.activitySer.getRetcodeByActivityRsp(articleRsp=alertActRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath="\\steamcase\\activity\\activityalertcase.xlsx",
					testclse=ActivityAlertTest
				)