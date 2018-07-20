#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: li.taojun
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006
@software: PyCharm
@file: addActivityTest.py
@time: 2018/5/9 15:43
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.article.add.ArticleAddService import ArticleAddService
from steam.activity.add.addActivityService import ActivityAddService
from opg.unit.testcaseRunMgr import runTestOneCls

class GoodsAddTest(ParametrizedTestCase):
      '''
            新增文章
      '''
      __interfaceName__ = "/steam-resource/admin/product/add-goods"
      def __init__(self, methodName='runTest', param=None):
          super(GoodsAddTest,self).__init__(methodName,param)
          self.activitySer = ActivityAddService(self.inputdata)
          self.setService(self.activitySer)

      def addGoods(self):
          addActRsp = self.activitySer.addActivity()
          retcode = self.activitySer.getRetcodeByActivityRsp(response=addActRsp)
          self.assertTrue(retcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
					casefilepath="\\steamcase\\goods\\goodsaddcase.xlsx",
					testclse=GoodsAddTest
				)