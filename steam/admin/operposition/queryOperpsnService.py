#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryOperpsnService.py 
@time: 2018/4/25 15:27 
"""
from opg.util.httptools import httpPost,httpGet
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import homeConfigQueryurl
from steam.util.configurl import delArticleurl
from steam.util.httpUopService import  HttpUopService
class OperpsnQueryService(HttpUopService):
    '''
        管理后台---运营位新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnQueryService, self).__init__(sqlvaluedict = kwargs)

    def queryOperpsnListdata(self):
        queryResult = httpGet(url     = homeConfigQueryurl + self.reqjsondata,
                              headers = self.jsonheart)
        return  queryResult

    def getRetCodeByRsp(self,queryRsp = None):
        return query_json(json_content = json.loads(queryRsp),
                          query        = "code")

    def getFirstResourceIdByRsp(self,queryRsp = None):
        if queryRsp is None:
            queryRsp = self.queryOperpsnListdata()
        return query_json(json_content = json.loads(queryRsp),
                          query        = "data.targets.0.id")

    def getFirstResourceTitleByRsp(self,queryRsp = None):
        return query_json(json_content = json.loads(queryRsp),
                          query        = "data.targets.0.title")

if __name__ == "__main__":
   queryjson = {
                  "position":"03",
	              "title":"",
                   "token":"a59fa2efd1774b2e9b925e27bb1bf630"
               }
   queryOper = OperpsnQueryService(queryjson)
   queryrst = queryOper.queryOperpsnListdata()
   id = queryOper.getFirstResourceIdByRsp(queryrst)
   print(id)

