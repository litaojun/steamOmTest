#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchQueryService.py 
@time: 2018/7/23 14:06 
"""
from opg.bak.uopService import decorator
import json
from opg.util.utils import query_json
#from steam.util.configurl import userMatchQueryUrl
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class UserMatchQueryService(HttpUopService):
    '''
        微信端用户报名
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserMatchQueryService, self).__init__(module   = "",
                                                    filename = "",
                                                    sqlvaluedict = kwargs ,
                                                    reqjsonfile  = None)

    def getMatchTitleIds(self,response = None):
        if response is None:
           #response = self.userMatchQuery()
           response = self.sendHttpReq()
        matchTitleLs = query_json(json_content = json.loads(response),
                                  query        = "subMatchList.0.subjectList")
        return [x["id"] for x in matchTitleLs]

    def getNameMatchIdDict(self,response = None):
        if response is None:
           #response = self.userMatchQuery()
           response = self.sendHttpReq()
        titleLs = query_json(json_content = json.loads(response),
                             query        = "subMatchList")
        return dict([(x["matchName"],x) for x in titleLs])

    @decorator(["setupGetSubMatchId"])
    def setInPutData(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        if "subMatchName" in self.inputKV:
            allMatchDict = self.getNameMatchIdDict(response=self.rsp)
            matchDict    = allMatchDict[self.inputKV["subMatchName"]]
            self.inputKV["subMatchId"] = matchDict["matchId"]
