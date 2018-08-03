#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: SessionUpdateService.py 
@time: 2018/7/30 14:12 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.schemajson import check_rspdata
from opg.util.utils import query_json
from steam.util.configurl import sessionUpdateUrl
from opg.util.httptools import httpPost
class SessionUpdateService(UopService):
    '''
        管理员修改场次
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(SessionUpdateService, self).__init__(module = "",
                                                    filename= "",
                                                    sqlvaluedict = kwargs ,
                                                    reqjsonfile = "sessionUpdateReq",
                                                    dbName="match")

    @decorator(["preInterfaceUserMatch"])
    def sessionUpdateReq(self):
        self.rsp = httpPost(url    = sessionUpdateUrl,
                            headers = self.jsonheart,
                            reqJsonData = self.reqjsondata)
        return self.rsp

    @check_rspdata(filepath = "sessionUpdateRspFmt")
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
   umas = SessionUpdateService(kwargs=argcs)
   rsp = umas.sessionUpdateReq()
   retcode = umas.getRetcodeByRsp(response=rsp)
   print(retcode)