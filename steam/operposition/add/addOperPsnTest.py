#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addOperPsnTest.py 
@time: 2018/4/25 18:14 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.operposition.add.addOperPsnService import OperpsnAddService

class OperpsnAddTest(ParametrizedTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/steam-featured/homeConfig/createConfig"
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnAddTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.operpsnSer = OperpsnAddService(self.inputdata)
          self.setService(self.operpsnSer)

      def testOperpsnAddNor(self):
          operpsnrsp = self.operpsnSer.addOperPosition()
          print("testclsrsp====" + str(operpsnrsp))
          rspcode = self.operpsnSer.getRetcodeByOperpsnRsp(operpsnrsp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnaddcase.xlsx",
                    testclse = OperpsnAddTest
                 )