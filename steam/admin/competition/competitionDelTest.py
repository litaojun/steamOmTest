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
from steam.admin.competition.competitionDelService import MatchDelService
from opg.unit.testcaseRunMgr import runTestOneCls
from steam.util.steamLog import SteamTestCase
from steam.util.testJsonFormat import initInputService
from steam.admin.competition.competitionService import MatchAddService
class MatchDelTest(SteamTestCase):
      '''
           admin删除赛事场次
      '''
      __interfaceName__ = "/operation-manage/match/deleteMatch"
      @initInputService( curser   = MatchDelService ,
                         services = [ [ MatchAddService,"addReqjsonfile" ] ])
      def __init__(self, methodName='runTest', param=None):
          super(MatchDelTest,self).__init__(methodName,param)

if __name__ == "__main__":
   from steam.admin.competition.competitionTest import MatchAddTest
   MatchAddTest(methodName = "compareRetcodeTest", param = [1, 2, 3, 4, 5, {}, 7, 8])
   runTestOneCls(
                    casefilepath = "\\steamcase\\competition\\match-servicematchdeleteMatchs.yml",
                    testclse     = MatchDelTest
                )