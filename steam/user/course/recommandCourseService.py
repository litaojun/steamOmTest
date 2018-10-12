#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: recommandCourseService.py 
@time: 2018/10/12 16:29 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import recommandCourseUrl
from opg.util.httptools import httpGet

class RecommandCourseService(UopService):
    '''
        用户查看推荐课程列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = "recommandCourseReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(RecommandCourseService, self).__init__(  module       = modul,
                                                       filename     = filename,
                                                       sqlvaluedict = kwargs ,
                                                       reqjsonfile  = reqjsonfile )

    def recommandCourseList(self):
        self.rsp =  httpGet(
                                  url     = recommandCourseUrl + self.reqjsondata,
                                  headers = self.jsonheart
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "courseId":4165,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"63779ff8becd413f9c389331592d5d96"
             }
    uvcSer = RecommandCourseService(kwargs=kwargs)
    courseRsp = uvcSer.recommandCourseList()
    print(courseRsp)