#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: QueryMemberIdService.py 
@time: 2018/8/13 9:55 
"""
import json
from opg.util.utils import query_json
# from steam.util.configurl import weixinUserMemberIdUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class QueryMemberIdService(HttpUopService):
    '''
        微信端用户登录后根据token换取memberId
    '''
    __interfaceName__ = "/member/login/queryMemberInfo"
    def __init__(self, kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(QueryMemberIdService, self).__init__(module    ="",
                                                     filename  ="",
                                                     sqlvaluedict = kwargs ,
                                                     reqjsonfile  = None)

    def userMemberIdReq(self):
        self.rsp = httpGet(url          =  weixinUserMemberIdUrl,
                           headers      =  self.jsonheart)
        return self.rsp

    def getMemberIdFromRsp(self,response=None):
        return query_json(json_content = json.loads(response),
                          query        = "data.memberId")

    #@check_rspdata(filepath=weixinUserLoginRspFmt)
    # def getRetcodeByRsp(self,response  = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

if __name__ == "__main__":
   args = {
              "phoneNo":"18916899938",
              "loginType":"NM",
              "verfiyCode":"",
              "scenes":"OTP"
          }