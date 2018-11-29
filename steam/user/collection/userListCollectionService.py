#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userListCollectionService.py 
@time: 2018/10/18 16:09 
"""
from opg.util.uopService import UopService,decorator
import json
from   opg.util.utils import query_json
from   steam.util.configurl import userListCollectionUrl
from   opg.util.httptools import httpGet
from   steam.util.httpUopService import  HttpUopService
class UserListCollectionService(HttpUopService):
    '''
        用户学习列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = None):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserListCollectionService, self).__init__(  module       = modul,
                                                          filename     = filename,
                                                          sqlvaluedict = kwargs ,
                                                           reqjsonfile = reqjsonfile )

    def userListCollectionReq(self):
        self.rsp =  httpGet(
                                  url         = userListCollectionUrl ,
                                  headers     = self.jsonheart
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    # def getRetcodeByRsp(self,response  = None):
    #     return query_json(json_content = json.loads(response),
    #                       query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "resourceId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"18bcd2b48e7f4a89a5f9f5bd5d9918a6"
             }
    uvcSer    = UserListCollectionService(kwargs=kwargs)
    courseRsp = uvcSer.userListCollectionReq()
    print(courseRsp)