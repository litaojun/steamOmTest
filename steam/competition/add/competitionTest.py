#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionTest.py 
@time: 2018/4/17 14:36 
"""
from opg.unit.parametrized import ParametrizedTestCase
from steam.competition.add.competitionService import MatchAddService
from opg.unit.testcaseRunMgr import runTestOneCls

class MatchAddTest(ParametrizedTestCase):
      '''
            admin新增分类
      '''
      __interfaceName__ = "/match-service/match/createMatch"
      def __init__(self, methodName='runTest', param=None):
          super(MatchAddTest,self).__init__(methodName,param)
          self.inputdata =  self.getInputData()
          self.expectdata = self.getExpectData()
          self.matchSer = MatchAddService(self.inputdata)
          self.setService(self.matchSer)

      def testMatchAddNor(self):
          matchrsp = self.matchSer.addMatch()
          rspcode = self.matchSer.getRetcodeByMatchRsp(matchrsp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\competition\\competitionaddcase.xlsx",
                    testclse = MatchAddTest
                 )