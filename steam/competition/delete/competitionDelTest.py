#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionDelTest.py 
@time: 2018/4/19 18:32 
"""
from steam.competition.delete.competitionDelService import MatchDelService
from opg.unit.parametrized import ParametrizedTestCase
from opg.unit.testcaseRunMgr import runTestOneCls
class MatchDelTest(ParametrizedTestCase):
      '''
            admin删除分类
      '''
      __interfaceName__ = "/match-service/match/deleteMatch"
      def __init__(self, methodName='runTest', param=None):
          super(MatchDelTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.matchDelSer = MatchDelService(self.inputdata)
          self.setService(self.matchDelSer)

      def testClassfiyDelNor(self):
          clsrsp = self.matchDelSer.delMatch()
          rspcode = self.matchDelSer.getRetcodeByMatchRsp(matchRsp=clsrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\competition\\competitiondelcase.xlsx",
                    testclse = MatchDelTest
                )