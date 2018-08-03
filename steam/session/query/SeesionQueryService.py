#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: SeesionQueryService.py 
@time: 2018/7/30 14:11 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.schemajson import check_rspdata
from opg.util.utils import query_json
from steam.util.configurl import sessionQueryUrl
from opg.util.httptools import httpPost,httpGet
class SessionQueryService(UopService):
    '''
        管理员查询场次
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(SessionQueryService, self).__init__(module = "",
                                                    filename= "",
                                                    sqlvaluedict = kwargs ,
                                                    reqjsonfile = "sessionQueryReq",
                                                    dbName="match")

    @decorator(["preInterfaceUserMatch"])
    def sessionQueryReq(self):
        self.rsp = httpGet(url = sessionQueryUrl + self.reqjsondata,
                           headers= self.jsonheart)
        return self.rsp

    @check_rspdata(filepath = "sessionQueryRspFmt")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getMatchIdBySessionName(self,response = None,sessionName = ""):
        if response is None:
            response = self.sessionQueryReq()
        sessionLs = query_json(json_content=json.loads(response),query = "pageContext.targets")
        curSession = [x["matchId"] for x in sessionLs if x["matchName"] == sessionName]
        if len(curSession) >= 1:
            return curSession[0]

    def setInPutData(self):
        matchName = self.inputKV.get("matchName")
        if matchName is not None:
            matchId = self.getMatchIdBySessionName(sessionName=matchName)
            self.inputKV["matchId"] = matchId


if __name__ == "__main__":
   argcs = {
                    "matchId": 22,
                    "matchName": "第11届世界奥林匹克大赛湖北场次",
                    "applyStartTime": 1532925382000,
                    "applyEndTime": 1533270987000,
                    "limitCount": 2,
                    "parentId": 22,
                    "state": 1,
                    "applyNum": 0
            }
   umas = SessionQueryService(kwargs=argcs)
   rsp = umas.sessionQueryReq()
   retcode = umas.getRetcodeByRsp(response=rsp)
   print(retcode)