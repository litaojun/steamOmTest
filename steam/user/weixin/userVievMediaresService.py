#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userVievMediaresService.py 
@time: 2018/7/4 17:01 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userViewMediaresUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserViewMediaresReq,weixinUserViewMediaresRspFmt
from opg.util.httptools import httpGet,httpPost
from steam.article.query.ArticleQueryService import ArticleQueryService
from steam.user.login.userLoginService import WeixinUserLoginService

class UserViewMediaresService(UopService):
    '''
        用户端通过文章ID浏览详情页面
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = weixinUserViewMediaresReq):
        """
        :param kwarg:
        :param modul:
        :param filename:
        :param reqjsonfile:
        """
        super(UserViewMediaresService, self).__init__(module      = modul,
                                                      filename    = filename,
                                                      sqlvaluedict= kwargs ,
                                                      reqjsonfile = reqjsonfile)

    def userViewMediares(self):
        self.rsp =  httpGet(
                                url     = userViewMediaresUrl + self.reqjsondata,
                                headers = self.jsonheart
                            )
        return self.rsp

    @check_rspdata(filepath=weixinUserViewMediaresRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

    def getCollectsNumByRsp(self,response = None):
        return query_json(json_content=json.loads(response),
                          query       ="data.collects")

if  __name__ == "__main__":
    kwarg = {
                "memberId": "09c1316f-b304-46b1-96ff-c9ebbd93a617",
                "title": "OM的诞生与发展",
                "resourceTypeId": 2,
                "token":""
            }
    aqs = ArticleQueryService(kwargs=kwarg)
    queryResultRsp = aqs.queryArtcle()
    rsid = aqs.getFirstResourceIdByRsp(queryRsp=queryResultRsp)
    kwarg["resourceId"] = rsid
    uvms = UserViewMediaresService(kwarg=kwarg)
    rsp = uvms.userViewMediares()
    retcode = uvms.getRetcodeByRsp(response=rsp)
    print(retcode)
    collNum = uvms.getCollectsNumByRsp(response=rsp)
    print(collNum)