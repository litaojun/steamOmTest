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
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import queryArticleurl
from steam.util.configurl import delArticleurl
# from steam.classify.delclassify.delClassifyService import ClassfiyDelService

class ArticleQueryService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleQueryService, self).__init__("", "", kwargs)
        self.rsp = None
        if "title" in kwargs:
             self.queryArticleUrl = queryArticleurl + "&title=" + kwargs["title"]
        self.queryArticleUrl = self.queryArticleUrl + "&resourceTypeId=" + str(kwargs["resourceTypeId"])
        # if "resourceTypeId"
        # resourceTypeId = 2
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def queryArtcle(self):
        queryResult = requests.get(url = self.queryArticleUrl)
        return  queryResult.text

    def getFirstResourceIdByRsp(self,queryRsp = None):
        return query_json(json_content=json.loads(queryRsp), query="data.targets.0.id")

if __name__ == "__main__":
    queryJsonData = {"title":"积分规则","resourceTypeId":2}
    aqs = ArticleQueryService(kwargs=queryJsonData)
    queryResultRsp = aqs.queryArtcle()
    rsid = aqs.getFirstResourceIdByRsp(queryRsp=queryResultRsp)
    print("rsid = %s" % rsid)
