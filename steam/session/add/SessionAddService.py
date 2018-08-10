#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: SessionAddService.py 
@time: 2018/7/30 11:50 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.schemajson import check_rspdata
from opg.util.utils import query_json
from steam.util.configurl import sessionAddUrl
from opg.util.httptools import httpPost
class SessionAddService(UopService):
    '''
        管理员新增场次
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(SessionAddService, self).__init__(module = "",
                                                    filename= "",
                                                    sqlvaluedict = kwargs ,
                                                    reqjsonfile = "sessionAddReq",
                                                    dbName="match")

    @decorator(["preInterfaceUserMatch"])
    def sessionAddReq(self):
        self.rsp = httpPost(url    = sessionAddUrl,
                            headers = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    @check_rspdata(filepath = "sessionAddRspFmt")
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
   argcs = {
                    "matchId": "需要服务器分配ID",
                    "matchName": "第11届世界奥林匹克大赛湖北场次",
                    "applyStartTime": 1532925382000,
                    "applyEndTime": 1533270987000,
                    "limitCount": 2,
                    "parentId": 22,
                    "state": 1,
                    "applyNum": 0
            }
   umas = SessionAddService(kwargs=argcs)
   rsp = umas.sessionAddReq()
   retcode = umas.getRetcodeByRsp(response=rsp)
   print(retcode)