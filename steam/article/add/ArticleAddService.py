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
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import addArticleurl
from steam.util.configurl import delArticleurl
from steam.article.query.ArticleQueryService import ArticleQueryService
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import  fxt,articleAddReq
class ArticleAddService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAddService, self).__init__("", "", kwargs,reqjsonfile=fxt.join(articleAddReq))
        self.rsp = None
        self.articleReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    @decorator("tearInterfaceDelOneArticle")
    def delArticle(self):
        articleid = self.getArticleIdByRsp(self.rsp)
        delclassfiyRsp = requests.post(
									        url=delArticleurl,
									        json={"resourceId": articleid},
									        headers=self.jsonheart,
									        verify=False
								      )
        print("delclassfiyRsp = %s" % delclassfiyRsp.text)
        return delclassfiyRsp.text

    def addArticle(self):
        addArticleRsp = requests.post(
		                                   url=addArticleurl,
		                                   json=self.articleReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        #self.articleReqjson[""] = self.getArticleIdByRsp(addArticleRsp)
        self.rsp = addArticleRsp.text
        print("addArticleRsp = %s" % addArticleRsp.text)
        return addArticleRsp.text

    @check_rspdata(filepath="\\steam\\article\jsonfmt\\addArticleRspFmt.json")
    def getRetcodeByArticleRsp(self,response = None):
        print("articleRsp=" + str(response))
        a = type(response)
        print(a)
        return query_json(json_content=json.loads(response), query="code")

    def getArticleIdByRsp(self,articleRsp = None):
        articleQs = ArticleQueryService(kwargs={"title":self.articleReqjson["title"],"resourceTypeId":self.articleReqjson["resourceTypeId"]})
        queryRsp = articleQs.queryArtcle()
        rssid = articleQs.getFirstResourceIdByRsp(queryRsp = queryRsp)
        return rssid

if __name__ == "__main__":
   pass