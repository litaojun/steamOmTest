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

from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import queryHomeConfigurl
from steam.util.configurl import delArticleurl
# from steam.classify.delclassify.delClassifyService import ClassfiyDelService

class OperpsnQueryService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(OperpsnQueryService, self).__init__("", "", kwargs)
        self.rsp = None
        self.queryHomeConfigurl = queryHomeConfigurl + str(kwargs["position"])
        if "title" in kwargs:
             self.queryHomeConfigurl = self.queryHomeConfigurl + "&title=" + kwargs["title"]
        # if "resourceTypeId"
        # resourceTypeId = 2
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryOperpsnListdata(self):
        queryResult = requests.get(url = self.queryHomeConfigurl,verify = False)
        return  queryResult.text

    def getRetCodeByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="code")
    def getFirstResourceIdByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.targets.0.id")

    def getFirstResourceTitleByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.targets.0.title")

if __name__ == "__main__":
   queryjson = {
                  "position":"03",
	              #"title":"Makeblock 2017 品牌视频"
               }
   queryOper = OperpsnQueryService(queryjson)
   queryrst = queryOper.queryOperpsnListdata()
   id = queryOper.getFirstResourceIdByRsp(queryrst)
   print(id)

