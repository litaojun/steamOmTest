#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delClassifyTest.py 
@time: 2018/4/18 19:06 
"""
from steam.classify.delclassify.delClassifyService import ClassfiyDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class ClassfiyDelTest(SteamTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/operation-manage/entry/removeEntry"
      def __init__(self, methodName='runTest', param=None):
          super(ClassfiyDelTest,self).__init__(methodName,param)
          self.classfiySer = ClassfiyDelService(self.inputdata)
          self.setService(self.classfiySer)

      def testClassfiyDelNor(self):
          clsrsp  = self.classfiySer.delClassfiy()
          rspcode = self.classfiySer.getRetcodeByClassfiyRsp(classfiyRsp = clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\classify\\classifydeletecase.xlsx",
                    testclse     = ClassfiyDelTest
                 )