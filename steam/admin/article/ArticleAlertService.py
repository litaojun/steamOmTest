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
import json
from opg.util.utils import query_json

from steam.util.httpUopService import  HttpUopService
class ArticleAlertService(HttpUopService):
    '''
        管理后台修改文章视频
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAlertService, self).__init__(module   = "",
                                                  filename = "",
                                                  sqlvaluedict = kwargs)
        self.articleReqjson = self.reqjsondata
        #self.artcleAddSer   = ArticleAddService(kwargs = self.articleReqjson)

    def alertArticle(self):
        self.sendHttpReq()

    def getRetcodeByArticleRsp(self,articleRsp = None):
        print("articleRsp=" + str(articleRsp))
        return query_json(json_content=json.loads(articleRsp), query="code")

    def getArticleIdByTitle(self,title = None):
        articleQs = ArticleQueryService(kwargs=self.inputKV)
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
