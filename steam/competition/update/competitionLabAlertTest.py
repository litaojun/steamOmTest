#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionAlertTest.py 
@time: 2018/4/20 15:06 
"""
from steam.admin.competition.competitionAlertService import CompetitionAlertService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
class CompetitionAlertTest(SteamTestCase):
      '''
            admin修改赛事场次
      '''
      __interfaceName__ = "/match-service/match/updateMatchById-del"
      def __init__(self, methodName='runTest', param=None):
          super(CompetitionAlertTest,self).__init__(methodName,param)
          self.inputdata["reqjsonfile"] = "competitionLabAlertReq"
          self.matchSer                   = CompetitionAlertService(self.inputdata)
          self.setService(self.matchSer)

      def matchLabAlertReq(self):
          matchrsp = self.matchSer.alertMatch()
          rspcode  = self.matchSer.getRetCodeAlertRsp(rsp = matchrsp)
          self.assertTrue(rspcode == self.expectdata["code"])

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath = "\\steamcase\\competition\\competitionlabalertcase.xlsx",
                    testclse = CompetitionAlertTest
                )