#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: queryAliyunVideoAuthService.py 
@time: 2018/10/12 17:36 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import queryAliyunVideoAuthUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class QueryAliyunVideoAuthService(HttpUopService):
    '''
        用户获取播放权限信息
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(QueryAliyunVideoAuthService, self).__init__(  module       = modul,
                                                            filename     = filename,
                                                            sqlvaluedict = kwargs ,
                                                            reqjsonfile  = reqjsonfile )

    def getAliyunVideoAuthReq(self):
        self.rsp =  httpGet(
                                  url     = queryAliyunVideoAuthUrl + self.reqjsondata,
                                  headers = self.jsonheart
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json( json_content = json.loads(response),
                           query        = "code" )

if  __name__ == "__main__":
    kwargs = {
                "courseId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"e0e1db2796f943259d1d87a7a48d727f"
             }
    uvcSer    = QueryAliyunVideoAuthService(kwargs=kwargs)
    courseRsp = uvcSer.getAliyunVideoAuthReq()
    print(courseRsp)