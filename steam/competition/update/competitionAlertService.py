#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionAlertService.py 
@time: 2018/4/20 15:06 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import delMatchurl,alertMatchurl
from steam.competition.add.competitionService import MatchAddService
class CompetitionAlertService(UopService):
    '''
        赛事修改
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(CompetitionAlertService, self).__init__("", "", kwargs)
        self.competitionAlertReqjson = {
	                                       "matchId":26,
	                                       "matchName":kwargs["matchName"]
                                        }
        self.competitionReqjson = {
							          "matchName":kwargs["matchName"]
						           }
        self.jsonheart = {
	                         "x-token":"admin"
                         }
        self.rsp = None
        self.competitionAddSer = MatchAddService(self.competitionReqjson)

    @decorator("preInterfaceAddOneMatch")
    def addOneMatch(self):
        matchrsp = self.competitionAddSer.addMatch()
        self.rsp = matchrsp
        self.competitionAlertReqjson["matchId"] = self.competitionAddSer.getMatchIdByRsp(matchrsp)

    @decorator("tearInterfaceDelOneMatch")
    def delMatch(self):
        #entryId = self.classfiy.getEntryIdByRsp(classfiyRsp=self.rsp)
        delMatchRsp = requests.post(
										url = delMatchurl ,
										json = { "matchId":self.competitionAlertReqjson['matchId']},
										headers = self.jsonheart,
										verify = False
									)
        print("delMatchRsp = %s" % delMatchRsp.text)
        return delMatchRsp.text
    #@decorator("addClassfiyService")
    def alertMatch(self):
        alertMatchRsp = requests.post(
		                                   url=alertMatchurl,
		                                   json=self.competitionAlertReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        print("alertMatchRsp = %s" % alertMatchRsp.text)
        return alertMatchRsp.text

    def getRetCodeAlertRsp(self,rsp):
        return query_json(json_content=json.loads(rsp), query="code")

if __name__ == "__main__":
	pass  