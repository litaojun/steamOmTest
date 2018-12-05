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
from steam.admin.competition.competitionService import MatchAddService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class MatchLabAddTest(SteamTestCase):
      '''
            admin新增赛事场次
      '''
      __interfaceName__ = "/match-service/match/createMatch-del"
      def __init__(self, methodName = 'runTest',
                         param      = None):
          super(MatchLabAddTest,self).__init__(methodName,param)
          self.inputdata["reqjsonfile"] = "competitionLabAddReq"
          self.matchSer                   = MatchAddService(self.inputdata)
          self.setService(self.matchSer)

      def matchLabAddReq(self):
          matchrsp = self.matchSer.addMatch()
          rspcode  = self.matchSer.getRetcodeByMatchRsp(matchrsp)
          self.assertTrue(rspcode == self.expectdata["code"])


if __name__ == "__main__":
   runTestOneCls(
                    casefilepath =  "\\steamcase\\competition\\competitionaddcase.xlsx",
                    testclse     =  MatchLabAddTest
                )