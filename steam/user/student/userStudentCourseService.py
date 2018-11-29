#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userStudentCourseService.py 
@time: 2018/10/12 17:17 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userStudentCourseListUrl
from opg.util.httptools import httpGet
from steam.util.httpUopService import  HttpUopService
class UserStudentCourseService(HttpUopService):
    '''
        用户查看我的学习课程列表
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = "userStudentCourseReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserStudentCourseService, self).__init__(  module       = modul,
                                                         filename     = filename,
                                                         sqlvaluedict = kwargs ,
                                                         reqjsonfile  = None )

    def userStudentCourseList(self):
        self.rsp =  httpGet(
                                  url     = userStudentCourseListUrl,
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
    uvcSer    = UserStudentCourseService(kwargs=kwargs)
    courseRsp = uvcSer.userStudentCourseList()
    print(courseRsp)