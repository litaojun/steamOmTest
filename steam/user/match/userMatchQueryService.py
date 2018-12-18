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
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userMatchQueryUrl
from opg.util.schemajson import check_rspdata
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

    def userMatchQuery(self):
        self.rsp = httpPost(url         = userMatchQueryUrl,
                            headers     = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    # @check_rspdata(filepath = "userMatchQueryRspFmt")
    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

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

if __name__ == "__main__":
   args = {
            "matchId": 22,
            "subMatchId": 23,
            "subjectIdList": [1, 4, 6],
            "contactName": "李陶军",
            "contactPhone": "18916899938",
            "studentName": "李陶军",
            "province": "上海",
            "city": "上海市",
            "country": "黄浦区",
            "group": "幼儿园",
            "school": "文庙路幼儿园",
            "nationality": "",
            "subMatchName": "亲子擂台赛初赛",
            "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4"
        }
   umps = UserMatchQueryService(kwargs=args)
   rsp = umps.userMatchQuery()
   print(rsp)