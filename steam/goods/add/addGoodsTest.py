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
from steam.activity.add.addActivityService import ActivityAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class GoodsAddTest(SteamTestCase):
      '''
            新增商品
      '''
      __interfaceName__ = "/operation-manage/product/add-goods"
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