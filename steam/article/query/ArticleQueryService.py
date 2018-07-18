#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleQueryService.py 
@time: 2018/4/23 13:49 
"""
from opg.util.uopService import UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import queryArticleurl
from steam.util.reqFormatPath import fxt,articleQueryReq,articleQueryRspFmt
from opg.util.httptools import httpGet
class ArticleQueryService(UopService):
    '''
        查询分类
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleQueryService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(articleQueryReq))
        # self.rsp = None
        self.queryArticleUrl = queryArticleurl + self.reqjsondata
        # self.jsonheart = {
	     #                     "x-token":"admin"
        #                  }

    def queryArtcle(self):
        queryResultrsp = httpGet(url=self.queryArticleUrl,headers={})
        return  queryResultrsp

    def getFirstResourceIdByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.targets.0.id")

if __name__ == "__main__":
    queryJsonData = {"title":"奥林匹克大赛2017年12月北京赛区","resourceTypeId":2}
    aqs = ArticleQueryService(kwargs=queryJsonData)
    queryResultRsp = aqs.queryArtcle()
    rsid = aqs.getFirstResourceIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)
