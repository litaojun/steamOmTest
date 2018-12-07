#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionDelService.py 
@time: 2018/4/19 18:29 
"""
from steam.util.httpUopService import  HttpUopService
from opg.util.uopService import decorator
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import delMatchurl
from steam.admin.competition.competitionService import MatchAddService
class MatchDelService(HttpUopService):
    '''
        admin删除赛事场次
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MatchDelService, self).__init__(
                                                  module = "",
                                                  filename = "",
                                                  sqlvaluedict = kwargs,
                                                  reqjsonfile = None
                                             )
    @decorator("preInterfaceAddOneMatch")
    def addOneMatch(self):
        #self.inputKV["reqjsonfile"] = "competitionAddReq"
        matchAddSer = MatchAddService(self.inputKV)
        matchrsp    = matchAddSer.addMatch()
        matchId     = matchAddSer.getMatchIdByRsp(matchrsp)
        self.reqjsondata["matchId"] = matchId
        self.inputKV["matchId"]     = matchId

    def delMatchById(self,matchId):
        delclassfiyRsp = requests.post(
									     url     = delMatchurl,
									     json    = self.reqjsondata,
									     headers = self.jsonheart,
									     verify  = False
								       )

    @decorator(["tearDownDelMatchOrSession"])
    def delMatch(self):
        self.sendHttpReq()

    def getRetcodeByMatchRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="code")

    def getMatchIdByRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="matchId")


if __name__ == "__main__":
   pass