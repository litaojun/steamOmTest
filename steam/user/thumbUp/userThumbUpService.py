#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userThumbUp.py 
@time: 2018/7/4 14:52 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json,del_json_data
from steam.util.configurl import userThumbUpUrl,userCancelThumbUpUrl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserThumbUpReq,weixinUserThumbUpRspFmt
from opg.util.httptools import httpGet,httpPost
from opg.util.lginfo import  logger
import operator as op
class UserThumbUpService(UopService):
    '''
        首页配置数据
    '''
    def __init__(self, kwarg={},modul="",filename= "",reqjsonfile = weixinUserThumbUpReq):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserThumbUpService, self).__init__(modul, filename, sqlvaluedict=kwarg , reqjsonfile = reqjsonfile)
        self.rsp = None
        self.userThumbUpReqjson = self.reqjsondata
        self.jsonheart = {
	                         "x-token":"admin"
                         }

    def userThumbUp(self):
        userThumbUpRsp =  httpPost(
                                        url     = userThumbUpUrl,
                                        headers = self.jsonheart,
                                        reqJsonData = self.userThumbUpReqjson
                                  )
        self.rsp = userThumbUpRsp
        return userThumbUpRsp

    def userCancelThumbUp(self):
        userCancelThumbUpRsp =  httpPost(
                                        url     = userCancelThumbUpUrl,
                                        headers = self.jsonheart,
                                        reqJsonData = self.userThumbUpReqjson
                                  )
        self.rsp = userCancelThumbUpRsp
        return userCancelThumbUpRsp

    @check_rspdata(filepath=weixinUserThumbUpRspFmt)
    def getRetcodeByThumbUpRsp(self,response = None):
        print("ThumbUpRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

if  __name__ == "__main__":
    kwarg = {
               "resourceId":"2104",
               "memberId":"09c1316f-b304-46b1-96ff-c9ebbd93a617"
            }
    userThumSer = UserThumbUpService(kwarg=kwarg)
    rsp = userThumSer.userThumbUp()
    retcode = userThumSer.getRetcodeByThumbUpRsp(response=rsp)
    print(retcode)
    rsp = userThumSer.userCancelThumbUp()
    retcode = userThumSer.getRetcodeByThumbUpRsp(response=rsp)
    print(retcode)