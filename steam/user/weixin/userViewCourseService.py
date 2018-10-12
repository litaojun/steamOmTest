#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Lieb 
@license: Apache Licence  
@contact: 2750416737@qq.com 
@site: http://blog.csdn.net/hqzxsc2006 
@software: PyCharm 
@file: userViewCourseService.py 
@time: 2018/10/12 14:53 
"""

from opg.util.uopService import UopService
import json
from opg.util.utils import query_json
from steam.util.configurl import userViewCourseUrl
from opg.util.httptools import httpGet

class UserViewCourseService(UopService):
    '''
        用户查看课程
    '''
    def __init__(self, kwargs      = {},
                       modul       = "",
                       filename    = "",
                       reqjsonfile = "weixinUserVieeCourseReq"):
        """
            :param entryName:
            :param picturePath:
        """
        super(UserViewCourseService, self).__init__(  module       = modul,
                                                      filename     = filename,
                                                      sqlvaluedict = kwargs ,
                                                      reqjsonfile  = reqjsonfile )

    def userViewCourse(self):
        self.rsp =  httpGet(
                                  url     = userViewCourseUrl + self.reqjsondata,
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
                "token":"868eead96c634443a81170cf5fa87948"
             }
    uvcSer = UserViewCourseService(kwargs=kwargs)
    courseRsp = uvcSer.userViewCourse()
    print(courseRsp)