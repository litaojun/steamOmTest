#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleSearchService.py 
@time: 2018/12/4 16:58 
"""
from opg.util.uopService import decorator
import json
from opg.util.utils import query_json
from steam.util.httpUopService import  HttpUopService
class ArticleSearchService(HttpUopService):
    '''
        管理员分页搜索文章视频
    '''
    def __init__(self, kwargs):

        super(ArticleSearchService, self).__init__("", "", kwargs,reqjsonfile=None)

    def queryArtcle(self):
        self.rsp = self.sendHttpReq()
        return  self.rsp

    @decorator(["setupGetFirstMedia","tearDownGetFirstMedia"])
    def getFirstResourceIdByRsp(self):
        if self.rsp is None:
           self.rsp = self.sendHttpReq()
        self.inputKV["resourceId"] = query_json(json_content = json.loads(self.rsp),
                                                  query        = "data.targets.0.id")

    def findTestdataByStatus(self):
        if self.rsp is None:
            self.rsp = self.sendHttpReq()
        dataLs = query_json( json_content = json.loads(self.rsp),
                             query        = "data.targets" )
        if len(dataLs) == 0 :
            return "100001"
        if dataLs[0].status == self.inputKV["status"] :
           self.getFirstResourceIdByRsp()
           return "100002"