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
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import userMatchAppleUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserLoginReq,weixinUserLoginRspFmt
from opg.util.httptools import httpGet,httpPost
class UserMatchAppleService(UopService):
    '''
        微信端用户登录
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserMatchAppleService, self).__init__(module = "weixin",
                                                    filename= "matchDb.xml",
                                                    sqlvaluedict = kwargs ,
                                                    reqjsonfile = "userMatchAppleReq",
                                                    dbName="match")

    @decorator(["preInterfaceUserMatch"])
    def userMatchApple(self):
        self.rsp = httpPost(url    = userMatchAppleUrl,
                            headers = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    #@check_rspdata(filepath = "userMatchAppleRspFmt")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")


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
   umps = UserMatchAppleService(kwargs=args)
   rsp = umps.userMatchApple()
   print(rsp)