#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: weixinSearchService.py 
@time: 2018/8/13 17:11 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userSearchEntryUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class UserSearchEntryService(HttpUopService):
    '''
          微信端-分类搜索
    '''
    def __init__(self,kwargs):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserSearchEntryService, self).__init__(module       =  "",
                                                     filename     =  "",
                                                     sqlvaluedict =  kwargs,
                                                     reqjsonfile  =  "userSearchEntryReq")

    def userSearchEntryReq(self):
        self.rsp = self.sendHttpReq()
        return self.rsp

    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

if __name__ == "__main__":
    queryJsonData = {
                         "entryId"     :75,
                         "currentPage":1,
                         "pageSize"   :10,
                         "resourceTypeId":12,
                         #"keyword":"早鸟价！呼伦贝尔｜私家牧场任你驰骋策马，原始森林徒步猎奇",
                         "keyword"  : "早鸟价",
                         "skuName"  :"价格（成人）",
                         "memberId" :"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                         "token"     :"e1974c2a63ab445dba7e0392b90a81bb"
                     }
    aqs = UserSearchEntryService(kwargs = queryJsonData)
    rsp = aqs.userSearchEntryReq()
    retcode = aqs.getRetcodeByRsp(response = rsp)
    print(retcode)
    print(rsp)