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

class OperpsnAlertTest(ParametrizedTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/removeIndexConfig"
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnAlertTest,self).__init__(methodName,param)
          self.operpsnSer = OperpsnAlertService(self.inputdata)
          self.setService(self.operpsnSer)

      def testOperpsnAlertNor(self):
          operrsp = self.operpsnSer.alertOperpsn()
          print("operrsp====" + str(operrsp))
          rspcode = self.operpsnSer.getRetCodeOperpsnRsp(rsp=operrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnalertcase.xlsx",
                    testclse = OperpsnAlertTest
                 )
