#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: competitionFindService.py 
@time: 2018/8/22 17:20 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import findMatchUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class MatchFindService(HttpUopService):
    '''
        admin查询赛事
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(MatchFindService, self).__init__(module  = "",
                                              filename = "",
                                              sqlvaluedict = kwargs)

    def findMatchReq(self):
        self.rsp = httpGet( url         = findMatchUrl,
                            headers     = self.jsonheart)
        return self.rsp

    def getRetcodeByMatchRsp(self,matchRsp = None):
        """
		    :param matchRsp:
		    :return:
	    """
        return query_json(json_content = json.loads(matchRsp), query = "code")

    def getMatchFromRspByName(self,matchRsp = None,matchName = ""):
        """
            :param matchRsp:
            :param matchName:
            :return:
        """
        if matchRsp is None:
            matchRsp = self.findMatchReq()
        matchList = query_json(json_content = json.loads(matchRsp),
                               query        = "pageContext.targets")
        curMatch = [ match  for match in matchList if match["matchName"] == matchName ]
        return curMatch[0] if len(curMatch) > 0 else None


if __name__ == "__main__":
        kwgs = {
            "matchId": 22,
            "matchName": "亲子擂台赛",
            "state": 2,
            "applyStartTime": 1534923240000,
            "applyEndTime": 1535528043000,
            "applyNum": 0,
            "limitCount": 3,
            "token": "2a11f655db724789a1e8e42399e60eab"
        }
        matchSer = MatchFindService(kwargs=kwgs)
        match = matchSer.getMatchFromRspByName(matchName="亲子擂台赛")
        print(match)