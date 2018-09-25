#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: AlertOperpsnTest.py 
@time: 2018/4/25 18:53 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.operposition.alert.AlertOperpsnService import OperpsnAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
class OperpsnAlertTest(SteamTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/removeIndexConfig"

      @initInput(services=[],
                 curser=OperpsnAlertService)
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnAlertTest,self).__init__(methodName,param)

      def testOperpsnAlertNor(self):
          operrsp = self.myservice.alertOperpsn()
          rspcode = self.myservice.getRetCodeOperpsnRsp(rsp=operrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnalertcase.xlsx",
                    testclse = OperpsnAlertTest
                 )
