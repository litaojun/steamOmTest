#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userMatchAppleService.py 
@time: 2018/7/23 14:14 
"""
from opg.util.uopService import decorator,UopService
import requests,json
from opg.util.utils import query_json
from steam.util.configurl import weixinUserLoginurl
from opg.util.schemajson import check_rspdata
from steam.util.reqFormatPath import weixinUserLoginReq,weixinUserLoginRspFmt
from opg.util.httptools import httpGet,httpPost
class UserMatchAppleService(UopService):
    '''
        微信端用户登录
    '''
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserMatchAppleService, self).__init__("", "", kwargs , reqjsonfile = "UserMatchAppleRspFmt")
        self.userMacthAppleReqjson = self.reqjsondata

    def weixinUserLogin(self):
        self.rsp = httpPost(url=weixinUserLoginurl,
                            headers=self.jsonheart,
                            reqJsonData=self.weixinUserLoginReqjson)
        return self.rsp


    def getMemberIdFromRsp(self,response=None):
        return query_json(json_content=json.loads(response), query="data.memberId")

    @check_rspdata(filepath=weixinUserLoginRspFmt)
    def getRetcodeByUserLoginRsp(self,response = None):
        print("homePageCnfRsp=" + str(response))
        return query_json(json_content=json.loads(response), query="code")

if __name__ == "__main__":
   args = {
              "phoneNo":"18916899938",
              "loginType":"NM",
              "verfiyCode":""
          }