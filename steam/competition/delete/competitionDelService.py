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

from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import delMatchurl
from steam.competition.add.competitionService import MatchAddService
class MatchDelService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MatchDelService, self).__init__("", "", kwargs)
        self.matchReqjson = {
							        "matchName": kwargs['matchName']
						    }
        self.delMatchIdJson = {"matchId":29}
        self.jsonheart =  {
	                         "x-token":"admin"
                          }
        self.matchser = MatchAddService(self.matchReqjson)

    @decorator("preInterfaceAddOneMatch")
    def addOneMatch(self):
        matchrsp = self.matchser.addMatch()
        self.delMatchIdJson["matchId"] = self.matchser.getMatchIdByRsp(matchrsp)

    def delMatchById(self,matchId):
        self.delMatchIdJson["matchId"] = matchId
        delclassfiyRsp = requests.post(
									     url     = delMatchurl,
									     json    = self.delMatchIdJson,
									     headers = self.jsonheart,
									     verify  = False
								       )
	    

    def delMatch(self):
        delmatchRsp = requests.post(
		                                   url     = delMatchurl,
		                                   json    = self.delMatchIdJson,
		                                   headers = self.jsonheart,
		                                   verify  = False
                                      )
        print("addclassfiyrsp = %s" % delmatchRsp.text)
        return delmatchRsp.text

    def getRetcodeByMatchRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="code")

    def getMatchIdByRsp(self, matchRsp=None):
        return query_json(json_content=json.loads(matchRsp), query="matchId")


if __name__ == "__main__":
   pass