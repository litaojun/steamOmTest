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
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class MatchAddService(HttpUopService):
    '''
        admin新增赛事场次
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(MatchAddService, self).__init__(module       = ""    ,
                                              filename     = ""    ,
                                              sqlvaluedict = kwargs ,
                                              reqjsonfile  = kwargs["reqjsonfile"])

    @decorator(["tearDownDelMatchSession"])
    def delMatch(self):
        self.sendHttpReq()

    @decorator(["setupAddMatchOrSession"])
    def addMatch(self):
        self.sendHttpReq()

    def getRetcodeByMatchRsp(self,matchRsp = None):
        """
		    :param matchRsp:
		    :return:
	    """
        return query_json(json_content = json.loads(matchRsp),
                          query        = "code")

    @decorator(["setupGetMatchOrSessionId"])
    def getMatchIdByRsp(self):
        """
            :param matchRsp:
            :return:
	    """
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        return query_json(json_content = json.loads(self.rsp),
                          query        = "matchId")