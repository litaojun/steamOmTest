#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: alertClassTest.py 
@time: 2018/4/18 19:06 
"""

from opg.unit.parametrized import ParametrizedTestCase
from steam.classify.alertclass.alertClassService import ClassfiyAlertService
from opg.unit.testcaseRunMgr import runTestOneCls

class ClassfiyAlertTest(ParametrizedTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/resource-service/resource/modifyEntry"
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiyAlertTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.classfiySer = ClassfiyAlertService(self.inputdata)
          self.setService(self.classfiySer)

      def testClassfiyAlertNor(self):
          clsrsp = self.classfiySer.alertClassfiy()
          print("testclsrsp====" + str(clsrsp))
          rspcode = self.classfiySer.getRetCodeAlertRsp(rsp=clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\addclassify\\classifyalertcase.xlsx",
                    testclse = ClassfiyAlertTest
                 )
