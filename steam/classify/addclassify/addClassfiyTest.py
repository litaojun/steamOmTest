#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: addClassfiyTest.py 
@time: 2018/4/17 14:41 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class ClassfiyAddTest(SteamTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/resource-service/resource/addEntry"
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiyAddTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.classfiySer = ClassfiyAddService(self.inputdata)
          self.setService(self.classfiySer)

      def testClassfiyAddNor(self):
          clsrsp = self.classfiySer.addClassfiy()
          rspcode = self.classfiySer.getRetcodeByClassfiyRsp(classfiyRsp=clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\classifyaddcase.xlsx",
                    testclse = ClassfiyAddTest
                 )
