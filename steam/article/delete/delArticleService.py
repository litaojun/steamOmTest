#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: li.taojun 
@contact: li.taojun@opg.cn
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: delArticleService.py 
@time: 2018/4/23 15:27 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import delArticleurl,addArticleurl
from steam.classify.addclassify.addClassfiyService import ClassfiyAddService
from steam.article.add.ArticleAddService import ArticleAddService
from steam.article.query.ArticleQueryService import ArticleQueryService
from steam.util.reqFormatPath import fxt,articleDelReq,articleDelRspFmt
from opg.util.httptools import httpGet,httpPost
class ArticleDelService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleDelService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(articleDelReq))
        self.delArticleIdJson = self.reqjsondata
        self.articleSer = ArticleAddService(kwargs = kwargs)

    @decorator("preInterfaceAddOneArticle")
    def addOneArticle(self):
        articlersp = self.articleSer.addArticle()
        # articleid = self.articleSer.getArticleIdByRsp()

    def delArticleByResourceId(self,articleid):
        self.delArticleIdJson["resourceId"] = articleid
        delArticleRsp = httpPost(url=delArticleurl,
                                 headers=self.jsonheart,
                                 reqJsonData=self.delArticleIdJson)
        return delArticleRsp

    def delClassfiy(self,title = "",resourceTypeId = None):
        #resid = self.getArticleIdByTitle(self.articleReqjson["title"])
        resid = self.getArticleIdByTitle(title,resourceTypeId)
        delarticleRsp = self.delArticleByResourceId(resid)
        print("delarticleRsp = %s" % delarticleRsp)
        return delarticleRsp

    def getRetcodeByArticleRsp(self, articleRsp=None):
        print("classfiyRsp===" + str(articleRsp))
        return query_json(json_content=json.loads(articleRsp), query="code")

    def getArticleIdByTitle(self, title="",resourceTypeId = None):
         articleQs = ArticleQueryService(kwargs={"title": title,"resourceTypeId":resourceTypeId})
         queryRsp = articleQs.queryArtcle()
         rssid = articleQs.getFirstResourceIdByRsp(queryRsp=queryRsp)
         return rssid


if __name__ == "__main__":
   reqdata = {
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
   articleSer = ArticleDelService(reqdata)
   articleSer.addOneArticle()
   articleId = articleSer.getArticleIdByTitle(title = reqdata["title"],resourceTypeId=reqdata["resourceTypeId"])
   delarticleRsp = articleSer.delClassfiy(title = reqdata["title"],resourceTypeId=reqdata["resourceTypeId"])
   code = articleSer.getRetcodeByArticleRsp(delarticleRsp)