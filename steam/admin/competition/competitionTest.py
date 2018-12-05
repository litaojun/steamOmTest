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
from steam.util.testJsonFormat import initInputService
from steam.admin.competition.competitionDelService import MatchDelService
class MatchAddTest(SteamTestCase):
      '''
            admin新增赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/createMatch"
      @initInputService( curser   = MatchAddService,
                         services = [ [MatchDelService,"delReqjsonfile"] ] )
      def __init__(self, methodName='runTest', param=None):
          super(MatchAddTest,self).__init__(methodName,param)

if __name__ == "__main__":
   runTestOneCls(
                    casefilepath =  "\\steamcase\\competition\\match-servicematchcreateMatchs.yml",
                    testclse     =  MatchAddTest
                )