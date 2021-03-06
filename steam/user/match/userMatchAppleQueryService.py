#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchAppleQueryService.py 
@time: 2018/7/26 12:46 
"""
from opg.bak.uopService import decorator,resultData
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class UserMatchAppleQueryService(HttpUopService):
    '''
        微信端用户查询已报名信息
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserMatchAppleQueryService, self).__init__(module   = "",
                                                         filename = "",
                                                         sqlvaluedict = kwargs ,
                                                         reqjsonfile  = None)

    def userMatchAppleQuery(self):
        # self.rsp = httpPost(url         = userMatchAppleQueryUrl,
        #                     headers     = self.jsonheart,
        #                     reqJsonData = self.reqjsondata)
        self.rsp = self.sendHttpReq()
        return self.rsp

    def getMatchNameDict(self,response = None):
        if response is None:
           response = self.sendHttpReq()
        userAppleMatchLs = query_json(json_content = json.loads(response),
                                      query        = "applyInfoList")
        return dict([(x["matchName"], x) for x in userAppleMatchLs])

    @resultData(param="getAppleMatchNum")
    def getCountAppleMath(self):
        return len(self.getMatchNameDict())
    #查询用户报名赛事的报名ID
    def getUserAppleIdByMatchName(self,response = None,matchName = None):
        matchDict = self.getMatchNameDict(response = response)
        if matchName in matchDict:
           return  matchDict[matchName]["applyId"]

    @decorator(["setupGetAppleId","tearDownGetAppleId"])
    def getAppleIdByMatchName(self):
        self.inputKV["applyId"] = self.getUserAppleIdByMatchName(matchName=self.inputKV["subMatchName"])

    #@check_rspdata(filepath = "userMatchAppleQueryRspFmt")
    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")


if __name__ == "__main__":
   args = {
            "matchId": 22,
            "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4"
        }
   umps = UserMatchAppleQueryService(kwargs=args)
   rsp = umps.userMatchAppleQuery()
   print(rsp)