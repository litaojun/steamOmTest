#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchAppleService.py 
@time: 2018/7/23 14:14 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userMatchAppleUrl
from opg.util.httptools import httpPost
from steam.admin.login.userLoginService import UserLoginService
from steam.competition.update.competitionAlertService import CompetitionAlertService
from steam.user.match.appleResetTools import getTokenReset
class UserMatchAppleService(UopService):
    '''
        微信端用户登录
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserMatchAppleService, self).__init__(
                                                         module       = "weixin",
                                                         filename     = "matchDb.xml",
                                                         sqlvaluedict =  kwargs ,
                                                         reqjsonfile  =  kwargs["reqjsonfile"],
                                                         dbName       =  "match"
                                                    )

    @decorator(["preInterfaceUserMatch"])
    def userMatchApple(self):
        self.rsp = httpPost(
                               url         =  userMatchAppleUrl,
                               headers     =  self.jsonheart,
                               reqJsonData =  self.reqjsondata
                            )
        return self.rsp

    @decorator(["preInterfaceUserCancelMatch"])
    def userCancelMatchApple(self):
        pass

    def getRetcodeByRsp(self,response  = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def getAppleIdFromRsp(self,response = None):
        return query_json(json_content  = json.loads(response),
                          query         = "applyId")

    @decorator(["preInterfaceUserAlertMatch"])
    def alterMatchTime(self):
        args = {
                  "username":"cuiyiming",
                  "password":"68039c0183cd34950fc57726f3b23446701c36a7898e66a61a805f4474b5a63c"
               }
        token = UserLoginService(kwargs=args).getTokenData()
        reqdata = {}
        reqdata["token"]        = token
        reqdata["matchId"]      = self.reqjsondata["subMatchId"]
        reqdata["matchName"]    = self.reqjsondata["subMatchName"]
        reqdata["applyStartTime"]   = 11111111111
        reqdata["applyEndTime"]     = 11111111111
        reqdata["reqjsonfile"]      = "competitionLabAlertReq"
        reqdata["limitCount"]   = self.inputKV["limitCount"]
        matchAlertSer             = CompetitionAlertService(kwargs = reqdata)
        if self.inputKV["sign"] == "start":
           matchAlertSer.alertMatchTime(s=-1,e=1)
        if self.inputKV["sign"] == "notStart":
           matchAlertSer.alertMatchTime(s=1, e=2)
        if self.inputKV["sign"] == "end":
           matchAlertSer.alertMatchTime(s=-2, e=-1)

    def resetToken(self):
        self.jsonheart["token"] = getTokenReset( phoneNo = self.inputKV["phoneNo"])

if __name__ == "__main__":
   args = {
            "matchId"       :  22,
            "subMatchId"    : 23,
            "subjectIdList" : [1, 4, 6],
            "contactName"   : "李陶军",
            "contactPhone"  :  "18916899938",
            "studentName"   : "李陶军",
            "province"      :  "上海",
            "city"     : "上海市",
            "country" : "黄浦区",
            "group"   : "幼儿园",
            "school"  : "文庙路幼儿园",
            "nationality"  : "",
            "subMatchName" : "亲子擂台赛初赛",
            "memberId"      : "e99abfeb-1ae5-41d8-a422-63bc108026d4"
        }
   umps = UserMatchAppleService(kwargs=args)
   rsp = umps.userMatchApple()
   print(rsp)