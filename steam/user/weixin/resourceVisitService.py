#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: resourceVisitService.py 
@time: 2018/10/19 10:31 
"""
from steam.util.configurl import userResourceVisistUrl
from opg.util.httptools import httpPost
from steam.util.httpUopService import  HttpUopService
class ResourceVisitService(HttpUopService):
    '''
        用户浏览内容后浏览量+1
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(ResourceVisitService, self).__init__(  module       = modul,
                                                     filename     = filename,
                                                     sqlvaluedict = kwargs ,
                                                     reqjsonfile  = reqjsonfile )

    def sendInterfaceUrlReq(self):
        self.rsp =  httpPost(
                                  url         = userResourceVisistUrl ,
                                  reqJsonData = self.reqjsondata,
                                  headers     = self.jsonheart
                             )
        return self.rsp

    # def getRetcodeByRsp(self,response = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "resourceId" : 4165,
                "memberId"   : "e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token"        : "db1986b2283c418a8c68f3b3d66cd385",
                "chapterName"  : "第一章",
                 "sectionName" : "1、"
             }
    uvcSer = ResourceVisitService(kwargs=kwargs)
    rsp = uvcSer.sendInterfaceUrlReq()
    print(rsp)