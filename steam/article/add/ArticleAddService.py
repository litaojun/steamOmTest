#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleAddService.py 
@time: 2018/4/20 16:17 
"""
from opg.util.uopService import decorator,UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import addArticleurl
from steam.util.configurl import delArticleurl
from steam.article.query.ArticleQueryService import ArticleQueryService
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import  fxt,articleAddReq,articleAddRspFmt
from opg.util.httptools import httpPost
class ArticleAddService(UopService):
    '''
        管理后台新增文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAddService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(articleAddReq))
        self.articleReqjson = self.reqjsondata

    @decorator("tearInterfaceDelOneArticle")
    def delArticle(self):
        articleid = self.getArticleIdByRsp(self.rsp)
        delclassfiyRsp = httpPost(url         = delArticleurl,
                                  headers     = self.jsonheart,
                                  reqJsonData = {"resourceId": articleid})
        return delclassfiyRsp

    def addArticle(self):
        addArticleRsp = httpPost(url         = addArticleurl,
                                 headers     = self.jsonheart,
                                 reqJsonData = self.reqjsondata)
        self.rsp      = addArticleRsp
        return addArticleRsp

    @check_rspdata(filepath=fxt.join(articleAddRspFmt))
    def getRetcodeByArticleRsp(self,response = None):
        return query_json(json_content=json.loads(response), query="code")

    def getArticleIdByRsp(self,articleRsp = None):
        articleQs = ArticleQueryService(kwargs=self.inputKV)
        queryRsp = articleQs.queryArtcle()
        rssid = articleQs.getFirstResourceIdByRsp(queryRsp = queryRsp)
        return rssid

if __name__ == "__main__":
   pass