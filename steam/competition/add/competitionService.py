#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionService.py 
@time: 2018/4/17 14:35 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addMatchurl,delMatchurl

class MatchAddService(UopService):
    '''
        增加赛事
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(MatchAddService, self).__init__("", "", kwargs)
        self.rsp = None
        self.matchReqjson = {
							        "matchName": kwargs['matchName']
						    }
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    @decorator("tearInterfaceDelOneMatch")
    def delMatch(self):
        matchId = self.getMatchIdByRsp(matchRsp = self.rsp)
        addmatchRsp = requests.post(
									        url = delMatchurl,
									        json = {"matchId":matchId},
									        headers = self.jsonheart,
									        verify = False
								    )
        return addmatchRsp.text

    def addMatch(self):
        addmatchRsp = requests.post(
		                                   url=addMatchurl,
		                                   json=self.matchReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                    )
        self.rsp = addmatchRsp.text
        return addmatchRsp.text

    def getRetcodeByMatchRsp(self,matchRsp = None):
        """
		    :param matchRsp:
		    :return:
	    """
        return query_json(json_content=json.loads(matchRsp), query="code")

    def getMatchIdByRsp(self,matchRsp = None):
        """
	    :param matchRsp:
	    :return:
	    """
        return query_json(json_content=json.loads(matchRsp), query="matchId")