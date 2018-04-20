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
from steam.util.configurl import addentryurl
from steam.util.configurl import delEntryurl
# from steam.classify.delclassify.delClassifyService import ClassfiyDelService

class ArticleAddService(UopService):
    '''
        分类新增
    '''
    def __init__(self, kwargs):
        """
        :param entryName:
        :param picturePath:
        """
        super(ArticleAddService, self).__init__("", "", kwargs)
        self.rsp = None
        self.articleReqjson = {
									"title": kwargs["title"],  #奥林匹克大赛2017年12月北京赛区
									"subtitle": kwargs[""],   #奥林匹克大赛2017年12月北京赛区-副标题
									"content": kwargs["content"] ,#"<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n<ul><li>fasf</li><li>asdfff</li><li><table style=\"border-collapse: collapse; width: 100%;\" border=\"1\" data-mce-style=\"border-collapse: collapse; width: 100%;\"><tbody><tr><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\">ffff</td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td></tr><tr><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br></td><td style=\"width: 16.6667%;\" data-mce-style=\"width: 16.6667%;\"><br data-mce-bogus=\"1\"></td></tr></tbody></table></li></ul>\n</body>\n</html>",
									"cornerMask":kwargs["cornerMask"],   # "花絮",
									"vendorId":kwargs["vendorId"] ,  #1,
									"baseVisits": kwargs["baseVisits"],  #"1",
									"baseCollects": kwargs["baseCollects"],  #1,
									"shareTitle": kwargs["shareTitle"] , #"奥林匹克大赛2017年12月北京赛区-分享标题",
									"thumbUrl": kwargs["thumbUrl"] ,#"http://uat-steam.opg.cn/_static/admin/images/resource/20180420161204_726874.png",
									"bannerUrl": kwargs["bannerUrl"], #"http://uat-steam.opg.cn/_static/admin/images/resource/20180420161213_347806.jpg",
									"shareDescription":kwargs["shareDescription"],   # "分享标题",
									"shareImgUrl": kwargs["shareImgUrl"] , #"http://uat-steam.opg.cn/_static/admin/images/resource/20180420161228_57360.png",
									"tags": eval(kwargs["tags"]) , #[2, 3],
									"entryIds":eval(kwargs["entryIds"]),  # [60],
									"matchId": int(kwargs["matchId"]) ,#20,
									"resourceTypeId": int(kwargs["resourceTypeId"]), #2,
									"state": kwargs["state"]  #"00"
								}
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    @decorator("tearInterfaceDelOneArticle")
    def delArticle(self):
        articleId = self.getArticleIdByRsp()
        delclassfiyRsp = requests.post(
									        url=delEntryurl,
									        json={"articleId": articleId},
									        headers=self.jsonheart,
									        verify=False
								      )
        print("delclassfiyRsp = %s" % delclassfiyRsp.text)
        return delclassfiyRsp.text

    def addArticle(self):
        addArticleRsp = requests.post(
		                                   url=addentryurl,
		                                   json=self.articleReqjson,
		                                   headers=self.jsonheart,
		                                   verify=False
                                      )
        self.rsp = addArticleRsp.text
        print("addArticleRsp = %s" % addArticleRsp.text)
        return addArticleRsp.text

    def getRetcodeByArticleRsp(self,articleRsp = None):
        print("articleRsp=" + str(articleRsp))
        return query_json(json_content=json.loads(articleRsp), query="code")

    def getArticleIdByRsp(self,articleRsp = None):
	    return query_json(json_content=json.loads(articleRsp), query="data")


if __name__ == "__main__":
	pass  