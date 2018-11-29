#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userCancelMatchAppleService.py 
@time: 2018/7/26 15:34 
"""
from opg.util.uopService import decorator,UopService
from steam.util.httpUopService import  HttpUopService
from steam.user.match.userMatchAppleService import UserMatchAppleService
from opg.util.utils import query_json
from steam.util.configurl import userCancelMatchAppleUrl
from opg.util.schemajson import check_rspdata
from opg.util.httptools import httpPost
from steam.user.match.userMatchAppleQueryService import UserMatchAppleQueryService
class UserCancelMatchAppleService(HttpUopService):
    '''
        微信端用户取消报名
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserCancelMatchAppleService, self).__init__(
                                                              module       = "weixin",
                                                              filename     = "matchDb.xml",
                                                              sqlvaluedict = kwargs ,
                                                              reqjsonfile  = None,
                                                              dbName       = "match"
                                                         )
    @decorator(["tearDownCancelMatchApple"])
    def userCancelMatchApple(self):
        # self.rsp = httpPost(url         = userCancelMatchAppleUrl,
        #                     headers     = self.jsonheart,
        #                     reqJsonData = self.reqjsondata)
        self.rsp = self.sendHttpReq()
        return self.rsp

    @decorator(["preInterfaceUserMatch"])
    def userMatchApple(self):
        userAppleMatchSer = UserMatchAppleService(kwargs=self.inputKV)
        # userAppleMatchSer.alterMatchTime()
        # userAppleMatchTwo()
        rsp = userAppleMatchSer.userMatchApple()
        self.reqjsondata["applyId"] = UserMatchAppleQueryService(self.inputKV).getUserAppleIdByMatchName(matchName=self.inputKV["subMatchName"])


    # @check_rspdata(filepath = "userCancelMatchAppleRspFmt")
    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

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
            "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
            "token":"69a42b2f9ebd4275a04a602648d857c1"
        }
   umps = UserCancelMatchAppleService(kwargs=args)
   rsp = umps.userCancelMatchApple()
   print(rsp)