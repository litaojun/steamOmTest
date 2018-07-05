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
from steam.util.configurl import userThumbUpUrl,userCancelThumbUpUrl
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
        userThumbUpRsp =  httpPost(
                                        url     = userThumbUpUrl,
                                        headers = self.jsonheart,
                                        reqJsonData = self.userThumbUpReqjson
                                  )
        self.rsp = userThumbUpRsp
        return userThumbUpRsp

    @check_rspdata(filepath=weixinUserViewMediaresRspFmt)
    def getRetcodeByThumbUpRsp(self,response = None):
        print("ThumbUpRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")