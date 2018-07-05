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
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json,del_json_data
from steam.util.configurl import userViewMediaresUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserViewMediaresReq,weixinUserViewMediaresRspFmt
from opg.util.httptools import httpGet,httpPost
class UserViewMediaresService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwarg={},modul="",filename= "",reqjsonfile = weixinUserViewMediaresReq):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserViewMediaresService, self).__init__(modul, filename, sqlvaluedict=kwarg , reqjsonfile = reqjsonfile)
        self.rsp = None
        self.userThumbUpReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def userViewMediares(self):
        userViewMediaresRsp =  httpGet(
                                            url     = userViewMediaresUrl + self.userThumbUpReqjson,
                                            headers = self.jsonheart
                                        )
        self.rsp = userViewMediaresRsp
        return userViewMediaresRsp

    @check_rspdata(filepath=weixinUserViewMediaresRspFmt)
    def getRetcodeByRsp(self,response = None):
        print("ThumbUpRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

if  __name__ == "__main__":
    kwarg = {
                "resourceId": "2104",
                "memberId": "09c1316f-b304-46b1-96ff-c9ebbd93a617"
            }
    uvms = UserViewMediaresService(kwarg=kwarg)
    rsp = uvms.userViewMediares()
    retcode = uvms.getRetcodeByRsp(response=rsp)
    print(retcode)