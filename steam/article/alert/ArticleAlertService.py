#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: ArticleAlertService.py 
@time: 2018/4/23 14:29 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import alertArtcleurl
from steam.util.configurl import delArticleurl
from steam.article.query.ArticleQueryService import ArticleQueryService
from steam.article.add.ArticleAddService import ArticleAddService
from steam.util.reqFormatPath import fxt,articleAlertReq,articleAlertRspFmt
from opg.util.httptools import httpGet,httpPost
class ArticleAlertService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAlertService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(articleAlertReq))
        # self.rsp = None
        self.articleReqjson = self.reqjsondata
        self.artcleAddSer = ArticleAddService(kwargs=self.articleReqjson)

    @decorator("preInterfaceAddOneArticle")
    def addArticle(self):
        self.artcleAddSer.addArticle()

    @decorator("tearInterfaceDelOneArticle")
    def delArticle(self):
        articleId = self.getArticleIdByTitle(title = self.articleReqjson["title"])
        delclassfiyRsp = httpPost(url=delArticleurl,
                                 headers=self.jsonheart,
                                 reqJsonData={"resourceId": articleId})
        print("delclassfiyRsp = %s" % delclassfiyRsp)
        return delclassfiyRsp

    def alertArticle(self):
        resid = self.getArticleIdByTitle(self.articleReqjson["title"])
        self.articleReqjson["resourceId"] = resid
        addArticleRsp = httpPost(url=alertArtcleurl,
                                 headers=self.jsonheart,
                                 reqJsonData=self.articleReqjson)
        self.rsp = addArticleRsp
        print("addArticleRsp = %s" % addArticleRsp)
        return addArticleRsp

    def getRetcodeByArticleRsp(self,articleRsp = None):
        print("articleRsp=" + str(articleRsp))
        return query_json(json_content=json.loads(articleRsp), query="code")

    def getArticleIdByTitle(self,title = None):
        articleQs = ArticleQueryService(kwargs={"title":title,"resourceTypeId":self.articleReqjson["resourceTypeId"]})
        queryRsp = articleQs.queryArtcle()
        rssid = articleQs.getFirstResourceIdByRsp(queryRsp = queryRsp)
        return rssid


if __name__ == "__main__":
   reqdata  ={
				'title': '奥林匹克大赛2017年12月北京赛区-自动化',
				'subtitle': '奥林匹克大赛2017年12月北京赛区-副标题-自动化',
				'content': '<!DOCTYPE html><html><head></head><body><p>方法</p></body></html>',
				'cornerMask': '花絮',
				'vendorId': 1,
	            'baseVisits': '1',
				'baseCollects': 1,
				'shareTitle': '奥林匹克大赛2017年12月北京赛区-分享标题-自动化',
				'thumbUrl': 'http://uat-steam.opg.cn/_static/admin/images/resource/20180420161204_726874.png',
				'bannerUrl': 'http://uat-steam.opg.cn/_static/admin/images/resource/20180420161213_347806.jpg',
				'shareDescription': '分享标题-自动化',
				'shareImgUrl': 'http://uat-steam.opg.cn/_static/admin/images/resource/20180+F20420161228_57360.png',
				'tags': [2, 3],
				'entryIds': [60],
				'matchId': 20,
				'resourceTypeId': 2,
				'state': '00'
			}
   articleSer = ArticleAlertService(kwargs=reqdata)
   addrsp = articleSer.addArticle()
   articleid = articleSer.getArticleIdByTitle(articleSer.articleReqjson["title"])
   alertRsp = articleSer.alertArticle()
   retcode  = articleSer.getRetcodeByArticleRsp(alertRsp)
   articleSer.delArticle()
