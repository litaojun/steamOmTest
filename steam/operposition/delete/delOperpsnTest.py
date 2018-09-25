#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delOperpsnTest.py 
@time: 2018/4/25 19:20 
"""
from steam.classify.delclassify.delClassifyService import ClassfiyDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInput
class OperpsnDelTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/resource-service/resource/removeEntry"

      @initInput(services = [],
                 curser   = ClassfiyDelService)
      def __init__(self, methodName='runTest', param=None):
          super(OperpsnDelTest,self).__init__(methodName,param)
          self.classfiySer = ClassfiyDelService(self.inputdata)
          self.setService(self.classfiySer)

      def testClassfiyDelNor(self):
          clsrsp  = self.myservice.delClassfiy()
          rspcode = self.myservice.getRetcodeByClassfiyRsp(classfiyRsp = clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\operposition\\operpsnalertcase.xlsx",
                    testclse = OperpsnDelTest
                 )

