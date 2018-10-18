#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: studyListService.py 
@time: 2018/10/16 17:06 
"""
from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userStudentCourseListUrl
from opg.util.httptools import httpGet

class StudyListService(UopService):
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
        super(StudyListService, self).__init__(  module       = modul,
                                                 filename     = filename,
                                                 sqlvaluedict = kwargs ,
                                                 reqjsonfile  = reqjsonfile )

    def getStudyListReq(self):
        self.rsp =  httpGet(
                                  url     = userStudentCourseListUrl ,
                                  headers = self.jsonheart
                            )
        return self.rsp

    #@check_rspdata(filepath=weixinUserViewActivityRspFmt)
    def getRetcodeByRsp(self,response = None):
        return query_json(json_content = json.loads(response),
                          query        = "code")

if  __name__ == "__main__":
    kwargs = {
                "courseId":4448,
                "materialId":15 ,
                "memberId":"e99abfeb-1ae5-41d8-a422-63bc108026d4",
                "token":"694c6006ac0a46ca8297000accc4e71e"
             }
    uvcSer    = StudyListService(kwargs=kwargs)
    courseRsp = uvcSer.getStudyListReq()
    print(courseRsp)
